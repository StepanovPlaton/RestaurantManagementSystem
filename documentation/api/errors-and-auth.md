# Ошибки и авторизация

## JWT

Система использует два независимых контура JWT:

| Схема OpenAPI | Кто использует | Заголовок |
|---------------|----------------|-----------|
| `jwtEmployee` | Admin, Manager, Courier | `Authorization: Bearer <access_token>` |
| `jwtClient` | Client | `Authorization: Bearer <access_token>` |

Получение токенов — см. [authentication.md](authentication.md):

- Сотрудники: `POST /auth/employees/login`, обновление — `POST /auth/employees/refresh`
- Клиенты: `POST /auth/clients/register`, `POST /auth/clients/login`, `POST /auth/clients/refresh`

Параметры JWT в backend (`application.properties`):

- `jwt.expiration` — время жизни access-токена (мс)
- `jwt.refresh-expiration` — время жизни refresh-токена (мс)

## Матрица доступа по ролям (SecurityConfig)

| Ресурс | Admin | Manager | Courier | Client | Примечание |
|--------|:-----:|:-------:|:-------:|:------:|------------|
| `/auth/**` | + | + | + | + | Без токена |
| `/roles/**` | + | | | | Только чтение |
| `/order-statuses/**` | + | | | | Только чтение |
| `/employees` GET (список) | + | + | | | |
| `/employees/me` GET/PATCH | + | + | + | | Свой профиль (курьер/менеджер без `PATCH /employees/{id}`) |
| `/employees` POST/PUT/PATCH/DELETE по `{id}` | + | | | | |
| `/clients` GET | + | + | + | Свой профиль |
| `/clients` POST | + | + | | | |
| `/clients` PUT/PATCH | + | + | + | Свой профиль |
| `/clients` DELETE | + | | | | |
| `/dishes`, `/menus`, `/ingredients` GET | + | + | + | + | Любой аутентифицированный |
| `/dishes`, `/menus`, `/ingredients` изменение | + | + | | | |
| `/photos`, `/avatars` GET | + | + | + | + | Аутентифицированный |
| `/photos`, `/avatars` загрузка/удаление | + | + | | | |
| `/orders` POST | + | + | | + | Создание заказа |
| `/orders` PUT | + | + | | | |
| `/orders` DELETE | + | | | | |
| `/orders/**` остальное | + | + | + | + | Courier/Client видят только свои заказы (фильтр в сервисе); в ответе заказа — `address_text`, ФИО клиента |

Authority в токене сотрудника совпадает с `roles.name` (`ADMIN`, `MANAGER`, `COURIER`).

> **Важно:** в OpenAPI у `/order-statuses` ранее мог быть указан доступ для клиента — фактически endpoint доступен **только Admin**. Менеджер и курьер работают со статусами через заказы и `status-history`.

## Загрузка файлов

| Endpoint | Content-Type | Поле | Кто загружает |
|----------|--------------|------|---------------|
| `POST /photos` | `multipart/form-data` | `file` | Admin, Manager |
| `POST /avatars` | `multipart/form-data` | `file` | Admin, Manager |
| `POST /dishes/{dishId}/photos` | `multipart/form-data` | `file` | Admin, Manager |

Максимальный размер: **10 MB**. Файлы сохраняются в каталог `uploads/` (настраивается `app.upload.dir`).

## Форматы ошибок

### 404 Not Found

```json
{
  "error": "Not Found",
  "message": "Resource not found",
  "details": "Dish not found: id=999"
}
```

### 400 Bad Request (дубликат, целостность данных, файл)

```json
{
  "error": "Bad Request",
  "message": "Resource already exists",
  "details": "Login already taken"
}
```

### 422 Unprocessable Entity (валидация)

```json
{
  "error": "Validation Error",
  "message": "Invalid input data",
  "fields": {
    "login": ["Длина логина должна быть от 4 до 16 символов"],
    "password": ["Пароль обязателен"]
  }
}
```

### 413 Payload Too Large

Превышен лимит загрузки файла (`spring.servlet.multipart.max-file-size`, по умолчанию 10 MB).

### 401 / 403

Стандартные ответы Spring Security при отсутствии или недостаточности прав.

## Swagger UI

При запущенном backend:

- OpenAPI JSON: `http://localhost:8080/api-docs`
- Swagger UI: `http://localhost:8080/swagger-ui.html`
