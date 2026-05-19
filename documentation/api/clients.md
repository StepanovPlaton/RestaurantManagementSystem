# Клиенты и адреса

Базовый URL: `http://localhost:8080`

Полная спецификация: [swagger.yaml](../swagger.yaml).
Матрица прав: [errors-and-auth.md](errors-and-auth.md) — при расхождении с OpenAPI доверяйте SecurityConfig.

---

### `GET /clients`

**Получить список клиентов**

Доступ: Admin, Manager

- **Авторизация (OpenAPI):** JWT сотрудника
- **Доступ по ролям (SecurityConfig):** Admin, Manager, Client (свой профиль)

**Параметры:**

Нет.

**Ответ 200 (пример):**

```json
{
  "data": [
    {
      "id": 1,
      "first_name": "Иван",
      "last_name": "Иванов",
      "middle_name": "Петрович",
      "login": "client1",
      "email": "ivan@example.com",
      "phone": "+79001234567",
      "avatar_id": 1
    }
  ],
  "total": 50
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

**Ответ 403 (пример):**

```json
{
  "error": "Forbidden",
  "exception": "Forbidden",
  "message": "Недостаточно прав для выполнения операции",
  "timestamp": "2024-01-15T10:30:00Z"
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

### `POST /clients`

**Создать клиента**

Доступ: Admin, Manager

- **Авторизация (OpenAPI):** JWT сотрудника
- **Доступ по ролям (SecurityConfig):** Admin, Manager

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
  "phone": "+79001234567",
  "avatar_id": 1
}
```

**Ответ 201 (пример):**

```json
{
  "id": 1,
  "first_name": "Иван",
  "last_name": "Иванов",
  "middle_name": "Петрович",
  "login": "client1",
  "email": "ivan@example.com",
  "phone": "+79001234567",
  "avatar_id": 1
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

**Ответ 401 (пример):**

```json
{
  "error": "Unauthorized",
  "exception": "Unauthorized",
  "message": "Неверный логин или пароль",
  "timestamp": "2024-01-15T10:30:00Z"
}
```

**Ответ 403 (пример):**

```json
{
  "error": "Forbidden",
  "exception": "Forbidden",
  "message": "Недостаточно прав для выполнения операции",
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

### `GET /clients/{clientId}/addresses`

**Получить адреса клиента**

Доступ: Admin, Manager, Client (только свои)

- **Авторизация (OpenAPI):** JWT сотрудника; JWT клиента
- **Доступ по ролям (SecurityConfig):** Admin, Manager, Client (свой профиль)

**Параметры:**

| Имя | In | Тип | Обязательный | Описание |
|-----|-----|-----|--------------|----------|
| `clientId` | path | integer | да |  |

**Ответ 200 (пример):**

```json
{
  "data": [
    {
      "id": 1,
      "client_id": 1,
      "address_text": "г. Москва, ул. Ленина, д. 10, кв. 5"
    }
  ],
  "total": 5
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

**Ответ 403 (пример):**

```json
{
  "error": "Forbidden",
  "exception": "Forbidden",
  "message": "Недостаточно прав для выполнения операции",
  "timestamp": "2024-01-15T10:30:00Z"
}
```

**Ответ 404 (пример):**

```json
{
  "error": "Not Found",
  "exception": "Resource not found",
  "message": "Resource not found: id=999",
  "timestamp": "2024-01-15T10:30:00Z"
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

### `POST /clients/{clientId}/addresses`

**Создать адрес клиента**

Доступ: Admin, Manager, Client (для себя)

- **Авторизация (OpenAPI):** JWT сотрудника; JWT клиента
- **Доступ по ролям (SecurityConfig):** Admin, Manager

**Параметры:**

| Имя | In | Тип | Обязательный | Описание |
|-----|-----|-----|--------------|----------|
| `clientId` | path | integer | да |  |

**Тело запроса (пример):**

```json
{
  "address_text": "г. Москва, ул. Ленина, д. 10, кв. 5"
}
```

**Ответ 201 (пример):**

```json
{
  "id": 1,
  "client_id": 1,
  "address_text": "г. Москва, ул. Ленина, д. 10, кв. 5"
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

**Ответ 403 (пример):**

```json
{
  "error": "Forbidden",
  "exception": "Forbidden",
  "message": "Недостаточно прав для выполнения операции",
  "timestamp": "2024-01-15T10:30:00Z"
}
```

**Ответ 404 (пример):**

```json
{
  "error": "Not Found",
  "exception": "Resource not found",
  "message": "Resource not found: id=999",
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

### `GET /clients/{clientId}/addresses/{id}`

**Получить адрес по ID**

Доступ: Admin, Manager, Client (только свои)

- **Авторизация (OpenAPI):** JWT сотрудника; JWT клиента
- **Доступ по ролям (SecurityConfig):** Admin, Manager, Client (свой профиль)

**Параметры:**

| Имя | In | Тип | Обязательный | Описание |
|-----|-----|-----|--------------|----------|
| `clientId` | path | integer | да |  |
| `id` | path | integer | да |  |

**Ответ 200 (пример):**

```json
{
  "id": 1,
  "client_id": 1,
  "address_text": "г. Москва, ул. Ленина, д. 10, кв. 5"
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

**Ответ 403 (пример):**

```json
{
  "error": "Forbidden",
  "exception": "Forbidden",
  "message": "Недостаточно прав для выполнения операции",
  "timestamp": "2024-01-15T10:30:00Z"
}
```

**Ответ 404 (пример):**

```json
{
  "error": "Not Found",
  "exception": "Resource not found",
  "message": "Resource not found: id=999",
  "timestamp": "2024-01-15T10:30:00Z"
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

### `PUT /clients/{clientId}/addresses/{id}`

**Полное обновление адреса**

Доступ: Admin, Manager, Client (для своих)

- **Авторизация (OpenAPI):** JWT сотрудника; JWT клиента
- **Доступ по ролям (SecurityConfig):** Admin, Manager, Client (свой профиль)

**Параметры:**

| Имя | In | Тип | Обязательный | Описание |
|-----|-----|-----|--------------|----------|
| `clientId` | path | integer | да |  |
| `id` | path | integer | да |  |

**Тело запроса (пример):**

```json
{
  "address_text": "г. Москва, ул. Ленина, д. 10, кв. 5"
}
```

**Ответ 200 (пример):**

```json
{
  "id": 1,
  "client_id": 1,
  "address_text": "г. Москва, ул. Ленина, д. 10, кв. 5"
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

**Ответ 403 (пример):**

```json
{
  "error": "Forbidden",
  "exception": "Forbidden",
  "message": "Недостаточно прав для выполнения операции",
  "timestamp": "2024-01-15T10:30:00Z"
}
```

**Ответ 404 (пример):**

```json
{
  "error": "Not Found",
  "exception": "Resource not found",
  "message": "Resource not found: id=999",
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

### `PATCH /clients/{clientId}/addresses/{id}`

**Частичное обновление адреса**

Доступ: Admin, Manager, Client (для своих)

- **Авторизация (OpenAPI):** JWT сотрудника; JWT клиента
- **Доступ по ролям (SecurityConfig):** Admin, Manager, Client (свой профиль)

**Параметры:**

| Имя | In | Тип | Обязательный | Описание |
|-----|-----|-----|--------------|----------|
| `clientId` | path | integer | да |  |
| `id` | path | integer | да |  |

**Тело запроса (пример):**

```json
{
  "address_text": "г. Москва, ул. Ленина, д. 10, кв. 5"
}
```

**Ответ 200 (пример):**

```json
{
  "id": 1,
  "client_id": 1,
  "address_text": "г. Москва, ул. Ленина, д. 10, кв. 5"
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

**Ответ 403 (пример):**

```json
{
  "error": "Forbidden",
  "exception": "Forbidden",
  "message": "Недостаточно прав для выполнения операции",
  "timestamp": "2024-01-15T10:30:00Z"
}
```

**Ответ 404 (пример):**

```json
{
  "error": "Not Found",
  "exception": "Resource not found",
  "message": "Resource not found: id=999",
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

### `DELETE /clients/{clientId}/addresses/{id}`

**Удалить адрес**

Доступ: Admin, Manager, Client (для своих)

- **Авторизация (OpenAPI):** JWT сотрудника; JWT клиента
- **Доступ по ролям (SecurityConfig):** Admin

**Параметры:**

| Имя | In | Тип | Обязательный | Описание |
|-----|-----|-----|--------------|----------|
| `clientId` | path | integer | да |  |
| `id` | path | integer | да |  |

**Ответ 204:** Адрес удален

**Ответ 401 (пример):**

```json
{
  "error": "Unauthorized",
  "exception": "Unauthorized",
  "message": "Неверный логин или пароль",
  "timestamp": "2024-01-15T10:30:00Z"
}
```

**Ответ 403 (пример):**

```json
{
  "error": "Forbidden",
  "exception": "Forbidden",
  "message": "Недостаточно прав для выполнения операции",
  "timestamp": "2024-01-15T10:30:00Z"
}
```

**Ответ 404 (пример):**

```json
{
  "error": "Not Found",
  "exception": "Resource not found",
  "message": "Resource not found: id=999",
  "timestamp": "2024-01-15T10:30:00Z"
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

### `GET /clients/{id}`

**Получить клиента по ID**

Доступ: Admin, Manager (любой), Client (только себя)

- **Авторизация (OpenAPI):** JWT сотрудника; JWT клиента
- **Доступ по ролям (SecurityConfig):** Admin, Manager, Client (свой профиль)

**Параметры:**

| Имя | In | Тип | Обязательный | Описание |
|-----|-----|-----|--------------|----------|
| `id` | path | integer | да |  |

**Ответ 200 (пример):**

```json
{
  "id": 1,
  "first_name": "Иван",
  "last_name": "Иванов",
  "middle_name": "Петрович",
  "login": "client1",
  "email": "ivan@example.com",
  "phone": "+79001234567",
  "avatar_id": 1
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

**Ответ 403 (пример):**

```json
{
  "error": "Forbidden",
  "exception": "Forbidden",
  "message": "Недостаточно прав для выполнения операции",
  "timestamp": "2024-01-15T10:30:00Z"
}
```

**Ответ 404 (пример):**

```json
{
  "error": "Not Found",
  "exception": "Resource not found",
  "message": "Resource not found: id=999",
  "timestamp": "2024-01-15T10:30:00Z"
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

### `PUT /clients/{id}`

**Полное обновление клиента**

Доступ: Admin, Manager

- **Авторизация (OpenAPI):** JWT сотрудника
- **Доступ по ролям (SecurityConfig):** Admin, Manager, Client (свой профиль)

**Параметры:**

| Имя | In | Тип | Обязательный | Описание |
|-----|-----|-----|--------------|----------|
| `id` | path | integer | да |  |

**Тело запроса (пример):**

```json
{
  "first_name": "Иван",
  "last_name": "Иванов",
  "middle_name": "Петрович",
  "login": "client1",
  "password": "newpassword123",
  "email": "ivan@example.com",
  "phone": "+79001234567",
  "avatar_id": 1
}
```

**Ответ 200 (пример):**

```json
{
  "id": 1,
  "first_name": "Иван",
  "last_name": "Иванов",
  "middle_name": "Петрович",
  "login": "client1",
  "email": "ivan@example.com",
  "phone": "+79001234567",
  "avatar_id": 1
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

**Ответ 403 (пример):**

```json
{
  "error": "Forbidden",
  "exception": "Forbidden",
  "message": "Недостаточно прав для выполнения операции",
  "timestamp": "2024-01-15T10:30:00Z"
}
```

**Ответ 404 (пример):**

```json
{
  "error": "Not Found",
  "exception": "Resource not found",
  "message": "Resource not found: id=999",
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

### `PATCH /clients/{id}`

**Частичное обновление клиента**

Доступ: Admin, Manager, Client (для себя)

- **Авторизация (OpenAPI):** JWT сотрудника; JWT клиента
- **Доступ по ролям (SecurityConfig):** Admin, Manager, Client (свой профиль)

**Параметры:**

| Имя | In | Тип | Обязательный | Описание |
|-----|-----|-----|--------------|----------|
| `id` | path | integer | да |  |

**Тело запроса (пример):**

```json
{
  "first_name": "Иван",
  "last_name": "Иванов",
  "middle_name": "Петрович",
  "login": "client1",
  "password": "newpassword123",
  "email": "ivan@example.com",
  "phone": "+79001234567",
  "avatar_id": 1
}
```

**Ответ 200 (пример):**

```json
{
  "id": 1,
  "first_name": "Иван",
  "last_name": "Иванов",
  "middle_name": "Петрович",
  "login": "client1",
  "email": "ivan@example.com",
  "phone": "+79001234567",
  "avatar_id": 1
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

**Ответ 403 (пример):**

```json
{
  "error": "Forbidden",
  "exception": "Forbidden",
  "message": "Недостаточно прав для выполнения операции",
  "timestamp": "2024-01-15T10:30:00Z"
}
```

**Ответ 404 (пример):**

```json
{
  "error": "Not Found",
  "exception": "Resource not found",
  "message": "Resource not found: id=999",
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

### `DELETE /clients/{id}`

**Удалить клиента**

Доступ: Admin

- **Авторизация (OpenAPI):** JWT сотрудника
- **Доступ по ролям (SecurityConfig):** Admin

**Параметры:**

| Имя | In | Тип | Обязательный | Описание |
|-----|-----|-----|--------------|----------|
| `id` | path | integer | да |  |

**Ответ 204:** Клиент удален

**Ответ 401 (пример):**

```json
{
  "error": "Unauthorized",
  "exception": "Unauthorized",
  "message": "Неверный логин или пароль",
  "timestamp": "2024-01-15T10:30:00Z"
}
```

**Ответ 403 (пример):**

```json
{
  "error": "Forbidden",
  "exception": "Forbidden",
  "message": "Недостаточно прав для выполнения операции",
  "timestamp": "2024-01-15T10:30:00Z"
}
```

**Ответ 404 (пример):**

```json
{
  "error": "Not Found",
  "exception": "Resource not found",
  "message": "Resource not found: id=999",
  "timestamp": "2024-01-15T10:30:00Z"
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
