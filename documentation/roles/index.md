# Роли пользователей

Система поддерживает четыре роли. Тип учётной записи в БД (`users.user_type`) — `EMPLOYEE` или `CLIENT`; для сотрудников дополнительно задаётся роль в `roles`.

| Роль | Код в БД | Тип user | Приложение | Документация |
|------|----------|----------|------------|--------------|
| Администратор | `ADMIN` | EMPLOYEE | Desktop web | [admin.md](admin.md) |
| Менеджер | `MANAGER` | EMPLOYEE | Desktop web | [manager.md](manager.md) |
| Курьер | `COURIER` | EMPLOYEE | Mobile web | [courier.md](courier.md) |
| Клиент | — | CLIENT | Mobile web | [client.md](client.md) |

## Общие экраны

| Страница | Кто видит | Макет |
|----------|-----------|-------|
| Вход в систему | Все | [fig-16](../пояснительная-записка/assets/fig-16-prototip-stranitsy-vhoda-v-sistemu.jpg) |
| Ошибка авторизации | Все | [fig-17](../пояснительная-записка/assets/fig-17-prototip-formy-vhoda-s-oshibkoy-avtorizatsii.jpg) |
| Регистрация клиента | Только клиент (ссылка с экрана входа) | — |

**API входа:**

- Сотрудники: `POST /auth/employees/login` — [authentication.md](../api/authentication.md)
- Клиенты: `POST /auth/clients/register`, `POST /auth/clients/login` — [authentication.md](../api/authentication.md)

После входа система определяет роль и перенаправляет в соответствующий интерфейс.

## Сводная матрица возможностей

| Возможность | Admin | Manager | Courier | Client |
|-------------|:-----:|:-------:|:-------:|:------:|
| Управление меню и блюдами | + | + | | Просмотр |
| Управление ингредиентами | + | + | | |
| Управление менеджерами и курьерами | + | | | |
| Просмотр/редактирование заказов | + | + | Свои | Свои |
| Назначение курьера на заказ | + | + | | |
| Смена статуса доставки | + | + | + | Ограниченно |
| Рабочий статус курьера (`is_working`) | + | + | + | |
| Регистрация и профиль клиента | | | | + |
| Адреса доставки | | | | + |
| Справочник ролей и статусов заказа | + | | | |

Детали прав на уровне API — [errors-and-auth.md](../api/errors-and-auth.md).

## Навигационные модели

- Администратор: [fig-32](../пояснительная-записка/assets/fig-32-navigatsionnaya-model-interfeysa-administratora.jpg)
- Менеджер: [fig-22](../пояснительная-записка/assets/fig-22-prototip-stranitsy-upravleniya-zakazami-menedzher.jpg) (раздел «Заказы»)
- Курьер: [fig-33](../пояснительная-записка/assets/fig-33-navigatsionnaya-model-interfeysa-kurera.jpg)
- Клиент: [fig-34](../пояснительная-записка/assets/fig-34-navigatsionnaya-model-interfeysa-klienta.jpg)
