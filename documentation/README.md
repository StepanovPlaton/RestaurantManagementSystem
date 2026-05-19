# Документация Restaurant Management System

Актуальная техническая документация целевой системы. Пояснительная записка (курсовой проект) не изменяется; расхождения с ней — в [замечаниях](zamechaniya-k-poyasnitelnoj-zapiske.md).

## Backend (источник истины для данных и API)

| Параметр               | Значение                                                                                        |
| ---------------------- | ----------------------------------------------------------------------------------------------- |
| Репозиторий            | [restaurant-backend](https://github.com/KarpinDmitry/restaurant-backend) (submodule `backend/`) |
| Ветка с полным API     | `employee`                                                                                      |
| Зафиксированный commit | `205d9583c23477ca04e554119cd935524a7e09ef`                                                      |
| OpenAPI в backend      | `backend/src/main/resources/openapi.yaml`                                                       |

## Оглавление

### Продукт

- [Краткое описание](product/overview.md)

### Роли и интерфейс

- [Сводка по ролям](roles/index.md)
- [Администратор](roles/admin.md)
- [Менеджер](roles/manager.md)
- [Курьер](roles/courier.md)
- [Клиент](roles/client.md)

### Данные

- [Сущности и поля](data/entities.md)
- [Перечисления и справочники](data/enums.md)
- [db.dbml](db.dbml) — схема для dbdiagram.io
- ERD: [screenshots/ERD.png](../screenshots/ERD.png) (обновить экспортом из dbml, см. ниже)

### API

- [Индекс endpoint-ов](api/index.md)
- [Авторизация](api/authentication.md)
- [Роли и сотрудники](api/employees-and-roles.md)
- [Клиенты](api/clients.md)
- [Блюда и меню](api/dishes-and-menus.md)
- [Заказы](api/orders.md)
- [Ошибки и JWT](api/errors-and-auth.md)
- [swagger.yaml](swagger.yaml) — OpenAPI 3.0

### Прочее

- [Пояснительная записка (архив проектирования)](пояснительная-записка/index.md)
- [Замечания к пояснительной записке](zamechaniya-k-poyasnitelnoj-zapiske.md)
- [Расхождения техдокументации с кодом](raszhozhdeniya-dokumentacii.md)

## Обновление документации

1. После изменений в backend — обновить `swagger.yaml` из `backend/src/main/resources/openapi.yaml`.
2. Перегенерировать API Markdown (колонка «Роли» из SecurityConfig, исправленные примеры ошибок):
   ```bash
   pip install pyyaml
   python documentation/scripts/openapi_to_api_md.py
   ```
   Файл `api/errors-and-auth.md` скрипт **не перезаписывает** — правьте вручную.
3. Сверить `db.dbml` и `data/entities.md` с миграциями Flyway.
4. При изменении UI — обновить `roles/*.md`; записку не трогать, дописать замечание в `zamechaniya-k-poyasnitelnoj-zapiske.md`.

## ERD-диаграмма

Файл [db.dbml](db.dbml) импортируется на [dbdiagram.io](https://dbdiagram.io). Экспорт PNG в `screenshots/ERD.png` выполняется вручную после изменения схемы.
