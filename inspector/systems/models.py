from django.db import models
from encrypted_model_fields.fields import EncryptedCharField

from .constants import APPLICATIONS


class System(models.Model):
    name = models.CharField(max_length=50, unique=True, null=True)
    application = models.IntegerField(choices=APPLICATIONS)

    def __str__(self):
        return self.name


class Enviroment(models.Model):
    name = models.CharField(max_length=50, unique=True, null=True)

    def __str__(self):
        return self.name


class Instance(models.Model):
    system = models.ForeignKey(System, on_delete=models.PROTECT)
    environment = models.ForeignKey(Enviroment, on_delete=models.PROTECT)
    host = models.CharField(max_length=100)
    port = models.IntegerField()
    database_or_schema = models.CharField(max_length=100)
    login = models.CharField(max_length=100)
    password = EncryptedCharField(max_length=100)
    unique_together = ((system, environment),)
