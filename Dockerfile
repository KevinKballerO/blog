# Usar una imagen base de Python
FROM python:3.8

# Establecer el directorio de trabajo
WORKDIR /usr/src/app

# Copiar los archivos de requisitos al contenedor
COPY requirements.txt ./

# Instalar las dependencias
RUN pip install --no-cache-dir -r requirements.txt

# Copiar el resto del código de la aplicación
COPY . .

# Exponer el puerto en el que se ejecutará la aplicación
EXPOSE 8000

# Comando para ejecutar la aplicación
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]

#docker build -t my-django-blog . construir la imagen de Docker

#docker run -p 8000:8000 my-django-blog   Ejecutar el contenedor de Docker

