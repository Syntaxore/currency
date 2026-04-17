# 💱 Currency Bot

Telegram-бот для конвертации валют в реальном времени, написанный на Python с использованием aiogram 3 и ExchangeRate API.

## 📌 Возможности

- Конвертация любой пары валют по актуальному курсу
- Простой ввод в формате `USD:RUB:100`
- Обработка ошибок формата и API
- Inline-клавиатура для удобного взаимодействия

## 🛠 Стек

| Технология | Назначение |
|---|---|
| Python 3.14 | Основной язык |
| aiogram 3 | Telegram Bot Framework |
| ExchangeRate API | Курсы валют в реальном времени |
| python-dotenv | Управление переменными окружения |

## 📁 Структура проекта

```
currency/
├── main.py                     # Точка входа
├── requirements.txt
├── .env                        # Переменные окружения (не в репозитории)
└── src/
    ├── __init__.py             # Инициализация бота и диспетчера
    ├── CurrencyAPI/
    │   └── currency.py         # Обёртка над ExchangeRate API
    ├── handlers/
    │   ├── start.py            # Обработчик /start
    │   └── get_currency.py     # Обработчик конвертации
    ├── keyboards/
    │   └── start_kb.py         # Inline-клавиатура
    └── States/
        └── states.py           # FSM-состояния
```

## 🚀 Запуск

### 1. Клонировать репозиторий

```bash
git clone https://github.com/your-username/currency-bot.git
cd currency-bot
```

### 2. Создать виртуальное окружение и установить зависимости

```bash
python -m venv .venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate
pip install -r requirements.txt
```

### 3. Настроить переменные окружения

Создать файл `.env` в корне проекта:

```env
BOT_API=your_telegram_bot_token
API_KEY=your_exchangerate_api_key
```

- **BOT_API** — токен бота от [@BotFather](https://t.me/BotFather)
- **API_KEY** — ключ от [ExchangeRate API](https://www.exchangerate-api.com/) (есть бесплатный план)

### 4. Запустить бота

```bash
python main.py
```

## 💬 Как пользоваться

1. Отправить `/start`
2. Нажать кнопку **💱 Конвертация**
3. Ввести данные в формате:

```
ВАЛЮТА1:ВАЛЮТА2:СУММА
```

Примеры:
```
USD:RUB:100
EUR:USD:50
BTC:USD:0.5
```

## 📄 Лицензия

MIT