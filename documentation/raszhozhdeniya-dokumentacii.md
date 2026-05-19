# Расхождения актуальной документации с действительностью

Журнал несоответствий между **технической** документацией ([README.md](README.md): `product/`, `roles/`, `data/`, `api/`, `swagger.yaml`, `db.dbml`) и фактическим состоянием системы (код, OpenAPI, миграции, UI).

Пояснительная записка — отдельно: [zamechaniya-k-poyasnitelnoj-zapiske.md](zamechaniya-k-poyasnitelnoj-zapiske.md).

Формат записи — см. правило `.cursor/rules/documentation-first.mdc`.

---

## 1. ListResponse: поле `items` в ROADMAP vs `data` в API

- **Документ:** [frontend/ROADMAP.md](../frontend/ROADMAP.md) (фаза 0, задача types.ts)
- **Сейчас в документации:** упоминание поля `items` в `ListResponse<T>`
- **Факт:** backend `ListResponse` record и OpenAPI `RolesList` используют `data` и `total` ([ListResponse.java](../backend/src/main/java/ru/karpin/restaurant/common/dto/ListResponse.java))
- **Исправить в документации:** в ROADMAP и примерах frontend указать `{ data: T[]; total: number }`

---

## 2. Email в форме менеджера (макет) vs API сотрудника

- **Документ:** [roles/admin.md](roles/admin.md) (раздел «Менеджеры»), макет [fig-21](пояснительная-записка/assets/fig-21-prototip-stranitsy-upravleniya-menedzherami.jpg)
- **Сейчас в документации:** поле email в анкете менеджера
- **Факт:** `EmployeeResponse` / `EmployeeCreate` — только `login`, `phone`, ФИО; email хранится у `User`, но не отдаётся в API сотрудников
- **Исправить в документации:** убрать email из описания формы менеджера или добавить поле в backend API

---

## 3. Статус заказа в `GET /orders` и OpenAPI

- **Документ:** [roles/manager.md](roles/manager.md) (§ Заказы), [frontend/ROADMAP.md](../frontend/ROADMAP.md) (фаза 3), [openapi.yaml](../backend/src/main/resources/openapi.yaml) (`Order`)
- **Сейчас в документации:** текущий статус доступен как `status_name` в ответе заказа; в OpenAPI у `Order` есть вложенные `client`, `courier`
- **Факт:** `OrderResponse` содержит только `id`, `client_id`, `address_id`, `manager_id`, `courier_id`, `total_price`, `created_at`; `OrderStatusHistoryResponse` — `status_id` без `status_name` ([OrderResponse.java](../backend/src/main/java/ru/karpin/restaurant/order/dto/OrderResponse.java))
- **Исправить в документации:** UI берёт статус из последней записи `GET /orders/{id}/status-history` и справочника `order_statuses` (каталог по id); убрать упоминание `status_name` в теле заказа; при необходимости расширить backend DTO

---

## 4. API курьера: профиль, смена и данные заказа — закрыто

- **Было:** курьер не мог `GET/PATCH /employees/{id}`; в заказе не было адреса и ФИО клиента.
- **Факт:** `GET/PATCH /employees/me` для ADMIN, MANAGER, COURIER; `OrderResponse` дополнен `address_text`, `client_first_name`, `client_last_name`, `client_middle_name`; список заказов курьера фильтруется на backend. Frontend: `/employees/me`, без dev-заглушек.
- **Документация:** [errors-and-auth.md](api/errors-and-auth.md), [courier.md](roles/courier.md) — при расхождении формулировок обновить там.

---

## 5. Клиент: создание адреса доставки — закрыто

- **Было:** frontend скрывал `POST` из‑за устаревшего описания SecurityConfig.
- **Факт:** `POST /clients/*/addresses` разрешён для CLIENT ([SecurityConfig.java](../backend/src/main/java/ru/karpin/restaurant/common/config/SecurityConfig.java)); UI: «Добавить адрес» в профиле и в корзине.
- **Ограничение:** `DELETE` адресов по-прежнему только ADMIN.

---

## 6. Клиент: загрузка аватара

- **Документ:** [roles/client.md](roles/client.md) (§ Профиль)
- **Сейчас в документации:** `POST /avatars` для профиля клиента
- **Факт:** `POST /avatars` и `DELETE /avatars/**` — только ADMIN, MANAGER; CLIENT — `GET /avatars/{id}` при наличии `avatar_id`
- **Исправить в документации:** убрать загрузку аватара из возможностей CLIENT; указать отображение через `GET` или инициалы
