# Справочник API

REST API системы управления рестораном. JSON в формате **snake_case**.

Колонка **Роли** отражает `SecurityConfig` backend, а не только поле `security` в OpenAPI.

## Быстрые ссылки

- [Авторизация](authentication.md)
- [Роли и сотрудники](employees-and-roles.md)
- [Клиенты](clients.md)
- [Блюда и меню](dishes-and-menus.md)
- [Заказы](orders.md)
- [Ошибки и JWT](errors-and-auth.md)
- [OpenAPI (YAML)](../swagger.yaml)

## Query-параметры (часто используемые)

| Endpoint | Параметр | Назначение |
|----------|----------|------------|
| `GET /employees` | `role_id` | Фильтр по роли (1=ADMIN, 2=MANAGER, 3=COURIER) |
| `GET /employees` | `is_working` | Курьеры/сотрудники на смене |
| `GET /orders` | `client_id` | Заказы клиента |
| `GET /orders` | `courier_id` | Заказы курьера |
| `GET /menus` | `is_active` | Только активные меню (для витрины клиента) |

## Все операции

| Метод | URL | Роли | Описание | Детали |
|-------|-----|------|----------|--------|
| `POST` | `/auth/clients/login` | Публичный | Вход клиента | [authentication.md](authentication.md) |
| `POST` | `/auth/clients/refresh` | Публичный | Обновление access токена клиента | [authentication.md](authentication.md) |
| `POST` | `/auth/clients/register` | Публичный | Регистрация нового клиента | [authentication.md](authentication.md) |
| `POST` | `/auth/employees/login` | Публичный | Вход сотрудника | [authentication.md](authentication.md) |
| `POST` | `/auth/employees/refresh` | Публичный | Обновление access токена сотрудника | [authentication.md](authentication.md) |
| `POST` | `/avatars` | Admin, Manager | Загрузить аватар | [employees-and-roles.md](employees-and-roles.md) |
| `GET` | `/avatars/{id}` | Любой аутентифицированный (GET); Admin, Manager (загрузка/удаление) | Получить метаданные аватара | [employees-and-roles.md](employees-and-roles.md) |
| `DELETE` | `/avatars/{id}` | Admin, Manager | Удалить аватар | [employees-and-roles.md](employees-and-roles.md) |
| `GET` | `/clients` | Admin, Manager, Client (свой профиль) | Получить список клиентов | [clients.md](clients.md) |
| `POST` | `/clients` | Admin, Manager | Создать клиента | [clients.md](clients.md) |
| `GET` | `/clients/{clientId}/addresses` | Admin, Manager, Client (свой профиль) | Получить адреса клиента | [clients.md](clients.md) |
| `POST` | `/clients/{clientId}/addresses` | Admin, Manager | Создать адрес клиента | [clients.md](clients.md) |
| `GET` | `/clients/{clientId}/addresses/{id}` | Admin, Manager, Client (свой профиль) | Получить адрес по ID | [clients.md](clients.md) |
| `PUT` | `/clients/{clientId}/addresses/{id}` | Admin, Manager, Client (свой профиль) | Полное обновление адреса | [clients.md](clients.md) |
| `PATCH` | `/clients/{clientId}/addresses/{id}` | Admin, Manager, Client (свой профиль) | Частичное обновление адреса | [clients.md](clients.md) |
| `DELETE` | `/clients/{clientId}/addresses/{id}` | Admin | Удалить адрес | [clients.md](clients.md) |
| `GET` | `/clients/{id}` | Admin, Manager, Client (свой профиль) | Получить клиента по ID | [clients.md](clients.md) |
| `PUT` | `/clients/{id}` | Admin, Manager, Client (свой профиль) | Полное обновление клиента | [clients.md](clients.md) |
| `PATCH` | `/clients/{id}` | Admin, Manager, Client (свой профиль) | Частичное обновление клиента | [clients.md](clients.md) |
| `DELETE` | `/clients/{id}` | Admin | Удалить клиента | [clients.md](clients.md) |
| `GET` | `/dishes` | Admin, Manager, Client, Courier (GET); Admin, Manager (изменение) | Получить список блюд | [dishes-and-menus.md](dishes-and-menus.md) |
| `POST` | `/dishes` | Admin, Manager | Создать блюдо | [dishes-and-menus.md](dishes-and-menus.md) |
| `GET` | `/dishes/{dishId}/ingredients` | Admin, Manager, Client, Courier (GET); Admin, Manager (изменение) | Получить ингредиенты блюда | [dishes-and-menus.md](dishes-and-menus.md) |
| `POST` | `/dishes/{dishId}/ingredients` | Admin, Manager | Добавить ингредиент к блюду | [dishes-and-menus.md](dishes-and-menus.md) |
| `DELETE` | `/dishes/{dishId}/ingredients/{ingredientId}` | Admin, Manager | Удалить ингредиент из блюда | [dishes-and-menus.md](dishes-and-menus.md) |
| `GET` | `/dishes/{dishId}/photos` | Admin, Manager, Client, Courier (GET); Admin, Manager (изменение) | Получить фотографии блюда | [dishes-and-menus.md](dishes-and-menus.md) |
| `POST` | `/dishes/{dishId}/photos` | Admin, Manager | Привязать фото к блюду | [dishes-and-menus.md](dishes-and-menus.md) |
| `DELETE` | `/dishes/{dishId}/photos/{photoId}` | Admin, Manager | Отвязать фото от блюда | [dishes-and-menus.md](dishes-and-menus.md) |
| `GET` | `/dishes/{id}` | Admin, Manager, Client, Courier (GET); Admin, Manager (изменение) | Получить блюдо по ID | [dishes-and-menus.md](dishes-and-menus.md) |
| `PUT` | `/dishes/{id}` | Admin, Manager | Полное обновление блюда | [dishes-and-menus.md](dishes-and-menus.md) |
| `PATCH` | `/dishes/{id}` | Admin, Manager | Частичное обновление блюда | [dishes-and-menus.md](dishes-and-menus.md) |
| `DELETE` | `/dishes/{id}` | Admin, Manager | Удалить блюдо | [dishes-and-menus.md](dishes-and-menus.md) |
| `GET` | `/employees` | Admin, Manager | Получить список сотрудников | [employees-and-roles.md](employees-and-roles.md) |
| `POST` | `/employees` | Admin | Создать сотрудника | [employees-and-roles.md](employees-and-roles.md) |
| `GET` | `/employees/{id}` | Admin, Manager | Получить сотрудника по ID | [employees-and-roles.md](employees-and-roles.md) |
| `PUT` | `/employees/{id}` | Admin | Полное обновление сотрудника | [employees-and-roles.md](employees-and-roles.md) |
| `PATCH` | `/employees/{id}` | Admin | Частичное обновление сотрудника | [employees-and-roles.md](employees-and-roles.md) |
| `DELETE` | `/employees/{id}` | Admin | Удалить сотрудника | [employees-and-roles.md](employees-and-roles.md) |
| `GET` | `/ingredients` | Admin, Manager, Client, Courier (GET); Admin, Manager (изменение) | Получить список ингредиентов | [dishes-and-menus.md](dishes-and-menus.md) |
| `POST` | `/ingredients` | Admin, Manager | Создать ингредиент | [dishes-and-menus.md](dishes-and-menus.md) |
| `GET` | `/ingredients/{id}` | Admin, Manager, Client, Courier (GET); Admin, Manager (изменение) | Получить ингредиент по ID | [dishes-and-menus.md](dishes-and-menus.md) |
| `PUT` | `/ingredients/{id}` | Admin, Manager | Полное обновление ингредиента | [dishes-and-menus.md](dishes-and-menus.md) |
| `PATCH` | `/ingredients/{id}` | Admin, Manager | Частичное обновление ингредиента | [dishes-and-menus.md](dishes-and-menus.md) |
| `DELETE` | `/ingredients/{id}` | Admin, Manager | Удалить ингредиент | [dishes-and-menus.md](dishes-and-menus.md) |
| `GET` | `/menus` | Admin, Manager, Client, Courier (GET); Admin, Manager (изменение) | Получить список меню | [dishes-and-menus.md](dishes-and-menus.md) |
| `POST` | `/menus` | Admin, Manager | Создать меню | [dishes-and-menus.md](dishes-and-menus.md) |
| `GET` | `/menus/{id}` | Admin, Manager, Client, Courier (GET); Admin, Manager (изменение) | Получить меню по ID | [dishes-and-menus.md](dishes-and-menus.md) |
| `PUT` | `/menus/{id}` | Admin, Manager | Полное обновление меню | [dishes-and-menus.md](dishes-and-menus.md) |
| `PATCH` | `/menus/{id}` | Admin, Manager | Частичное обновление меню | [dishes-and-menus.md](dishes-and-menus.md) |
| `DELETE` | `/menus/{id}` | Admin, Manager | Удалить меню | [dishes-and-menus.md](dishes-and-menus.md) |
| `GET` | `/menus/{menuId}/dishes` | Admin, Manager, Client, Courier (GET); Admin, Manager (изменение) | Получить блюда в меню | [dishes-and-menus.md](dishes-and-menus.md) |
| `POST` | `/menus/{menuId}/dishes` | Admin, Manager | Добавить блюдо в меню | [dishes-and-menus.md](dishes-and-menus.md) |
| `DELETE` | `/menus/{menuId}/dishes/{dishId}` | Admin, Manager | Удалить блюдо из меню | [dishes-and-menus.md](dishes-and-menus.md) |
| `GET` | `/order-statuses` | Admin | Получить список статусов заказов | [orders.md](orders.md) |
| `GET` | `/order-statuses/{id}` | Admin | Получить статус по ID | [orders.md](orders.md) |
| `GET` | `/orders` | Admin, Manager, Courier, Client | Получить список заказов | [orders.md](orders.md) |
| `POST` | `/orders` | Admin, Manager, Client | Создать заказ | [orders.md](orders.md) |
| `GET` | `/orders/{id}` | Admin, Manager, Courier, Client | Получить заказ по ID | [orders.md](orders.md) |
| `PUT` | `/orders/{id}` | Admin, Manager | Полное обновление заказа | [orders.md](orders.md) |
| `PATCH` | `/orders/{id}` | Admin, Manager, Courier, Client | Частичное обновление заказа | [orders.md](orders.md) |
| `DELETE` | `/orders/{id}` | Admin | Удалить заказ | [orders.md](orders.md) |
| `GET` | `/orders/{orderId}/items` | Admin, Manager, Courier, Client | Получить позиции заказа | [orders.md](orders.md) |
| `POST` | `/orders/{orderId}/items` | Admin, Manager, Client | Добавить позицию в заказ | [orders.md](orders.md) |
| `GET` | `/orders/{orderId}/items/{id}` | Admin, Manager, Courier, Client | Получить позицию заказа по ID | [orders.md](orders.md) |
| `PUT` | `/orders/{orderId}/items/{id}` | Admin, Manager | Полное обновление позиции | [orders.md](orders.md) |
| `PATCH` | `/orders/{orderId}/items/{id}` | Admin, Manager, Courier, Client | Частичное обновление позиции | [orders.md](orders.md) |
| `DELETE` | `/orders/{orderId}/items/{id}` | Admin | Удалить позицию из заказа | [orders.md](orders.md) |
| `GET` | `/orders/{orderId}/status-history` | Admin, Manager, Courier, Client | Получить историю статусов заказа | [orders.md](orders.md) |
| `POST` | `/orders/{orderId}/status-history` | Admin, Manager, Client | Изменить статус заказа | [orders.md](orders.md) |
| `POST` | `/photos` | Admin, Manager | Загрузить фото | [dishes-and-menus.md](dishes-and-menus.md) |
| `GET` | `/photos/{id}` | Любой аутентифицированный (GET); Admin, Manager (загрузка/удаление) | Получить метаданные фото | [dishes-and-menus.md](dishes-and-menus.md) |
| `DELETE` | `/photos/{id}` | Admin, Manager | Удалить фото | [dishes-and-menus.md](dishes-and-menus.md) |
| `GET` | `/roles` | Аутентифицированный | Получить список ролей | [employees-and-roles.md](employees-and-roles.md) |
| `GET` | `/roles/{id}` | Admin | Получить роль по ID | [employees-and-roles.md](employees-and-roles.md) |