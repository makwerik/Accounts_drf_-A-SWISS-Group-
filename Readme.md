<h1>A_SWISS_GROUP Project</h1>

<h2>Описание проекта</h2>

Это веб-приложение на Django с REST API для управления пользователями. Приложение реализовано с использованием Django и Django REST Framework (DRF). Для упрощения запуска проекта используется Docker.

<h2>Функциональность</h2>

- **Создание пользователя** с валидацией полей в зависимости от заголовка `x-Device`.
- **Получение пользователя по ID**.
- **Поиск пользователей** по одному или нескольким полям: фамилия, имя, отчество, телефон, email.

<h2>Стек технологий</h2>

- Python 3.10
- Django
- Django REST Framework
- Docker
- SQLite (Т.к условий не было, оставил по умолчанию)

---

<h2>Установка с Docker</h2>

<h3>1. Клонирование репозитория</h3>

```bash
git clone https://github.com/makwerik/Accounts_drf_-A-SWISS-Group-.git
cd A_SWISS_GROUP
```

<h3>2. Запуск контейнеров</h3>

```bash
docker-compose up --build
```

<h3>3. Применение миграций</h3>
Если миграции не были применены автоматически, выполните команду:

```bash
pip install -r requirements.txt
```

<h3>4. Применение миграций</h3>

```bash
docker-compose up -d
docker-compose exec web python manage.py migrate
```

<h3>4. Создание суперпользователя</h3>
Для доступа к админке Django выполните команду для создания суперпользователя:

```bash
docker-compose up -d
docker-compose exec web python manage.py createsuperuser
```

<h3>5. Запуск тестов</h3>

```bash
docker-compose up -d
docker-compose exec web python manage.py test
```

P.s (login:makwerik, password:12345)
---
<h2>Локальная установка без Docker</h2>

<h3>1. Клонирование репозитория</h3>

```bash
git clone https://github.com/makwerik/Accounts_drf_-A-SWISS-Group-.git
cd A_SWISS_GROUP
```

<h3>2. Создание и активация виртуального окружения</h3>

```bash
python -m venv venv
source venv/bin/activate  # для Windows: venv\Scripts\activate
```

<h3>3. Установка зависимостей</h3>

```bash
pip install -r requirements.txt
```

<h3>4. Применение миграций</h3>

```bash
python manage.py migrate
```

<h3>5. Запуск сервера разработки</h3>

```bash
python manage.py runserver
```

<h3>6. Запуск тестов</h3>

```bash
python manage.py test
```

---
<h2>Использование API</h2>

<h3>Создание пользователя</h3>

``http://127.0.0.1:8000/api/users/`` POST

<p>В зависимости от заголовка x-Device, разные поля обязательны:

x-Device: mail - обязательные поля: first_name, email<br>
x-Device: mobile - обязательные поля: phone_number<br>
x-Device: web - обязательные поля: все поля, кроме email и residence_address

</p>

<h3>Получение пользователя по ID</h3>
``http://127.0.0.1:8000/api/get_user_id/`` GET<br>

``body = {"userid":"3"}``

<h3>Поиск пользователей по критериям</h3>

<h4>Пример:</h4>

``http://127.0.0.1:8000/api/search_user/?last_name=Верёвкин`` GET

<p>Поддерживаемые параметры для поиска:<br>

first_name <br>
last_name <br>
middle_name <br>
phone_number<br>
email</p>
