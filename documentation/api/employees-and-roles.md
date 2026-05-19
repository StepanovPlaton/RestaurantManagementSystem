# Роли, сотрудники, аватары

Базовый URL: `http://localhost:8080`

Полная спецификация: [swagger.yaml](../swagger.yaml).
Матрица прав: [errors-and-auth.md](errors-and-auth.md) — при расхождении с OpenAPI доверяйте SecurityConfig.

---

### `POST /avatars`

**Загрузить аватар**

Доступ: Все авторизованные. Multipart-форма с полем 'file' (jpeg/png/webp, до 10 MB). Возвращает метаданные с URL.

- **Авторизация (OpenAPI):** JWT сотрудника; JWT клиента
- **Доступ по ролям (SecurityConfig):** Admin, Manager

**Параметры:**

Нет.

**Тело запроса:** `Content-Type: multipart/form-data`

| Поле | Тип | Обязательный |
|------|-----|--------------|
| `file` | string | да |

Лимит размера файла: 10 MB (`spring.servlet.multipart.max-file-size`).

**Ответ 201 (пример):**

```json
{
  "id": 1,
  "path": "/uploads/avatars/a3f1c2d4-uuid.jpg"
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

**Ответ 413 (пример):**

```json
{
  "error": "Not Found",
  "exception": "Resource not found",
  "message": "Dish not found: id=999",
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

### `GET /avatars/{id}`

**Получить метаданные аватара**

Доступ: Все авторизованные

- **Авторизация (OpenAPI):** JWT сотрудника; JWT клиента
- **Доступ по ролям (SecurityConfig):** Любой аутентифицированный (GET); Admin, Manager (загрузка/удаление)

**Параметры:**

| Имя | In | Тип | Обязательный | Описание |
|-----|-----|-----|--------------|----------|
| `id` | path | integer | да |  |

**Ответ 200 (пример):**

```json
{
  "id": 1,
  "path": "/uploads/avatars/a3f1c2d4-uuid.jpg"
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

### `DELETE /avatars/{id}`

**Удалить аватар**

Доступ: Admin, Manager. Удаляет файл с диска и запись из БД. Связка с сотрудником/клиентом обнуляется на стороне employee/client (SET NULL).

- **Авторизация (OpenAPI):** JWT сотрудника
- **Доступ по ролям (SecurityConfig):** Admin, Manager

**Параметры:**

| Имя | In | Тип | Обязательный | Описание |
|-----|-----|-----|--------------|----------|
| `id` | path | integer | да |  |

**Ответ 204:** Аватар удалён

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

### `GET /employees`

**Получить список сотрудников**

Доступ: Admin, Manager

- **Авторизация (OpenAPI):** JWT сотрудника
- **Доступ по ролям (SecurityConfig):** Admin, Manager

**Параметры:**

| Имя | In | Тип | Обязательный | Описание |
|-----|-----|-----|--------------|----------|
| `role_id` | query | integer | нет |  |
| `is_working` | query | boolean | нет |  |

**Ответ 200 (пример):**

```json
{
  "data": [
    {
      "id": 1,
      "first_name": "Петр",
      "last_name": "Петров",
      "middle_name": "Иванович",
      "login": "manager1",
      "role_id": 2,
      "role": {
        "id": 1,
        "name": "Admin"
      },
      "phone": "+79001234567",
      "avatar_id": 1,
      "is_working": true
    }
  ],
  "total": 10
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

### `POST /employees`

**Создать сотрудника**

Доступ: Admin

- **Авторизация (OpenAPI):** JWT сотрудника
- **Доступ по ролям (SecurityConfig):** Admin

**Параметры:**

Нет.

**Тело запроса (пример):**

```json
{
  "first_name": "Петр",
  "last_name": "Петров",
  "middle_name": "Иванович",
  "login": "manager1",
  "password": "password123",
  "role_id": 2,
  "phone": "+79001234567",
  "avatar_id": 1,
  "is_working": false
}
```

**Ответ 201 (пример):**

```json
{
  "id": 1,
  "first_name": "Петр",
  "last_name": "Петров",
  "middle_name": "Иванович",
  "login": "manager1",
  "role_id": 2,
  "role": {
    "id": 1,
    "name": "Admin"
  },
  "phone": "+79001234567",
  "avatar_id": 1,
  "is_working": true
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

### `GET /employees/{id}`

**Получить сотрудника по ID**

Доступ: Admin, Manager (любой), Employee (только себя)

- **Авторизация (OpenAPI):** JWT сотрудника
- **Доступ по ролям (SecurityConfig):** Admin, Manager

**Параметры:**

| Имя | In | Тип | Обязательный | Описание |
|-----|-----|-----|--------------|----------|
| `id` | path | integer | да |  |

**Ответ 200 (пример):**

```json
{
  "id": 1,
  "first_name": "Петр",
  "last_name": "Петров",
  "middle_name": "Иванович",
  "login": "manager1",
  "role_id": 2,
  "role": {
    "id": 1,
    "name": "Admin"
  },
  "phone": "+79001234567",
  "avatar_id": 1,
  "is_working": true
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

### `PUT /employees/{id}`

**Полное обновление сотрудника**

Доступ: Admin

- **Авторизация (OpenAPI):** JWT сотрудника
- **Доступ по ролям (SecurityConfig):** Admin

**Параметры:**

| Имя | In | Тип | Обязательный | Описание |
|-----|-----|-----|--------------|----------|
| `id` | path | integer | да |  |

**Тело запроса (пример):**

```json
{
  "first_name": "Петр",
  "last_name": "Петров",
  "middle_name": "Иванович",
  "login": "manager1",
  "password": "newpassword123",
  "role_id": 2,
  "phone": "+79001234567",
  "avatar_id": 1,
  "is_working": true
}
```

**Ответ 200 (пример):**

```json
{
  "id": 1,
  "first_name": "Петр",
  "last_name": "Петров",
  "middle_name": "Иванович",
  "login": "manager1",
  "role_id": 2,
  "role": {
    "id": 1,
    "name": "Admin"
  },
  "phone": "+79001234567",
  "avatar_id": 1,
  "is_working": true
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

### `PATCH /employees/{id}`

**Частичное обновление сотрудника**

Доступ: Admin, Manager (для подчиненных)

- **Авторизация (OpenAPI):** JWT сотрудника
- **Доступ по ролям (SecurityConfig):** Admin

**Параметры:**

| Имя | In | Тип | Обязательный | Описание |
|-----|-----|-----|--------------|----------|
| `id` | path | integer | да |  |

**Тело запроса (пример):**

```json
{
  "first_name": "Петр",
  "last_name": "Петров",
  "middle_name": "Иванович",
  "login": "manager1",
  "password": "newpassword123",
  "role_id": 2,
  "phone": "+79001234567",
  "avatar_id": 1,
  "is_working": true
}
```

**Ответ 200 (пример):**

```json
{
  "id": 1,
  "first_name": "Петр",
  "last_name": "Петров",
  "middle_name": "Иванович",
  "login": "manager1",
  "role_id": 2,
  "role": {
    "id": 1,
    "name": "Admin"
  },
  "phone": "+79001234567",
  "avatar_id": 1,
  "is_working": true
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

### `DELETE /employees/{id}`

**Удалить сотрудника**

Доступ: Admin

- **Авторизация (OpenAPI):** JWT сотрудника
- **Доступ по ролям (SecurityConfig):** Admin

**Параметры:**

| Имя | In | Тип | Обязательный | Описание |
|-----|-----|-----|--------------|----------|
| `id` | path | integer | да |  |

**Ответ 204:** Сотрудник удален

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

### `GET /roles`

**Получить список ролей**

Доступ: Admin

- **Авторизация (OpenAPI):** JWT сотрудника
- **Доступ по ролям (SecurityConfig):** Аутентифицированный

**Параметры:**

Нет.

**Ответ 200 (пример):**

```json
{
  "data": [
    {
      "id": 1,
      "name": "Admin"
    }
  ],
  "total": 3
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

### `GET /roles/{id}`

**Получить роль по ID**

Доступ: Admin

- **Авторизация (OpenAPI):** JWT сотрудника
- **Доступ по ролям (SecurityConfig):** Admin

**Параметры:**

| Имя | In | Тип | Обязательный | Описание |
|-----|-----|-----|--------------|----------|
| `id` | path | integer | да |  |

**Ответ 200 (пример):**

```json
{
  "id": 1,
  "name": "Admin"
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
