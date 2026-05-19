#!/usr/bin/env python3
"""Генерация Markdown-документации API из OpenAPI (swagger.yaml)."""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[1]
SWAGGER = ROOT / "swagger.yaml"
API_DIR = ROOT / "api"

TAG_FILES = {
    "Authentication (Employees)": "authentication",
    "Authentication (Clients)": "authentication",
    "Roles": "employees-and-roles",
    "Employees": "employees-and-roles",
    "Clients": "clients",
    "Client Addresses": "clients",
    "Dishes": "dishes-and-menus",
    "Photos": "dishes-and-menus",
    "Avatars": "employees-and-roles",
    "Menus": "dishes-and-menus",
    "Ingredients": "dishes-and-menus",
    "Order Statuses": "orders",
    "Orders": "orders",
    "Order Items": "orders",
}

METHOD_ORDER = ["get", "post", "put", "patch", "delete"]

# Соответствует SecurityConfig в backend (ветка employee).
STANDARD_RESPONSE_EXAMPLES: dict[str, object] = {
    "401": {
        "error": "Unauthorized",
        "exception": "Unauthorized",
        "message": "Неверный логин или пароль",
        "timestamp": "2024-01-15T10:30:00Z",
    },
    "403": {
        "error": "Forbidden",
        "exception": "Forbidden",
        "message": "Недостаточно прав для выполнения операции",
        "timestamp": "2024-01-15T10:30:00Z",
    },
    "404": {
        "error": "Not Found",
        "exception": "Resource not found",
        "message": "Resource not found: id=999",
        "timestamp": "2024-01-15T10:30:00Z",
    },
    "422": {
        "error": "Validation Error",
        "message": "Invalid input data",
        "fields": {
            "login": ["Длина логина должна быть от 4 до 16 символов"],
            "password": ["Пароль обязателен"],
        },
    },
}


def resolve_ref(spec: dict, ref: str) -> dict:
    if not ref.startswith("#/"):
        return {}
    parts = ref.lstrip("#/").split("/")
    node = spec
    for p in parts:
        node = node.get(p, {})
    return node


def schema_example(spec: dict, schema: dict, depth: int = 0) -> object:
    if depth > 4:
        return {}
    if "$ref" in schema:
        schema = resolve_ref(spec, schema["$ref"])
    if "example" in schema:
        return schema["example"]
    if "enum" in schema:
        return schema["enum"][0]
    t = schema.get("type")
    if t == "object":
        props = schema.get("properties", {})
        return {k: schema_example(spec, v, depth + 1) for k, v in props.items()}
    if t == "array":
        return [schema_example(spec, schema.get("items", {}), depth + 1)]
    if t == "integer":
        return 1
    if t == "number":
        return 9.99
    if t == "boolean":
        return True
    return "string"


def json_block(obj: object) -> str:
    return "```json\n" + json.dumps(obj, ensure_ascii=False, indent=2) + "\n```"


def security_line(security: list | None) -> str:
    if not security:
        return "Публичный (без авторизации)"
    parts = []
    for req in security:
        for name in req:
            if name == "jwtEmployee":
                parts.append("JWT сотрудника")
            elif name == "jwtClient":
                parts.append("JWT клиента")
            else:
                parts.append(name)
    return "; ".join(parts) if parts else "Требуется авторизация"


def access_roles(method: str, path: str) -> str:
    """Роли по SecurityConfig (authority), не только по полю security в OpenAPI."""
    m = method.upper()
    if path.startswith("/auth/"):
        return "Публичный"
    if path.startswith("/roles/") or path.startswith("/order-statuses"):
        return "Admin"
    if path.startswith("/employees"):
        return "Admin, Manager" if m == "GET" else "Admin"
    if path.startswith("/clients"):
        if m == "DELETE":
            return "Admin"
        if m == "POST":
            return "Admin, Manager"
        if m in ("GET", "PUT", "PATCH"):
            return "Admin, Manager, Client (свой профиль)"
    if any(path.startswith(p) for p in ("/dishes", "/menus", "/ingredients")):
        return "Admin, Manager, Client, Courier (GET); Admin, Manager (изменение)" if m == "GET" else "Admin, Manager"
    if path.startswith("/photos") or path.startswith("/avatars"):
        return "Любой аутентифицированный (GET); Admin, Manager (загрузка/удаление)" if m == "GET" else "Admin, Manager"
    if path.startswith("/orders"):
        if m == "POST":
            return "Admin, Manager, Client"
        if m == "DELETE":
            return "Admin"
        if m == "PUT":
            return "Admin, Manager"
        return "Admin, Manager, Courier, Client"
    return "Аутентифицированный"


def response_example(spec: dict, code: str, resp: dict) -> object | None:
    if code in STANDARD_RESPONSE_EXAMPLES:
        return STANDARD_RESPONSE_EXAMPLES[code]
    content = resp.get("content", {})
    app_json = content.get("application/json", {})
    ex = app_json.get("example")
    if ex is not None:
        return ex
    schema = app_json.get("schema", {})
    if schema:
        return schema_example(spec, schema)
    return None


def format_parameters(params: list) -> str:
    if not params:
        return "Нет."
    lines = [
        "| Имя | In | Тип | Обязательный | Описание |",
        "|-----|-----|-----|--------------|----------|",
    ]
    for p in params:
        sch = p.get("schema", {})
        ptype = sch.get("type", p.get("type", "—"))
        lines.append(
            f"| `{p['name']}` | {p.get('in', '')} | {ptype} | "
            f"{'да' if p.get('required') else 'нет'} | {p.get('description', '')} |"
        )
    return "\n".join(lines)


