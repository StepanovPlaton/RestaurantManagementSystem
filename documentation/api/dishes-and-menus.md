# Блюда, меню, ингредиенты, фото

Базовый URL: `http://localhost:8080`

Полная спецификация: [swagger.yaml](../swagger.yaml).
Матрица прав: [errors-and-auth.md](errors-and-auth.md) — при расхождении с OpenAPI доверяйте SecurityConfig.

---

### `GET /dishes`

**Получить список блюд**

Доступ: Все авторизованные

- **Авторизация (OpenAPI):** JWT сотрудника; JWT клиента
- **Доступ по ролям (SecurityConfig):** Admin, Manager, Client, Courier (GET); Admin, Manager (изменение)

**Параметры:**

Нет.

**Ответ 200 (пример):**

```json
{
  "data": [
    {
      "id": 1,
      "name": "Стейк из говядины",
      "weight": 300.5,
      "calories": 450,
      "price": 1200.0,
      "description": "Сочный стейк из мраморной говядины"
    }
  ],
  "total": 30
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

### `POST /dishes`

**Создать блюдо**

Доступ: Admin, Manager

- **Авторизация (OpenAPI):** JWT сотрудника
- **Доступ по ролям (SecurityConfig):** Admin, Manager

**Параметры:**

Нет.

**Тело запроса (пример):**

```json
{
  "name": "Стейк из говядины",
  "weight": 300.5,
  "calories": 450,
  "price": 1200.0,
  "description": "Сочный стейк из мраморной говядины"
}
```

**Ответ 201 (пример):**

```json
{
  "id": 1,
  "name": "Стейк из говядины",
  "weight": 300.5,
  "calories": 450,
  "price": 1200.0,
  "description": "Сочный стейк из мраморной говядины"
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

### `GET /dishes/{dishId}/ingredients`

**Получить ингредиенты блюда**

Доступ: Все авторизованные

- **Авторизация (OpenAPI):** JWT сотрудника; JWT клиента
- **Доступ по ролям (SecurityConfig):** Admin, Manager, Client, Courier (GET); Admin, Manager (изменение)

**Параметры:**

| Имя | In | Тип | Обязательный | Описание |
|-----|-----|-----|--------------|----------|
| `dishId` | path | integer | да |  |

**Ответ 200 (пример):**

```json
{
  "data": [
    {
      "id": 1,
      "name": "Говядина"
    }
  ],
  "total": 1
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

### `POST /dishes/{dishId}/ingredients`

**Добавить ингредиент к блюду**

Доступ: Admin, Manager

- **Авторизация (OpenAPI):** JWT сотрудника
- **Доступ по ролям (SecurityConfig):** Admin, Manager

**Параметры:**

| Имя | In | Тип | Обязательный | Описание |
|-----|-----|-----|--------------|----------|
| `dishId` | path | integer | да |  |

**Тело запроса (пример):**

```json
{
  "ingredient_id": 1
}
```

**Ответ 201 (пример):**

```json
{
  "dish_id": 1,
  "ingredient_id": 1,
  "dish": {
    "id": 1,
    "name": "Стейк из говядины",
    "weight": 300.5,
    "calories": 450,
    "price": 1200.0,
    "description": "Сочный стейк из мраморной говядины"
  },
  "ingredient": {
    "id": 1,
    "name": "Говядина"
  }
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

### `DELETE /dishes/{dishId}/ingredients/{ingredientId}`

**Удалить ингредиент из блюда**

Доступ: Admin, Manager

- **Авторизация (OpenAPI):** JWT сотрудника
- **Доступ по ролям (SecurityConfig):** Admin, Manager

**Параметры:**

| Имя | In | Тип | Обязательный | Описание |
|-----|-----|-----|--------------|----------|
| `dishId` | path | integer | да |  |
| `ingredientId` | path | integer | да |  |

**Ответ 204:** Ингредиент удален

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

### `GET /dishes/{dishId}/photos`

**Получить фотографии блюда**

Доступ: Все авторизованные

- **Авторизация (OpenAPI):** JWT сотрудника; JWT клиента
- **Доступ по ролям (SecurityConfig):** Admin, Manager, Client, Courier (GET); Admin, Manager (изменение)

**Параметры:**

| Имя | In | Тип | Обязательный | Описание |
|-----|-----|-----|--------------|----------|
| `dishId` | path | integer | да |  |

**Ответ 200 (пример):**

```json
{
  "data": [
    {
      "id": 1,
      "path": "/uploads/photos/dish1.jpg"
    }
  ],
  "total": 1
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

### `POST /dishes/{dishId}/photos`

**Привязать фото к блюду**

Доступ: Admin, Manager

- **Авторизация (OpenAPI):** JWT сотрудника
- **Доступ по ролям (SecurityConfig):** Admin, Manager

**Параметры:**

| Имя | In | Тип | Обязательный | Описание |
|-----|-----|-----|--------------|----------|
| `dishId` | path | integer | да |  |

**Тело запроса (пример):**

```json
{
  "photo_id": 1
}
```

**Ответ 201 (пример):**

```json
{
  "dish_id": 1,
  "photo_id": 1,
  "dish": {
    "id": 1,
    "name": "Стейк из говядины",
    "weight": 300.5,
    "calories": 450,
    "price": 1200.0,
    "description": "Сочный стейк из мраморной говядины"
  },
  "photo": {
    "id": 1,
    "path": "/uploads/photos/dish1.jpg"
  }
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

### `DELETE /dishes/{dishId}/photos/{photoId}`

**Отвязать фото от блюда**

Доступ: Admin, Manager

- **Авторизация (OpenAPI):** JWT сотрудника
- **Доступ по ролям (SecurityConfig):** Admin, Manager

**Параметры:**

| Имя | In | Тип | Обязательный | Описание |
|-----|-----|-----|--------------|----------|
| `dishId` | path | integer | да |  |
| `photoId` | path | integer | да |  |

**Ответ 204:** Фото отвязано

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

### `GET /dishes/{id}`

**Получить блюдо по ID**

Доступ: Все авторизованные

- **Авторизация (OpenAPI):** JWT сотрудника; JWT клиента
- **Доступ по ролям (SecurityConfig):** Admin, Manager, Client, Courier (GET); Admin, Manager (изменение)

**Параметры:**

| Имя | In | Тип | Обязательный | Описание |
|-----|-----|-----|--------------|----------|
| `id` | path | integer | да |  |

**Ответ 200 (пример):**

```json
{
  "id": 1,
  "name": "Стейк из говядины",
  "weight": 300.5,
  "calories": 450,
  "price": 1200.0,
  "description": "Сочный стейк из мраморной говядины"
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

### `PUT /dishes/{id}`

**Полное обновление блюда**

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
  "name": "Стейк из говядины",
  "weight": 300.5,
  "calories": 450,
  "price": 1200.0,
  "description": "Сочный стейк из мраморной говядины"
}
```

**Ответ 200 (пример):**

```json
{
  "id": 1,
  "name": "Стейк из говядины",
  "weight": 300.5,
  "calories": 450,
  "price": 1200.0,
  "description": "Сочный стейк из мраморной говядины"
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

### `PATCH /dishes/{id}`

**Частичное обновление блюда**

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
  "name": "Стейк из говядины",
  "weight": 300.5,
  "calories": 450,
  "price": 1200.0,
  "description": "Сочный стейк из мраморной говядины"
}
```

**Ответ 200 (пример):**

```json
{
  "id": 1,
  "name": "Стейк из говядины",
  "weight": 300.5,
  "calories": 450,
  "price": 1200.0,
  "description": "Сочный стейк из мраморной говядины"
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

### `DELETE /dishes/{id}`

**Удалить блюдо**

Доступ: Admin, Manager

- **Авторизация (OpenAPI):** JWT сотрудника
- **Доступ по ролям (SecurityConfig):** Admin, Manager

**Параметры:**

| Имя | In | Тип | Обязательный | Описание |
|-----|-----|-----|--------------|----------|
| `id` | path | integer | да |  |

**Ответ 204:** Блюдо удалено

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

### `GET /ingredients`

**Получить список ингредиентов**

Доступ: Все авторизованные

- **Авторизация (OpenAPI):** JWT сотрудника; JWT клиента
- **Доступ по ролям (SecurityConfig):** Admin, Manager, Client, Courier (GET); Admin, Manager (изменение)

**Параметры:**

Нет.

**Ответ 200 (пример):**

```json
{
  "data": [
    {
      "id": 1,
      "name": "Говядина"
    }
  ],
  "total": 20
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

### `POST /ingredients`

**Создать ингредиент**

Доступ: Admin, Manager

- **Авторизация (OpenAPI):** JWT сотрудника
- **Доступ по ролям (SecurityConfig):** Admin, Manager

**Параметры:**

Нет.

**Тело запроса (пример):**

```json
{
  "name": "Говядина"
}
```

**Ответ 201 (пример):**

```json
{
  "id": 1,
  "name": "Говядина"
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

### `GET /ingredients/{id}`

**Получить ингредиент по ID**

Доступ: Все авторизованные

- **Авторизация (OpenAPI):** JWT сотрудника; JWT клиента
- **Доступ по ролям (SecurityConfig):** Admin, Manager, Client, Courier (GET); Admin, Manager (изменение)

**Параметры:**

| Имя | In | Тип | Обязательный | Описание |
|-----|-----|-----|--------------|----------|
| `id` | path | integer | да |  |

**Ответ 200 (пример):**

```json
{
  "id": 1,
  "name": "Говядина"
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

### `PUT /ingredients/{id}`

**Полное обновление ингредиента**

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
  "name": "Говядина"
}
```

**Ответ 200 (пример):**

```json
{
  "id": 1,
  "name": "Говядина"
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

### `PATCH /ingredients/{id}`

**Частичное обновление ингредиента**

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
  "name": "Говядина"
}
```

**Ответ 200 (пример):**

```json
{
  "id": 1,
  "name": "Говядина"
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

### `DELETE /ingredients/{id}`

**Удалить ингредиент**

Доступ: Admin, Manager

- **Авторизация (OpenAPI):** JWT сотрудника
- **Доступ по ролям (SecurityConfig):** Admin, Manager

**Параметры:**

| Имя | In | Тип | Обязательный | Описание |
|-----|-----|-----|--------------|----------|
| `id` | path | integer | да |  |

**Ответ 204:** Ингредиент удален

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

### `GET /menus`

**Получить список меню**

Доступ: Все авторизованные. Клиенты видят только активные меню

- **Авторизация (OpenAPI):** JWT сотрудника; JWT клиента
- **Доступ по ролям (SecurityConfig):** Admin, Manager, Client, Courier (GET); Admin, Manager (изменение)

**Параметры:**

| Имя | In | Тип | Обязательный | Описание |
|-----|-----|-----|--------------|----------|
| `is_active` | query | boolean | нет |  |

**Ответ 200 (пример):**

```json
{
  "data": [
    {
      "id": 1,
      "name": "Летнее меню",
      "seasonality": "Лето",
      "is_active": true
    }
  ],
  "total": 4
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

### `POST /menus`

**Создать меню**

Доступ: Admin, Manager

- **Авторизация (OpenAPI):** JWT сотрудника
- **Доступ по ролям (SecurityConfig):** Admin, Manager

**Параметры:**

Нет.

**Тело запроса (пример):**

```json
{
  "name": "Летнее меню",
  "seasonality": "Лето",
  "is_active": true
}
```

**Ответ 201 (пример):**

```json
{
  "id": 1,
  "name": "Летнее меню",
  "seasonality": "Лето",
  "is_active": true
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

### `GET /menus/{id}`

**Получить меню по ID**

Доступ: Все авторизованные

- **Авторизация (OpenAPI):** JWT сотрудника; JWT клиента
- **Доступ по ролям (SecurityConfig):** Admin, Manager, Client, Courier (GET); Admin, Manager (изменение)

**Параметры:**

| Имя | In | Тип | Обязательный | Описание |
|-----|-----|-----|--------------|----------|
| `id` | path | integer | да |  |

**Ответ 200 (пример):**

```json
{
  "id": 1,
  "name": "Летнее меню",
  "seasonality": "Лето",
  "is_active": true
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

### `PUT /menus/{id}`

**Полное обновление меню**

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
  "name": "Летнее меню",
  "seasonality": "Лето",
  "is_active": true
}
```

**Ответ 200 (пример):**

```json
{
  "id": 1,
  "name": "Летнее меню",
  "seasonality": "Лето",
  "is_active": true
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

### `PATCH /menus/{id}`

**Частичное обновление меню**

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
  "name": "Летнее меню",
  "seasonality": "Лето",
  "is_active": true
}
```

**Ответ 200 (пример):**

```json
{
  "id": 1,
  "name": "Летнее меню",
  "seasonality": "Лето",
  "is_active": true
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

### `DELETE /menus/{id}`

**Удалить меню**

Доступ: Admin, Manager

- **Авторизация (OpenAPI):** JWT сотрудника
- **Доступ по ролям (SecurityConfig):** Admin, Manager

**Параметры:**

| Имя | In | Тип | Обязательный | Описание |
|-----|-----|-----|--------------|----------|
| `id` | path | integer | да |  |

**Ответ 204:** Меню удалено

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

### `GET /menus/{menuId}/dishes`

**Получить блюда в меню**

Доступ: Все авторизованные

- **Авторизация (OpenAPI):** JWT сотрудника; JWT клиента
- **Доступ по ролям (SecurityConfig):** Admin, Manager, Client, Courier (GET); Admin, Manager (изменение)

**Параметры:**

| Имя | In | Тип | Обязательный | Описание |
|-----|-----|-----|--------------|----------|
| `menuId` | path | integer | да |  |

**Ответ 200 (пример):**

```json
{
  "data": [
    {
      "id": 1,
      "name": "Стейк из говядины",
      "weight": 300.5,
      "calories": 450,
      "price": 1200.0,
      "description": "Сочный стейк из мраморной говядины"
    }
  ],
  "total": 1
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

### `POST /menus/{menuId}/dishes`

**Добавить блюдо в меню**

Доступ: Admin, Manager

- **Авторизация (OpenAPI):** JWT сотрудника
- **Доступ по ролям (SecurityConfig):** Admin, Manager

**Параметры:**

| Имя | In | Тип | Обязательный | Описание |
|-----|-----|-----|--------------|----------|
| `menuId` | path | integer | да |  |

**Тело запроса (пример):**

```json
{
  "dish_id": 1
}
```

**Ответ 201 (пример):**

```json
{
  "menu_id": 1,
  "dish_id": 1,
  "menu": {
    "id": 1,
    "name": "Летнее меню",
    "seasonality": "Лето",
    "is_active": true
  },
  "dish": {
    "id": 1,
    "name": "Стейк из говядины",
    "weight": 300.5,
    "calories": 450,
    "price": 1200.0,
    "description": "Сочный стейк из мраморной говядины"
  }
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

### `DELETE /menus/{menuId}/dishes/{dishId}`

**Удалить блюдо из меню**

Доступ: Admin, Manager

- **Авторизация (OpenAPI):** JWT сотрудника
- **Доступ по ролям (SecurityConfig):** Admin, Manager

**Параметры:**

| Имя | In | Тип | Обязательный | Описание |
|-----|-----|-----|--------------|----------|
| `menuId` | path | integer | да |  |
| `dishId` | path | integer | да |  |

**Ответ 204:** Блюдо удалено из меню

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

### `POST /photos`

**Загрузить фото**

Доступ: Все авторизованные. Multipart-форма с полем 'file' (jpeg/png/webp, до 10 MB). Возвращает метаданные с URL для GET статики.

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
  "path": "/uploads/photos/dish1.jpg"
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

### `GET /photos/{id}`

**Получить метаданные фото**

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
  "path": "/uploads/photos/dish1.jpg"
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

### `DELETE /photos/{id}`

**Удалить фото**

Доступ: Admin, Manager. Удаляет файл с диска и запись из БД. Связки с блюдами через dish_photos удаляются каскадно.

- **Авторизация (OpenAPI):** JWT сотрудника
- **Доступ по ролям (SecurityConfig):** Admin, Manager

**Параметры:**

| Имя | In | Тип | Обязательный | Описание |
|-----|-----|-----|--------------|----------|
| `id` | path | integer | да |  |

**Ответ 204:** Фото удалено

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
