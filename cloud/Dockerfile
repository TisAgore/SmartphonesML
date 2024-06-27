# Используем базовый образ Python
FROM python:3.9-slim

# Устанавливаем рабочую директорию внутри контейнера
WORKDIR /app

# Копируем все необходимые файлы в контейнер
COPY MLmodel.py MLTGbot.py Finaldataset.csv /app/

# Устанавливаем зависимости, если они есть (создайте файл requirements.txt, если его нет)
COPY requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt

# Запускаем основной файл
CMD ["python", "MLTGbot.py"]

