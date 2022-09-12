FROM python:3.10.0-alpine

WORKDIR /app

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONNUNBUFFERED 1

COPY . .

RUN pip install --upgrade pip

RUN pip install -r ./requirements/local.txt


ENTRYPOINT ["sh", "./entrypoint.sh"]