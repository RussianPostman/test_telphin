Для тестового запуска необходимо:

1. Создать и заполнить файл с переменными окружения:

```
TARIFFS_API_KEY
TARIFFS_URL
```

2. Запустить проект командой

```
docker-compose up -d --build
```

3. Работа с API
Документация будет доступна по "http://localhost:8004/docs"

Оттуда же можно попроьбовать единственный эндпоинт

# Запуск без докера:

1. Развернуть виртуальное окружение и установить зависимости 

- для MacOS
```
python3 -m venv venv
source venv/bin/activate
```
- для Windows
```
python -m venv venv
source venv/Scripts/activate
```
2. Установить зависимости
```
pip install requirements.txt
```
3. Запустить веб сервис
```
uvicorn api_project.composites.api:app --host 0.0.0.0 --reload
```
