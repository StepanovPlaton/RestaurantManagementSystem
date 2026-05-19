# Заказы и статусы

Базовый URL: `http://localhost:8080`

Полная спецификация: [swagger.yaml](../swagger.yaml).
Матрица прав: [errors-and-auth.md](errors-and-auth.md) — при расхождении с OpenAPI доверяйте SecurityConfig.

---

### `GET /order-statuses`

**Получить список статусов заказов**

Доступ: только Admin (authority ADMIN). Справочник заполняется миграциями; менеджер, курьер и клиент используют коды статусов из ответов заказа и истории.

- **Авторизация (OpenAPI):** JWT сотрудника
- **Доступ по ролям (SecurityConfig):** Admin

**Параметры:**

Нет.

**Ответ 200 (пример):**

```json
{
  "data": [
    {
      "id": 1,
      "status_name": "NEW"
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

### `GET /order-statuses/{id}`

**Получить статус по ID**

Доступ: только Admin (authority ADMIN)

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
  "status_name": "NEW"
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

### `GET /orders`

**Получить список заказов**

Доступ: Admin, Manager (все), Courier (назначенные), Client (свои)

- **Авторизация (OpenAPI):** JWT сотрудника; JWT клиента
- **Доступ по ролям (SecurityConfig):** Admin, Manager, Courier, Client

**Параметры:**

| Имя | In | Тип | Обязательный | Описание |
|-----|-----|-----|--------------|----------|
| `client_id` | query | integer | нет |  |
| `courier_id` | query | integer | нет |  |
| `status_id` | query | integer | нет |  |

**Ответ 200 (пример):**

```json
{
  "data": [
    {
      "id": 1,
      "client_id": 1,
      "client": {
        "id": 1,
        "first_name": "Иван",
        "last_name": "Иванов",
        "middle_name": "Петрович",
        "login": "client1",
        "email": "ivan@example.com",
        "phone": "+79001234567",
        "avatar_id": 1
      },
      "address_id": 1,
      "address": {
        "id": 1,
        "client_id": 1,
        "address_text": "г. Москва, ул. Ленина, д. 10, кв. 5"
      },
      "manager_id": 2,
      "manager": {
        "id": 1,
        "first_name": "Петр",
        "last_name": "Петров",
        "middle_name": "Иванович",
        "login": "manager1",
        "role_id": 2,
        "role": {
          "id": {},
          "name": {}
        },
        "phone": "+79001234567",
        "avatar_id": 1,
        "is_working": true
      },
      "courier_id": 3,
      "courier": {
        "id": 1,
        "first_name": "Петр",
        "last_name": "Петров",
        "middle_name": "Иванович",
        "login": "manager1",
        "role_id": 2,
        "role": {
          "id": {},
          "name": {}
        },
        "phone": "+79001234567",
        "avatar_id": 1,
        "is_working": true
      },
      "total_price": 2400.0,
      "created_at": "2024-01-15T10:30:00Z"
    }
  ],
  "total": 100
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

### `POST /orders`

**Создать заказ**

Доступ: Client, Manager

- **Авторизация (OpenAPI):** JWT сотрудника; JWT клиента
- **Доступ по ролям (SecurityConfig):** Admin, Manager, Client

**Параметры:**

Нет.

**Тело запроса (пример):**

```json
{
  "address_id": 1,
  "items": [
    {
      "dish_id": 1,
      "quantity": 2
    }
  ]
}
```

**Ответ 201 (пример):**

```json
{
  "id": 1,
  "client_id": 1,
  "client": {
    "id": 1,
    "first_name": "Иван",
    "last_name": "Иванов",
    "middle_name": "Петрович",
    "login": "client1",
    "email": "ivan@example.com",
    "phone": "+79001234567",
    "avatar_id": 1
  },
  "address_id": 1,
  "address": {
    "id": 1,
    "client_id": 1,
    "address_text": "г. Москва, ул. Ленина, д. 10, кв. 5"
  },
  "manager_id": 2,
  "manager": {
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
  },
  "courier_id": 3,
  "courier": {
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
  },
  "total_price": 2400.0,
  "created_at": "2024-01-15T10:30:00Z"
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

### `GET /orders/{id}`

**Получить заказ по ID**

Доступ: Admin, Manager (любой), Courier (назначенные), Client (свои)

- **Авторизация (OpenAPI):** JWT сотрудника; JWT клиента
- **Доступ по ролям (SecurityConfig):** Admin, Manager, Courier, Client

**Параметры:**

| Имя | In | Тип | Обязательный | Описание |
|-----|-----|-----|--------------|----------|
| `id` | path | integer | да |  |

**Ответ 200 (пример):**

```json
{
  "id": 1,
  "client_id": 1,
  "client": {
    "id": 1,
    "first_name": "Иван",
    "last_name": "Иванов",
    "middle_name": "Петрович",
    "login": "client1",
    "email": "ivan@example.com",
    "phone": "+79001234567",
    "avatar_id": 1
  },
  "address_id": 1,
  "address": {
    "id": 1,
    "client_id": 1,
    "address_text": "г. Москва, ул. Ленина, д. 10, кв. 5"
  },
  "manager_id": 2,
  "manager": {
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
  },
  "courier_id": 3,
  "courier": {
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
  },
  "total_price": 2400.0,
  "created_at": "2024-01-15T10:30:00Z"
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

### `PUT /orders/{id}`

**Полное обновление заказа**

Доступ: Admin, Manager

- **Авторизация (OpenAPI):** JWT сотрудника
- **Доступ по ролям (SecurityConfig):** Admin, Manager

**Параметры:**

| Имя | In | Тип | Обязательный | Описание |
|-----|-----|-----|--------------|----------|
| `id` | path | integer | да |  |

**Тело запроса (пример):**

```json
{
  "address_id": 1,
  "manager_id": 2,
  "courier_id": 3
}
```

**Ответ 200 (пример):**

```json
{
  "id": 1,
  "client_id": 1,
  "client": {
    "id": 1,
    "first_name": "Иван",
    "last_name": "Иванов",
    "middle_name": "Петрович",
    "login": "client1",
    "email": "ivan@example.com",
    "phone": "+79001234567",
    "avatar_id": 1
  },
  "address_id": 1,
  "address": {
    "id": 1,
    "client_id": 1,
    "address_text": "г. Москва, ул. Ленина, д. 10, кв. 5"
  },
  "manager_id": 2,
  "manager": {
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
  },
  "courier_id": 3,
  "courier": {
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
  },
  "total_price": 2400.0,
  "created_at": "2024-01-15T10:30:00Z"
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

### `PATCH /orders/{id}`

**Частичное обновление заказа**

Доступ: Admin, Manager, Courier (для назначенных)

- **Авторизация (OpenAPI):** JWT сотрудника; JWT клиента
- **Доступ по ролям (SecurityConfig):** Admin, Manager, Courier, Client

**Параметры:**

| Имя | In | Тип | Обязательный | Описание |
|-----|-----|-----|--------------|----------|
| `id` | path | integer | да |  |

**Тело запроса (пример):**

```json
{
  "address_id": 1,
  "manager_id": 2,
  "courier_id": 3
}
```

**Ответ 200 (пример):**

```json
{
  "id": 1,
  "client_id": 1,
  "client": {
    "id": 1,
    "first_name": "Иван",
    "last_name": "Иванов",
    "middle_name": "Петрович",
    "login": "client1",
    "email": "ivan@example.com",
    "phone": "+79001234567",
    "avatar_id": 1
  },
  "address_id": 1,
  "address": {
    "id": 1,
    "client_id": 1,
    "address_text": "г. Москва, ул. Ленина, д. 10, кв. 5"
  },
  "manager_id": 2,
  "manager": {
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
  },
  "courier_id": 3,
  "courier": {
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
  },
  "total_price": 2400.0,
  "created_at": "2024-01-15T10:30:00Z"
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

### `DELETE /orders/{id}`

**Удалить заказ**

Доступ: Admin

- **Авторизация (OpenAPI):** JWT сотрудника
- **Доступ по ролям (SecurityConfig):** Admin

**Параметры:**

| Имя | In | Тип | Обязательный | Описание |
|-----|-----|-----|--------------|----------|
| `id` | path | integer | да |  |

**Ответ 204:** Заказ удален

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

### `GET /orders/{orderId}/items`

**Получить позиции заказа**

Доступ: Все авторизованные с доступом к заказу

- **Авторизация (OpenAPI):** JWT сотрудника; JWT клиента
- **Доступ по ролям (SecurityConfig):** Admin, Manager, Courier, Client

**Параметры:**

| Имя | In | Тип | Обязательный | Описание |
|-----|-----|-----|--------------|----------|
| `orderId` | path | integer | да |  |

**Ответ 200 (пример):**

```json
{
  "data": [
    {
      "id": 1,
      "order_id": 1,
      "order": {
        "id": 1,
        "client_id": 1,
        "client": {
          "id": {},
          "first_name": {},
          "last_name": {},
          "middle_name": {},
          "login": {},
          "email": {},
          "phone": {},
          "avatar_id": {}
        },
        "address_id": 1,
        "address": {
          "id": {},
          "client_id": {},
          "address_text": {}
        },
        "manager_id": 2,
        "manager": {
          "id": {},
          "first_name": {},
          "last_name": {},
          "middle_name": {},
          "login": {},
          "role_id": {},
          "role": {},
          "phone": {},
          "avatar_id": {},
          "is_working": {}
        },
        "courier_id": 3,
        "courier": {
          "id": {},
          "first_name": {},
          "last_name": {},
          "middle_name": {},
          "login": {},
          "role_id": {},
          "role": {},
          "phone": {},
          "avatar_id": {},
          "is_working": {}
        },
        "total_price": 2400.0,
        "created_at": "2024-01-15T10:30:00Z"
      },
      "dish_id": 1,
      "dish": {
        "id": 1,
        "name": "Стейк из говядины",
        "weight": 300.5,
        "calories": 450,
        "price": 1200.0,
        "description": "Сочный стейк из мраморной говядины"
      },
      "quantity": 2,
      "price_at_moment": 1200.0
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

### `POST /orders/{orderId}/items`

**Добавить позицию в заказ**

Доступ: Client (свои заказы), Manager

- **Авторизация (OpenAPI):** JWT сотрудника; JWT клиента
- **Доступ по ролям (SecurityConfig):** Admin, Manager, Client

**Параметры:**

| Имя | In | Тип | Обязательный | Описание |
|-----|-----|-----|--------------|----------|
| `orderId` | path | integer | да |  |

**Тело запроса (пример):**

```json
{
  "dish_id": 1,
  "quantity": 2
}
```

**Ответ 201 (пример):**

```json
{
  "id": 1,
  "order_id": 1,
  "order": {
    "id": 1,
    "client_id": 1,
    "client": {
      "id": 1,
      "first_name": "Иван",
      "last_name": "Иванов",
      "middle_name": "Петрович",
      "login": "client1",
      "email": "ivan@example.com",
      "phone": "+79001234567",
      "avatar_id": 1
    },
    "address_id": 1,
    "address": {
      "id": 1,
      "client_id": 1,
      "address_text": "г. Москва, ул. Ленина, д. 10, кв. 5"
    },
    "manager_id": 2,
    "manager": {
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
    },
    "courier_id": 3,
    "courier": {
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
    },
    "total_price": 2400.0,
    "created_at": "2024-01-15T10:30:00Z"
  },
  "dish_id": 1,
  "dish": {
    "id": 1,
    "name": "Стейк из говядины",
    "weight": 300.5,
    "calories": 450,
    "price": 1200.0,
    "description": "Сочный стейк из мраморной говядины"
  },
  "quantity": 2,
  "price_at_moment": 1200.0
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

### `GET /orders/{orderId}/items/{id}`

**Получить позицию заказа по ID**

Доступ: Все авторизованные с доступом к заказу

- **Авторизация (OpenAPI):** JWT сотрудника; JWT клиента
- **Доступ по ролям (SecurityConfig):** Admin, Manager, Courier, Client

**Параметры:**

| Имя | In | Тип | Обязательный | Описание |
|-----|-----|-----|--------------|----------|
| `orderId` | path | integer | да |  |
| `id` | path | integer | да |  |

**Ответ 200 (пример):**

```json
{
  "id": 1,
  "order_id": 1,
  "order": {
    "id": 1,
    "client_id": 1,
    "client": {
      "id": 1,
      "first_name": "Иван",
      "last_name": "Иванов",
      "middle_name": "Петрович",
      "login": "client1",
      "email": "ivan@example.com",
      "phone": "+79001234567",
      "avatar_id": 1
    },
    "address_id": 1,
    "address": {
      "id": 1,
      "client_id": 1,
      "address_text": "г. Москва, ул. Ленина, д. 10, кв. 5"
    },
    "manager_id": 2,
    "manager": {
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
    },
    "courier_id": 3,
    "courier": {
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
    },
    "total_price": 2400.0,
    "created_at": "2024-01-15T10:30:00Z"
  },
  "dish_id": 1,
  "dish": {
    "id": 1,
    "name": "Стейк из говядины",
    "weight": 300.5,
    "calories": 450,
    "price": 1200.0,
    "description": "Сочный стейк из мраморной говядины"
  },
  "quantity": 2,
  "price_at_moment": 1200.0
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

### `PUT /orders/{orderId}/items/{id}`

**Полное обновление позиции**

Доступ: Admin, Manager

- **Авторизация (OpenAPI):** JWT сотрудника
- **Доступ по ролям (SecurityConfig):** Admin, Manager

**Параметры:**

| Имя | In | Тип | Обязательный | Описание |
|-----|-----|-----|--------------|----------|
| `orderId` | path | integer | да |  |
| `id` | path | integer | да |  |

**Тело запроса (пример):**

```json
{
  "dish_id": 1,
  "quantity": 2
}
```

**Ответ 200 (пример):**

```json
{
  "id": 1,
  "order_id": 1,
  "order": {
    "id": 1,
    "client_id": 1,
    "client": {
      "id": 1,
      "first_name": "Иван",
      "last_name": "Иванов",
      "middle_name": "Петрович",
      "login": "client1",
      "email": "ivan@example.com",
      "phone": "+79001234567",
      "avatar_id": 1
    },
    "address_id": 1,
    "address": {
      "id": 1,
      "client_id": 1,
      "address_text": "г. Москва, ул. Ленина, д. 10, кв. 5"
    },
    "manager_id": 2,
    "manager": {
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
    },
    "courier_id": 3,
    "courier": {
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
    },
    "total_price": 2400.0,
    "created_at": "2024-01-15T10:30:00Z"
  },
  "dish_id": 1,
  "dish": {
    "id": 1,
    "name": "Стейк из говядины",
    "weight": 300.5,
    "calories": 450,
    "price": 1200.0,
    "description": "Сочный стейк из мраморной говядины"
  },
  "quantity": 2,
  "price_at_moment": 1200.0
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

### `PATCH /orders/{orderId}/items/{id}`

**Частичное обновление позиции**

Доступ: Admin, Manager

- **Авторизация (OpenAPI):** JWT сотрудника
- **Доступ по ролям (SecurityConfig):** Admin, Manager, Courier, Client

**Параметры:**

| Имя | In | Тип | Обязательный | Описание |
|-----|-----|-----|--------------|----------|
| `orderId` | path | integer | да |  |
| `id` | path | integer | да |  |

**Тело запроса (пример):**

```json
{
  "dish_id": 1,
  "quantity": 2
}
```

**Ответ 200 (пример):**

```json
{
  "id": 1,
  "order_id": 1,
  "order": {
    "id": 1,
    "client_id": 1,
    "client": {
      "id": 1,
      "first_name": "Иван",
      "last_name": "Иванов",
      "middle_name": "Петрович",
      "login": "client1",
      "email": "ivan@example.com",
      "phone": "+79001234567",
      "avatar_id": 1
    },
    "address_id": 1,
    "address": {
      "id": 1,
      "client_id": 1,
      "address_text": "г. Москва, ул. Ленина, д. 10, кв. 5"
    },
    "manager_id": 2,
    "manager": {
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
    },
    "courier_id": 3,
    "courier": {
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
    },
    "total_price": 2400.0,
    "created_at": "2024-01-15T10:30:00Z"
  },
  "dish_id": 1,
  "dish": {
    "id": 1,
    "name": "Стейк из говядины",
    "weight": 300.5,
    "calories": 450,
    "price": 1200.0,
    "description": "Сочный стейк из мраморной говядины"
  },
  "quantity": 2,
  "price_at_moment": 1200.0
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

### `DELETE /orders/{orderId}/items/{id}`

**Удалить позицию из заказа**

Доступ: Admin, Manager, Client (свои заказы)

- **Авторизация (OpenAPI):** JWT сотрудника; JWT клиента
- **Доступ по ролям (SecurityConfig):** Admin

**Параметры:**

| Имя | In | Тип | Обязательный | Описание |
|-----|-----|-----|--------------|----------|
| `orderId` | path | integer | да |  |
| `id` | path | integer | да |  |

**Ответ 204:** Позиция удалена

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

### `GET /orders/{orderId}/status-history`

**Получить историю статусов заказа**

Доступ: Admin, Manager (любой), Courier (назначенные), Client (свои)

- **Авторизация (OpenAPI):** JWT сотрудника; JWT клиента
- **Доступ по ролям (SecurityConfig):** Admin, Manager, Courier, Client

**Параметры:**

| Имя | In | Тип | Обязательный | Описание |
|-----|-----|-----|--------------|----------|
| `orderId` | path | integer | да |  |

**Ответ 200 (пример):**

```json
{
  "data": [
    {
      "id": 1,
      "order_id": 1,
      "order": {
        "id": 1,
        "client_id": 1,
        "client": {
          "id": {},
          "first_name": {},
          "last_name": {},
          "middle_name": {},
          "login": {},
          "email": {},
          "phone": {},
          "avatar_id": {}
        },
        "address_id": 1,
        "address": {
          "id": {},
          "client_id": {},
          "address_text": {}
        },
        "manager_id": 2,
        "manager": {
          "id": {},
          "first_name": {},
          "last_name": {},
          "middle_name": {},
          "login": {},
          "role_id": {},
          "role": {},
          "phone": {},
          "avatar_id": {},
          "is_working": {}
        },
        "courier_id": 3,
        "courier": {
          "id": {},
          "first_name": {},
          "last_name": {},
          "middle_name": {},
          "login": {},
          "role_id": {},
          "role": {},
          "phone": {},
          "avatar_id": {},
          "is_working": {}
        },
        "total_price": 2400.0,
        "created_at": "2024-01-15T10:30:00Z"
      },
      "status_id": 2,
      "status": {
        "id": 1,
        "status_name": "NEW"
      },
      "changed_at": "2024-01-15T11:00:00Z",
      "employee_id": 2,
      "employee": {
        "id": 1,
        "first_name": "Петр",
        "last_name": "Петров",
        "middle_name": "Иванович",
        "login": "manager1",
        "role_id": 2,
        "role": {
          "id": {},
          "name": {}
        },
        "phone": "+79001234567",
        "avatar_id": 1,
        "is_working": true
      },
      "client_id": 1,
      "client": {
        "id": 1,
        "first_name": "Иван",
        "last_name": "Иванов",
        "middle_name": "Петрович",
        "login": "client1",
        "email": "ivan@example.com",
        "phone": "+79001234567",
        "avatar_id": 1
      },
      "comment": "Заказ доставлен"
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

### `POST /orders/{orderId}/status-history`

**Изменить статус заказа**

Доступ: Admin, Manager, Courier (назначенные), Client (свои)

- **Авторизация (OpenAPI):** JWT сотрудника; JWT клиента
- **Доступ по ролям (SecurityConfig):** Admin, Manager, Client

**Параметры:**

| Имя | In | Тип | Обязательный | Описание |
|-----|-----|-----|--------------|----------|
| `orderId` | path | integer | да |  |

**Тело запроса (пример):**

```json
{
  "status_id": 2,
  "comment": "Заказ доставлен"
}
```

**Ответ 201 (пример):**

```json
{
  "id": 1,
  "order_id": 1,
  "order": {
    "id": 1,
    "client_id": 1,
    "client": {
      "id": 1,
      "first_name": "Иван",
      "last_name": "Иванов",
      "middle_name": "Петрович",
      "login": "client1",
      "email": "ivan@example.com",
      "phone": "+79001234567",
      "avatar_id": 1
    },
    "address_id": 1,
    "address": {
      "id": 1,
      "client_id": 1,
      "address_text": "г. Москва, ул. Ленина, д. 10, кв. 5"
    },
    "manager_id": 2,
    "manager": {
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
    },
    "courier_id": 3,
    "courier": {
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
    },
    "total_price": 2400.0,
    "created_at": "2024-01-15T10:30:00Z"
  },
  "status_id": 2,
  "status": {
    "id": 1,
    "status_name": "NEW"
  },
  "changed_at": "2024-01-15T11:00:00Z",
  "employee_id": 2,
  "employee": {
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
  },
  "client_id": 1,
  "client": {
    "id": 1,
    "first_name": "Иван",
    "last_name": "Иванов",
    "middle_name": "Петрович",
    "login": "client1",
    "email": "ivan@example.com",
    "phone": "+79001234567",
    "avatar_id": 1
  },
  "comment": "Заказ доставлен"
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
