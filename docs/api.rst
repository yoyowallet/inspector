API
===

Inspector exposes several REST APIs built with Django Rest Framework
(https://www.django-rest-framework.org/). By default, token authentication
is required, and for now a token can only be manually obtained through the
Django admin panel.

Scope of the APIs will change. The important part are the APIs
for running checks, therefore allowing execution in a workflow
or on a schedule by an external tool.

Full API documentation can be accessed by adding
:code:`/apidocs` to Inspector's base URL
