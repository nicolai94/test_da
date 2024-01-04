# Test DA
---
## Запуск
**Действия:**
1. Склонировать репозиторий
2. Ввести команду docker-compose up --build
4. Дождаться запуска контейнера
---
## Документация
**localhost:8000/docs**
---
## Админка
**localhost:8000/admin**
---
## Создание пользователя
1. Зайти в контейнер docker-compose exec backend bash
2. Ввести python cli.py createuser
3. Ввести данные и подтвердить