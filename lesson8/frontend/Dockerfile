FROM python:3.11-slim
# Устанавливаем рабочую директорию внутри контейнера
WORKDIR /app
# Копируем файл с зависимостями
COPY requirements.txt .
# Устанавливаем зависимости
RUN pip install --no-cache-dir -r requirements.txt
# Копируем весь остальной код приложения в контейнер
COPY . .
# Указываем порт, на котором будет работать приложение (согласно docker-compose порт 8000)
EXPOSE 8000
# Запускаем сервер uvicorn
CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8000"]