def format_request_body(spec: dict, rb: dict) -> list[str]:
    content = rb.get("content", {})
    lines: list[str] = []
    if "multipart/form-data" in content:
        mp = content["multipart/form-data"]
        schema = mp.get("schema", {})
        if "$ref" in schema:
            schema = resolve_ref(spec, schema["$ref"])
        props = schema.get("properties", {})
        lines.extend([
            "**Тело запроса:** `Content-Type: multipart/form-data`",
            "",
            "| Поле | Тип | Обязательный |",
            "|------|-----|--------------|",
        ])
        for name, prop in props.items():
            required = name in schema.get("required", [])
            lines.append(
                f"| `{name}` | {prop.get('type', 'string')} | {'да' if required else 'нет'} |"
            )
        lines.extend(["", "Лимит размера файла: 10 MB (`spring.servlet.multipart.max-file-size`).", ""])
        return lines
    app_json = content.get("application/json", {})
    schema = app_json.get("schema", {})
    ex = app_json.get("example")
    if ex is None and schema:
        ex = schema_example(spec, schema)
    lines.extend(["**Тело запроса (пример):**", "", json_block(ex), ""])
    return lines


def operation_block(spec: dict, path: str, method: str, op: dict) -> str:
    summary = op.get("summary", op.get("operationId", ""))
    desc = op.get("description", "")
    roles = access_roles(method, path)
    lines = [
        f"### `{method.upper()} {path}`",
        "",
        f"**{summary}**",
        "",
    ]
    if desc:
        lines.extend([desc.strip(), ""])
    lines.extend([
        f"- **Авторизация (OpenAPI):** {security_line(op.get('security'))}",
        f"- **Доступ по ролям (SecurityConfig):** {roles}",
        "",
        "**Параметры:**",
        "",
        format_parameters(op.get("parameters", [])),
        "",
    ])
    rb = op.get("requestBody")
    if rb:
        lines.extend(format_request_body(spec, rb))
    for code, resp in sorted(op.get("responses", {}).items()):
        ex = response_example(spec, code, resp)
        if ex is not None:
            lines.extend([f"**Ответ {code} (пример):**", "", json_block(ex), ""])
        else:
            lines.extend([f"**Ответ {code}:** {resp.get('description', '')}", ""])
    lines.append("---")
    lines.append("")
    return "\n".join(lines)


def main() -> int:
    with open(SWAGGER, encoding="utf-8") as f:
        spec = yaml.safe_load(f)

    by_file: dict[str, list[str]] = {}
    index_rows: list[str] = []

    paths = spec.get("paths", {})
    for path in sorted(paths.keys()):
        path_item = paths[path]
        for method in METHOD_ORDER:
            if method not in path_item:
                continue
            op = path_item[method]
            tags = op.get("tags", ["Other"])
            tag = tags[0]
            fname = TAG_FILES.get(tag, "other")
            block = operation_block(spec, path, method, op)
            by_file.setdefault(fname, [])
            if not by_file[fname] or not by_file[fname][0].startswith("# "):
                titles = {
                    "authentication": "Авторизация",
                    "employees-and-roles": "Роли, сотрудники, аватары",
                    "clients": "Клиенты и адреса",
                    "dishes-and-menus": "Блюда, меню, ингредиенты, фото",
                    "orders": "Заказы и статусы",
                }
                by_file[fname] = [
                    f"# {titles.get(fname, fname)}",
                    "",
                    "Базовый URL: `http://localhost:8080`",
                    "",
                    "Полная спецификация: [swagger.yaml](../swagger.yaml).",
                    "Матрица прав: [errors-and-auth.md](errors-and-auth.md) — при расхождении с OpenAPI доверяйте SecurityConfig.",
                    "",
                    "---",
                    "",
                ]
            by_file[fname].append(block)
            index_rows.append(
                f"| `{method.upper()}` | `{path}` | {access_roles(method, path)} | "
                f"{op.get('summary', '')} | [{fname}.md]({fname}.md) |"
            )

    API_DIR.mkdir(parents=True, exist_ok=True)
    for fname, parts in by_file.items():
        out = API_DIR / f"{fname}.md"
        out.write_text("\n".join(parts), encoding="utf-8")
        print(f"Wrote {out}")

    index = [
        "# Справочник API",
        "",
        "REST API системы управления рестораном. JSON в формате **snake_case**.",
        "",
        "Колонка **Роли** отражает `SecurityConfig` backend, а не только поле `security` в OpenAPI.",
        "",
        "## Быстрые ссылки",
        "",
        "- [Авторизация](authentication.md)",
        "- [Роли и сотрудники](employees-and-roles.md)",
        "- [Клиенты](clients.md)",
        "- [Блюда и меню](dishes-and-menus.md)",
        "- [Заказы](orders.md)",
        "- [Ошибки и JWT](errors-and-auth.md)",
        "- [OpenAPI (YAML)](../swagger.yaml)",
        "",
        "## Query-параметры (часто используемые)",
        "",
        "| Endpoint | Параметр | Назначение |",
        "|----------|----------|------------|",
        "| `GET /employees` | `role_id` | Фильтр по роли (1=ADMIN, 2=MANAGER, 3=COURIER) |",
        "| `GET /employees` | `is_working` | Курьеры/сотрудники на смене |",
        "| `GET /orders` | `client_id` | Заказы клиента |",
        "| `GET /orders` | `courier_id` | Заказы курьера |",
        "| `GET /menus` | `is_active` | Только активные меню (для витрины клиента) |",
        "",
        "## Все операции",
        "",
        "| Метод | URL | Роли | Описание | Детали |",
        "|-------|-----|------|----------|--------|",
        *index_rows,
    ]
    (API_DIR / "index.md").write_text("\n".join(index), encoding="utf-8")
    print(f"Wrote {API_DIR / 'index.md'}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
