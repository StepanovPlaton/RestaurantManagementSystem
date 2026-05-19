# Роль: Менеджер (MANAGER)

Обработка заказов, работа с клиентами, управление меню и блюдами. Desktop web-приложение.

## Возможности

- Просмотр и редактирование заказов, назначение курьера
- Добавление/удаление позиций в заказе, отмена заказа
- CRUD клиентов (кроме удаления — только admin)
- CRUD меню, блюд, ингредиентов, загрузка фото
- Просмотр сотрудников (GET `/employees`)

## Страницы

### Вход

См. [index.md](index.md#общие-экраны). API: `POST /auth/employees/login`.

### Заказы

- **Назначение:** мониторинг и обработка заказов клиентов.
- **Элементы:** таблица заказов; модальное «Редактирование заказа» (клиент, сумма, статус, список блюд; кнопки «Сохранить», «Отменить заказ»).
- **Действия:** изменить статус через историю, назначить курьера, изменить состав, отменить.
- **API:**
  - `GET/POST /orders`, `GET/PUT/PATCH/DELETE /orders/{id}`
  - `GET/POST /orders/{orderId}/status-history`
  - `GET/POST/PATCH/DELETE /orders/{orderId}/items`
  - `GET /employees?role_id=3` (курьеры), `GET /employees?is_working=true`
  - Справочник `GET /order-statuses` — **только Admin**; менеджер берёт `status_name` из `GET /orders/{id}` и истории статусов
  - — [orders.md](../api/orders.md), [employees-and-roles.md](../api/employees-and-roles.md)
- **Макет:** [fig-22](../пояснительная-записка/assets/fig-22-prototip-stranitsy-upravleniya-zakazami-menedzher.jpg)

### Меню, Блюда, Ингредиенты

Те же экраны, что у администратора (без раздела «Сотрудники»). См. [admin.md](admin.md).

### Настройки, справка

- **Настройки:** `/staff/settings` — см. [admin.md](admin.md).
- **Справка:** `/staff/help`; **О разработчиках:** `/staff/about` — см. [admin.md](admin.md#справка-и-о-разработчиках).

## Навигация

Боковое меню: группа «Ресторан» → «Заказы»; «Настройки», «Справка» — [fig-22](../пояснительная-записка/assets/fig-22-prototip-stranitsy-upravleniya-zakazami-menedzher.jpg).
