# Usar Python 3.12 como imagen base
FROM python:3.12-slim

# Establecer variables de entorno de Python
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Establecer el directorio de trabajo
WORKDIR /app

# Instalar dependencias del sistema necesarias para PostgreSQL y compilación
RUN apt-get update && apt-get install -y --no-install-recommends \
    gcc \
    libpq-dev \
    && rm -rf /var/lib/apt/lists/*

# Copiar el archivo de requerimientos e instalar dependencias
COPY requerimientos.txt /app/
RUN pip install --upgrade pip && pip install -r requerimientos.txt

# Copiar el resto del código del proyecto
COPY . /app/