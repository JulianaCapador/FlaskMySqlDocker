FROM python:3

MAINTANER Jorge y Juliana

RUN mkdir /aplicacion

WORKDIR /aplicacion

COPY hola.py /aplicacion

EXPOSE 8080

COPY . /aplicacion

CMD [ "python", ".hola.py" ]
