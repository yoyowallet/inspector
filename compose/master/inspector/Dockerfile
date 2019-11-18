FROM python:3.7-alpine

ENV PYTHONUNBUFFERED 1

RUN apk update \
  # psycopg2 dependencies
  && apk add --virtual build-deps gcc python3-dev musl-dev \
  && apk add postgresql-dev \
  # Pillow dependencies
  && apk add jpeg-dev zlib-dev freetype-dev lcms2-dev openjpeg-dev tiff-dev tk-dev tcl-dev \
  # CFFI dependencies
  && apk add libffi-dev py-cffi

RUN addgroup -S django \
    && adduser -S -G django django

# Requirements are installed here to ensure they will be cached.
COPY ./requirements /requirements
RUN pip install --no-cache-dir -r /requirements/production.txt

COPY ./compose/master/inspector/entrypoint /entrypoint
COPY ./compose/master/inspector/start /start
COPY ./compose/master/inspector/celery/worker/start /start-celeryworker
COPY ./compose/master/inspector/celery/beat/start /start-celerybeat
COPY ./compose/master/inspector/celery/flower/start /start-flower

RUN chown django /entrypoint /start*

COPY . /app

RUN chown -R django /app

USER django

WORKDIR /app

ENV DJANGO_SETTINGS_MODULE config.settings.production

ENTRYPOINT ["/entrypoint"]
