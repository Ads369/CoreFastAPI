FROM python:3.11-slim
LABEL maintainer="info@smart-transport.ru"
ENV PYTHONUNBUFFERED 1
ENV LANG ru_RU.UTF-8
ENV TZ Asia/Yekaterinburg

RUN apt-get update &&  \
    apt-get install --no-install-recommends -y \
    libpq5 \
    git && \
    apt-get clean && rm -rf /var/lib/apt/lists/*

COPY ./requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

WORKDIR /code
COPY . /code


EXPOSE 8000
