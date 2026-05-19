# Restaurant Management System

Система управления рестораном с доставкой заказов: меню и блюда, обработка заказов, роли сотрудников (администратор, менеджер, курьер) и клиентское мобильное приложение.

![ERD Diagram](./screenshots/ERD.png)

## О проекте

- REST API на Spring Boot (JWT, PostgreSQL, Flyway)
- Раздельная авторизация сотрудников и клиентов
- Управление меню, блюдами, ингредиентами, фотографиями
- Заказы с историей статусов и назначением курьеров
- **Backend** реализован; **frontend** — в разработке

Подробная документация: **[documentation/README.md](./documentation/README.md)**

## Роли

| Роль | Описание |
|------|----------|
| **Admin** | Меню, блюда, ингредиенты, сотрудники |
| **Manager** | Заказы, клиенты, назначение курьеров |
| **Courier** | Свои заказы, статус доставки, смена |
| **Client** | Меню, корзина, заказы, профиль и адреса |

## Структура репозитория

```
RestaurantManagementSystem/
├── backend/                 # Submodule: Spring Boot API
├── frontend/                # Submodule: веб-клиент (в разработке)
├── documentation/           # Актуальная документация
│   ├── api/                 # Описание endpoint-ов
│   ├── data/                # Модель данных
│   ├── roles/               # Роли и страницы UI
│   ├── product/             # Описание продукта
│   ├── swagger.yaml         # OpenAPI 3.0
│   ├── db.dbml              # Схема БД
│   └── пояснительная-записка/  # Архив проектирования (курсовой)
├── deploy/nginx/            # nginx config for root docker-compose
├── docker-compose.yml       # Full stack (frontend + backend + DB + nginx)
├── screenshots/
│   └── ERD.png
└── README.md
```

## Полный стек в Docker

Из корня репозитория (нужны submodules `backend/` и `frontend/`):

```bash
git submodule update --init --recursive
cp .env.example .env
docker compose up -d --build
```

- Приложение: [http://localhost](http://localhost)
- Swagger UI: [http://localhost/swagger-ui.html](http://localhost/swagger-ui.html)
- OpenAPI JSON: [http://localhost/api-docs](http://localhost/api-docs)

Опционально:

```bash
# pgAdmin → http://127.0.0.1:5050 (хост БД в UI: postgres, порт 5432)
docker compose --profile devtools up -d

# Публикация в интернет через CloudPub (токен в .env: CLOUDPUB_TOKEN)
docker compose --profile tunnel up -d
docker compose logs -f cloudpub
```

## Быстрый старт (backend)

Только API и PostgreSQL (без frontend/nginx):

```bash
cd backend
cp .env.example .env
docker compose up -d
# API: http://localhost:8080
# Swagger UI: http://localhost:8080/swagger-ui.html
```

## Быстрый старт (frontend)

```bash
cd frontend
npm install
cp .env.example .env.local
npm run dev
# http://localhost:3000
```

Подробнее: [frontend/README.md](./frontend/README.md).

## Лицензия

Проект распространяется под лицензией [**WTFPL**](./LICENCE).
