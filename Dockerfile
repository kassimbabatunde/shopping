FROM python:3.8-alpine

ENV PATH="/scripts:${PATH}"

RUN apk add --update --no-cache --virtual .tmp gcc libc-dev linux-headers


RUN mkdir /weddingapp
WORKDIR /weddingapp
COPY requirements.txt /weddingapp/
RUN pip install -r requirements.txt
COPY . /weddingapp/

COPY scripts /scripts

RUN apk del .tmp
RUN chmod +x /scripts/*

RUN mkdir -p /vol/web/media
RUN mkdir -p /vol/web/static

RUN adduser -D devuser
RUN chown -R devuser:devuser /vol
RUN chmod -R 755 /vol/web

USER devuser

CMD [ "entrypoint.sh" ]