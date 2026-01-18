FROM python:3.8-slim

WORKDIR /app
COPY . .

# Install system dependencies for mysqlclient
RUN apt-get update && apt-get install -y \
    gcc \
    pkg-config \
    default-libmysqlclient-dev \
    && rm -rf /var/lib/apt/lists/*

RUN pip install flask mysqlclient

EXPOSE 5002
CMD ["python", "app.py"]