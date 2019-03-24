FROM python:3.7-alpine

ENV PYTHONUNBUFFERED 1

RUN apk update \
  # psycopg2 dependencies
  && apk add --virtual build-deps gcc python3-dev musl-dev \
  && apk add postgresql-dev mariadb-dev\
  # Pillow dependencies
  && apk add jpeg-dev zlib-dev freetype-dev lcms2-dev openjpeg-dev tiff-dev tk-dev tcl-dev \
  # CFFI dependencies
  && apk add libffi-dev py-cffi \
  # Translations dependencies
  && apk add gettext \
  # https://docs.djangoproject.com/en/dev/ref/django-admin/#dbshell
  && apk add postgresql-client

# Requirements are installed here to ensure they will be cached.
COPY ./requirements /requirements
RUN pip install -r /requirements/local.txt

COPY ./compose/master/inspector/entrypoint /entrypoint
COPY ./compose/develop/inspector/start /start
COPY ./compose/develop/inspector/celery/worker/start /start-celeryworker
COPY ./compose/develop/inspector/celery/beat/start /start-celerybeat
COPY ./compose/develop/inspector/celery/flower/start /start-flower

WORKDIR /app

ENTRYPOINT ["/entrypoint"]
