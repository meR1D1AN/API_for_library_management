# API для управления библиотекой
## Описание проекта
Проект представляет собой REST API для управления библиотекой. API позволяет работать с книгами, авторами, пользователями, а также отслеживать выдачу книг и их возврат. Проект построен на фреймворке Django с использованием Django REST Framework и JWT для аутентификации.
## Основной функционал:
- Управление книгами (создание, редактирование, удаление, поиск по различным критериям).
- Управление авторами (создание, редактирование, удаление).
- Управление пользователями (регистрация, авторизация, получение информации).
- Выдача и возврат книг пользователям.
- Аутентификация с помощью JWT (JSON Web Tokens).
## Стек технологий:
- Backend: Django, Django REST Framework
- База данных: PostgreSQL
- Аутентификация: JWT (используя djangorestframework-simplejwt)
- Контейнеризация: Docker, Docker Compose
- Документация API: OpenAPI (Swagger / ReDoc)
- Формат кода: PEP8
## Установка и запуск проекта
1. Клонирование репозитория
- ```bash
  git clone https://github.com/MeR1D1AN/API_for_library_management.git
  cd API_for_library_management
  ```
2. Установка зависимостей
- ```bash 
  poetry install
  ```
3. Настройте файл окружения:

   Скопируйте .env.sample в .env и настройте переменные окружения в файле .env.
- ```bash
  cp .env.sample .env
  ```
4. Применение миграции:

- ```bash
  python manage.py migrate
  ```
5. Для заполнения тестовой базы данных используйте команды:

- Команда для создания обычного пользователя
- ```bash
  python manage.py cu
  ```
- Команда для создания администратора
- ```bash
  python manage.py csu
  ```
- Добавление данных в базу данных  
- ```bash
  python manage.py loaddata static/fixture/test_info.json
  ```
6. Запуск сервера
- ```bash
  python manage.py runserver
  ```
  
## **Запуск проекта с Docker**

Убедитесь, что у вас установлен Docker и Docker Compose. Для запуска контейнеров используйте следующую команду:
- ```bash
  docker-compose up -d --build
  ```
  
### Docker Compose поднимет два сервиса:

- db: Сервис PostgreSQL для базы данных.

- app: Сервис Django, который автоматически выполнит миграции и запустит сервер разработки.


### Команды внутри контейнера:

Для создания админа
- ```bash
  docker-compose exec app python manage.py csu
  ```
Для создания обычного пользователя
- ```bash
  docker-compose exec app python manage.py csu
  ```
Для добавления тестовых данных в базу данных
- ```bash
  docker-compose exec app python manage.py loaddata static/fixture/test_info.json
  ```

## Документация API

Автогенерируемая документация доступна по следующим URL:

- Swagger: http://localhost:8000/api/docs/

- ReDoc: http://localhost:8000/api/redoc/


# Основные эндпоинты API

### Аутентификация и пользователи:
- POST /api/users/: Регистрация нового пользователя.
- POST /api/token/: Авторизация пользователя, и получение JWT токенов (access и refresh).
- POST /api/token/refresh/: Обновление JWT токена.
- GET /api/users/: Получение списка пользователей (для администратора).
### Книги:
- GET /api/books/: Получение списка всех книг.
- POST /api/books/: Создание новой книги.
- GET /api/books/{id}/: Получение информации о конкретной книге.
- PUT /api/books/{id}/: Обновление информации о книге.
- DELETE /api/books/{id}/: Удаление книги.

Поиск книг по названию, автору, жанру через параметры запроса.
### Авторы:
- GET /api/authors/: Получение списка всех авторов.
- POST /api/authors/: Создание нового автора.
- GET /api/authors/{id}/: Получение информации о конкретном авторе.
- PUT /api/authors/{id}/: Обновление информации об авторе.
- DELETE /api/authors/{id}/: Удаление автора.
### Выдача книг:
- GET /api/relbooks/: Получение списка всех выдач книг.
- POST /api/relbooks/: Создание записи о выдаче книги пользователю.
- GET /api/relbooks/{id}/: Получение информации о конкретной выдаче.
- PUT /api/relbooks/{id}/: Обновление записи о выдаче.
- DELETE /api/relbooks/{id}/: Удаление записи о выдаче.

## Дополнительная информация
- Язык приложения: Русский (ru-ru)
- Время сервера: Europe/Moscow
- Автор: Никита Шидогубов nikita.sh@gklifts.ru