# Stage 1: Build Stage
FROM python:3.8-slim AS build

WORKDIR /app

RUN apt-get update && apt-get install -y \
    gcc \
    pkg-config \
    default-libmysqlclient-dev \
    && rm -rf /var/lib/apt/lists/*

COPY . .

RUN pip install flask mysqlclient

# Stage 2 production stage
FROM python:3.8-slim

WORKDIR /app

COPY --from=Build /app /app

EXPOSE 5002

CMD [ "python", "app.py" ]