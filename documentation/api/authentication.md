# Авторизация

Базовый URL: `http://localhost:8080`

Полная спецификация: [swagger.yaml](../swagger.yaml).
Матрица прав: [errors-and-auth.md](errors-and-auth.md) — при расхождении с OpenAPI доверяйте SecurityConfig.

---

### `POST /auth/clients/login`

**Вход клиента**

Доступ: Публичный

- **Авторизация (OpenAPI):** Публичный (без авторизации)
- **Доступ по ролям (SecurityConfig):** Публичный

**Параметры:**

Нет.

**Тело запроса (пример):**

```json
{
  "login": "client1",
  "password": "password123"
}
```

**Ответ 200 (пример):**

```json
{
  "access_token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...",
  "refresh_token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...",
  "token_type": "Bearer",
  "expires_in": 3600
}
```

**Ответ 401 (пример):**

```json
{
  "error": "Unauthorized",
  "exception": "Unauthorized",
  "message": "Неверный логин или пароль",
  "timestamp": "2024-01-15T10:30:00Z"
}
```

**Ответ 422 (пример):**

```json
{
  "error": "Validation Error",
  "message": "Invalid input data",
  "fields": {
    "login": [
      "Длина логина должна быть от 4 до 16 символов"
    ],
    "password": [
      "Пароль обязателен"
    ]
  }
}
```

**Ответ 500 (пример):**

```json
{
  "error": "Not Found",
  "exception": "Resource not found",
  "message": "Dish not found: id=999",
  "timestamp": "2024-01-15T10:30:00Z"
}
```

---

### `POST /auth/clients/refresh`

**Обновление access токена клиента**

Доступ: Публичный

- **Авторизация (OpenAPI):** Публичный (без авторизации)
- **Доступ по ролям (SecurityConfig):** Публичный

**Параметры:**

Нет.

**Тело запроса (пример):**

```json
{
  "refresh_token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9..."
}
```

**Ответ 200 (пример):**

```json
{
  "access_token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...",
  "refresh_token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...",
  "token_type": "Bearer",
  "expires_in": 3600
}
```

**Ответ 401 (пример):**

```json
{
  "error": "Unauthorized",
  "exception": "Unauthorized",
  "message": "Неверный логин или пароль",
  "timestamp": "2024-01-15T10:30:00Z"
}
```

**Ответ 422 (пример):**

```json
{
  "error": "Validation Error",
  "message": "Invalid input data",
  "fields": {
    "login": [
      "Длина логина должна быть от 4 до 16 символов"
    ],
    "password": [
      "Пароль обязателен"
    ]
  }
}
```

**Ответ 500 (пример):**

```json
{
  "error": "Not Found",
  "exception": "Resource not found",
  "message": "Dish not found: id=999",
  "timestamp": "2024-01-15T10:30:00Z"
}
```

---

### `POST /auth/clients/register`

**Регистрация нового клиента**

Доступ: Публичный

- **Авторизация (OpenAPI):** Публичный (без авторизации)
- **Доступ по ролям (SecurityConfig):** Публичный

**Параметры:**

Нет.

**Тело запроса (пример):**

```json
{
  "first_name": "Иван",
  "last_name": "Иванов",
  "middle_name": "Петрович",
  "login": "client1",
  "password": "password123",
  "email": "ivan@example.com",
  "phone": "+79001234567"
}
```

**Ответ 201 (пример):**

```json
{
  "access_token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...",
  "refresh_token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...",
  "token_type": "Bearer",
  "expires_in": 3600
}
```

**Ответ 400 (пример):**

```json
{
  "error": "Not Found",
  "exception": "Resource not found",
  "message": "Dish not found: id=999",
  "timestamp": "2024-01-15T10:30:00Z"
}
```

**Ответ 422 (пример):**

```json
{
  "error": "Validation Error",
  "message": "Invalid input data",
  "fields": {
    "login": [
      "Длина логина должна быть от 4 до 16 символов"
    ],
    "password": [
      "Пароль обязателен"
    ]
  }
}
```

**Ответ 500 (пример):**

```json
{
  "error": "Not Found",
  "exception": "Resource not found",
  "message": "Dish not found: id=999",
  "timestamp": "2024-01-15T10:30:00Z"
}
```

---

### `POST /auth/employees/login`

**Вход сотрудника**

Доступ: Публичный

- **Авторизация (OpenAPI):** Публичный (без авторизации)
- **Доступ по ролям (SecurityConfig):** Публичный

**Параметры:**

Нет.

**Тело запроса (пример):**

```json
{
  "login": "manager1",
  "password": "password123"
}
```

**Ответ 200 (пример):**

```json
{
  "access_token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...",
  "refresh_token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...",
  "token_type": "Bearer",
  "expires_in": 3600
}
```

**Ответ 401 (пример):**

```json
{
  "error": "Unauthorized",
  "exception": "Unauthorized",
  "message": "Неверный логин или пароль",
  "timestamp": "2024-01-15T10:30:00Z"
}
```

**Ответ 422 (пример):**

```json
{
  "error": "Validation Error",
  "message": "Invalid input data",
  "fields": {
    "login": [
      "Длина логина должна быть от 4 до 16 символов"
    ],
    "password": [
      "Пароль обязателен"
    ]
  }
}
```

**Ответ 500 (пример):**

```json
{
  "error": "Not Found",
  "exception": "Resource not found",
  "message": "Dish not found: id=999",
  "timestamp": "2024-01-15T10:30:00Z"
}
```

---

### `POST /auth/employees/refresh`

**Обновление access токена сотрудника**

Доступ: Публичный

- **Авторизация (OpenAPI):** Публичный (без авторизации)
- **Доступ по ролям (SecurityConfig):** Публичный

**Параметры:**

Нет.

**Тело запроса (пример):**

```json
{
  "refresh_token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9..."
}
```

**Ответ 200 (пример):**

```json
{
  "access_token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...",
  "refresh_token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...",
  "token_type": "Bearer",
  "expires_in": 3600
}
```

**Ответ 401 (пример):**

```json
{
  "error": "Unauthorized",
  "exception": "Unauthorized",
  "message": "Неверный логин или пароль",
  "timestamp": "2024-01-15T10:30:00Z"
}
```

**Ответ 422 (пример):**

```json
{
  "error": "Validation Error",
  "message": "Invalid input data",
  "fields": {
    "login": [
      "Длина логина должна быть от 4 до 16 символов"
    ],
    "password": [
      "Пароль обязателен"
    ]
  }
}
```

**Ответ 500 (пример):**

```json
{
  "error": "Not Found",
  "exception": "Resource not found",
  "message": "Dish not found: id=999",
  "timestamp": "2024-01-15T10:30:00Z"
}
```

---
