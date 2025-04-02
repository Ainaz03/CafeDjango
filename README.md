# Cafe Orders

Простое веб-приложение на Django для управления заказами в кафе.

## Возможности
- Создание заказов с указанием стола и списка блюд
- Просмотр списка всех заказов
- Обновление статуса заказа (в ожидании, готово, оплачено)
- Удаление заказов
- Расчёт общей выручки за смену
- API для получения списка заказов

## Установка и запуск
### 1. Клонирование репозитория
```bash
git clone https://github.com/Ainaz03/CafeDjango
cd cafe_orders
```

### 2. Установка зависимостей
```
python -m venv venv
source venv/bin/activate  # Для Linux/Mac
venv\Scripts\activate  # Для Windows
pip install -r requirements.txt
```

### 3. Настройка базы данных
- Убедитесь, что у вас установлен PostgreSQL.
- В файле `settings.py` укажите данные для подключения к БД.
```
# База данных
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': os.getenv('DB_NAME', 'cafe_db'),
        'USER': os.getenv('DB_USER', 'postgres'),           # Вместо postgres - ваше имя пользователя
        'PASSWORD': os.getenv('DB_PASSWORD', 'Password'),   # Вместо passwaord - ваш пароль
        'HOST': os.getenv('DB_HOST', 'localhost'),
        'PORT': os.getenv('DB_PORT', '5432'),
    }
}
```

### 4. Выполнение миграций
```
python manage.py migrate
```

### 5. Запуск сервера
```
python manage.py runserver
```
Приложение будет доступно по адресу: [http://127.0.0.1:8000/](http://127.0.0.1:8000/).

## API
- Получить список заказов: `GET /api/orders/`

## Тестирование
Для запуска тестов выполните команду:
```bash
python manage.py test orders
```
