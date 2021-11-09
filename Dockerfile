# syntax=docker/dockerfile:1
FROM python:3
ENV PYTHONUNBUFFERED=1
WORKDIR /proyecto2021S2
COPY requirements.txt /proyecto2021S2/
RUN pip install -r requirements.txt
COPY . /proyecto2021S2/


# # syntax=docker/dockerfile:1
# FROM python:3
# ENV PYTHONUNBUFFERED=1

# # set a directory for the app
# WORKDIR /proyecto2021S2

# # copy all the files to the container
# COPY . /proyecto2021S2/

# # install dependencies
# RUN pip install --no-cache-dir -r requirements.txt


# docker ps  //Para ver los contenedores activos
# docker exec -it ContainerID /bin/bash  //login y consola en el contenedor
# docker-compose up  //Iniciar sitio

