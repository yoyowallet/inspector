from django.db import models
from django.urls import reverse
from encrypted_model_fields.fields import EncryptedCharField

from .constants import APPLICATIONS


class System(models.Model):
    name = models.CharField(max_length=50, unique=True, null=True)
    application = models.IntegerField(choices=APPLICATIONS)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ("-pk",)

    def __unicode__(self):
        return "%s" % self.pk

    def get_url(self, action):
        return reverse(f"systems_system_{action}", args=(self.pk,))

    def get_name(self):
        return self.name


class Environment(models.Model):
    name = models.CharField(max_length=50, unique=True, null=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ("-pk",)

    def __unicode__(self):
        return "%s" % self.pk

    def get_url(self, action):
        return reverse(f"systems_environment_{action}", args=(self.pk,))

    def get_name(self):
        return self.name


class Instance(models.Model):
    system = models.ForeignKey(System, on_delete=models.PROTECT)
    environment = models.ForeignKey(Environment, on_delete=models.PROTECT)
    host = models.CharField(max_length=100, null=True, blank=True)
    port = models.IntegerField(null=True, blank=True)
    db = models.CharField(max_length=100, null=True, blank=True)
    schema = models.CharField(max_length=100, null=True, blank=True)
    login = models.CharField(max_length=100, null=True, blank=True)
    password = EncryptedCharField(max_length=100, null=True, blank=True)
    extra_json = models.TextField(null=True, blank=True)
    unique_together = ((system, environment),)

    class Meta:
        ordering = ("-pk",)

    def __unicode__(self):
        return "%s" % self.pk

    def get_url(self, action):
        return reverse(f"systems_instance_{action}", args=(self.pk,))

    def get_absolute_url(self):
        self.get_url("update")

    def get_name(self):
        return f"{self.system.name} / {self.environment.name} "
