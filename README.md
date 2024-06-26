# Речной трекер 🌊

Речной трекер — это Telegram бот для отслеживания уровня рек в реальном времени. Получайте актуальную информацию о состоянии водоемов прямо в вашем Telegram.

## 📋 Возможности

- 📊 Получение текущего уровня воды в реках
- 🔔 Настройка уведомлений о достижении критических уровней
- 🌍 Поддержка различных географических регионов **(в разработке)**
- 📈 Графическое отображение изменений уровня воды за определенный период **(в разработке)**

## 🚀 Как начать пользоваться ботом

1. Найдите бота в Telegram: [@Речной трекер](https://t.me/track_rivers_bot)
2. Нажмите на кнопку "Start" или отправьте команду `/start`
3. Следуйте инструкциям бота для выбора реки и настройки уведомлений

## 🛠️ Установка и запуск

Если вы хотите развернуть бота самостоятельно, выполните следующие шаги:

1. Клонируйте репозиторий:

   ```bash
   git clone https://github.com/rmirsh/emercit_bot.git
   cd emercit_bot
   
2. Заполните файл `.env`:

    ```dotenv
    DB_URL=your_db_url
    TOKEN=your_bot_token_from_BotFather
    DELAY=delay_in_notifications

    # For docker
    POSTGRES_HOST_AUTH_METHOD=
    POSTGRES_USER=
    POSTGRES_PASSWORD=
    POSTGRES_DB=

3. Установите зависимости:

   ```bash
   pip install -r requirements.txt
   ```
   Или
   ```bash
   poetry install
   ```

4. Запустите бота через `docker-compose`:

    ```bash
   docker-compose up -d
    ```

    Или просто напрямую через `bash`:

    ```
   python run.py
    ```

---
### 🛠️ Технологии и инструменты

- PostgreSQL
- Python
- aiogram
- sqlalchemy
- aiohttp
- [API для получения данных об уровнях рек](https://ru.emercit.com/)
