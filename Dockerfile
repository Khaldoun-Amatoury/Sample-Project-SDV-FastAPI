FROM python:3.10-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the entire current directory (including .env)
COPY . .

EXPOSE 80

CMD ["python", "./src/main.py"]
