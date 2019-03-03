Installation
============

Inspector is a Django app with a Celery worker for executing the checks.
If you know Django, and how to deploy Django apps, you are already one step ahead.

Requirements
------------

* Python 3.6+
* Postgres
* Redis

Docker images
-------------

Please note that currently there is no image tagged :code:`latest` published.
This will be done once the app is stable enough and a proper release process is in place


Develop
~~~~~~~

The :code:`develop` image contains only dependencies required to run the app in development mode,
with code being mounted from the current directory. It is the fastest way to get you started,
but under no circumstances this should be used to run in production.

Steps to get you up and running

1) Clone the repo
2) :code:`docker-compose -f docker-compose-develop.yml up`

This will also deploy Redis and Postgres. The environment will be running off the configuration in:

* :code:`.envs/.develop`
* :code:`config/settings/local.py`

Master
~~~~~~

The image tagged :code:`master` contains the app code from the master branch.

Steps for easy deployment:

1) Setup Postgres and Redis
2) Copy and edit configuration files

   * :code:`.envs/.example/.django.example` -> :code:`.envs/.inspector/.django`
   * :code:`.envs/.example/.postgres.example` -> :code:`.envs/.inspector/.postgres`

3) :code:`docker-compose up`

This will start gunicorn with Whitenoise for serving static files
(http://whitenoise.evans.io/en/stable/) over HTTP on port 5000.
It's highly recommended that you use a HTTPS proxy in front such as NGINX.
For more details see:

* https://docs.djangoproject.com/en/2.1/howto/deployment/
* https://uwsgi-docs.readthedocs.io/en/latest/tutorials/Django_and_nginx.html
