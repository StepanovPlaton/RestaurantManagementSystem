# Роль: Клиент (CLIENT)

Оформление заказов на доставку через mobile web. Нижняя навигация: Меню | Корзина | Заказы | Профиль.

## Возможности

- Регистрация и вход
- Просмотр активных меню и блюд
- Корзина и оформление заказа (адрес доставки)
- История заказов, отслеживание активного заказа
- Управление профилем и адресами доставки

## Страницы

### Регистрация

- **Назначение:** создание учётной записи клиента.
- **Элементы:** ФИО, логин, пароль, email, телефон.
- **API:** `POST /auth/clients/register` — [authentication.md](../api/authentication.md)

### Вход

См. [index.md](index.md#общие-экраны). API: `POST /auth/clients/login`.

### Меню

- **Назначение:** выбор блюд из активных меню.
- **Элементы:** вкладки меню; карточки блюд с ценой и счётчиком порций; кнопка «Перейти в корзину».
- **API:** `GET /menus?is_active=true`, `GET /menus/{id}/dishes`, `GET /dishes/{id}`
- **Макет:** [fig-27](../пояснительная-записка/assets/fig-27-prototip-stranitsy-prosmotra-menyu.jpg)

### Карточка блюда

- **Назначение:** подробности блюда перед добавлением в корзину.
- **Элементы:** фото, описание, вес, калории, ингредиенты, выбор количества, «В корзину».
- **API:** `GET /dishes/{id}`, `GET /dishes/{dishId}/ingredients`, `GET /dishes/{dishId}/photos`
- **Макет:** [fig-28](../пояснительная-записка/assets/fig-28-prototip-stranitsy-kartochki-blyuda.jpg)

### Корзина и оформление заказа

- **Назначение:** проверка состава, выбор адреса, создание заказа.
- **Действия:** изменить количество; выбрать адрес из сохранённых или добавить новый; подтвердить заказ.
- **API:**
  - `POST /orders` (тело: `address_id`, позиции)
  - `GET/POST /clients/{clientId}/addresses`
  - `POST /orders/{orderId}/items`
  - — [orders.md](../api/orders.md), [clients.md](../api/clients.md)
- **Макет:** корзина — в навигации [fig-34](../пояснительная-записка/assets/fig-34-navigatsionnaya-model-interfeysa-klienta.jpg)

### История заказов

- **Назначение:** список прошлых и текущих заказов.
- **Элементы:** карточки с номером, датой, статусом, составом; кнопки «Отследить», «Повторить», «Оценить» (UI; оценка — вне scope backend).
- **API:** `GET /orders` (свои заказы)
- **Макет:** [fig-29](../пояснительная-записка/assets/fig-29-prototip-stranitsy-istorii-zakazov.jpg)

### Отслеживание заказа

- **Назначение:** статус активного заказа в реальном времени.
- **Элементы:** пошаговая шкала; данные курьера; «Подтвердить получение», «Отменить заказ».
- **API:** `GET /orders/{id}`, `GET /orders/{orderId}/status-history`, `POST /orders/{orderId}/status-history`
- **Макет:** [fig-30](../пояснительная-записка/assets/fig-30-prototip-stranitsy-otslezhivaniya-zakaza.jpg)

### Профиль

- **Назначение:** личные данные и адреса.
- **Элементы:** аватар, ФИО, email; «Личные данные», «Адреса доставки»; ссылки **«Справка»** (`/app/help`) и **«О разработчиках»** (`/app/about`); выход.
- **API:** `GET/PATCH /clients/{id}`, `/clients/{clientId}/addresses`, `POST /avatars`
- **Макет:** [fig-31](../пояснительная-записка/assets/fig-31-prototip-stranitsy-profilya-polzovatelya.jpg)

## Навигация

[fig-34](../пояснительная-записка/assets/fig-34-navigatsionnaya-model-interfeysa-klienta.jpg): Меню → карточка блюда → корзина → заказ → отслеживание.

## Функции только в UI (нет в API)

- **Оценить заказ** — предусмотрено в прототипе, endpoint в backend отсутствует (см. [zamechaniya](../zamechaniya-k-poyasnitelnoj-zapiske.md)).
