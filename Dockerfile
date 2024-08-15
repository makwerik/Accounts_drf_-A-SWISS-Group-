FROM python:3.10

#  рабочая директория внутри контейнера
WORKDIR /app

# копируем файл зависимостей в контейнер
COPY requirements.txt .

# установка зависимостей
RUN pip install --no-cache-dir -r requirements.txt

# копируем все файлы проекта в рабочую директорию
COPY . /app

# переходим в директорию проекта, где находится manage.py
WORKDIR /app/myproject

# выполняем миграции, затем запускаем сервер
CMD ["sh", "-c", "python manage.py migrate && python manage.py runserver 0.0.0.0:8000"]
