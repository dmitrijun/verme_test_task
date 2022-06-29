# Тестовое задание в компанию Verme

Вводные в [Google Docs](https://docs.google.com/document/d/1fkx7_38rLtsUwo1c3G5Jp6dDkF0fvJAq80d985_YidI/edit?usp=sharing).

## Запуск

Перед запуском необходимо установить все необходимые модули, запустив:

```bash
    pip install -r requirements.txt
```
Чтобы запустить сервер:
```bash
    python3 manage.py runserver
```

## Получить построенное дерево целиком

```
    GET http://localhost:8000/tree_serializer 
```

## Получить поддерево

```
    GET http://localhost:8000/tree_serializer/<Tree_id>/ 
```