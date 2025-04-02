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
```
git clone https://github.com/Ainaz03/CafeDjango
cd CafeDjango
```

### 2. Запуск виртуальной среды
Для Windows
```
venv\Scripts\activate
cd cafe_orders
```

### 3. Настройка базы данных
- Убедитесь, что у вас установлен PostgreSQL.
- Открываем psql (или PgAdmin) и выполняем команду:
```
CREATE DATABASE cafe_db;
```
- В файле `cafe_orders\settings.py` укажите данные для подключения к БД.
```
# База данных
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': os.getenv('DB_NAME', 'cafe_db'),            # cafe_db - название созданной БД
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
Приложение будет доступно по адресу: http://127.0.0.1:8000/

## API
- Получить список заказов: `GET http://127.0.0.1:8000/orders/api/orders/`

## Тестирование
Для запуска тестов выполните команду:
```
python manage.py test orders
```
