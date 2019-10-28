from . import models

from rest_framework import serializers


class SystemSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.System
        fields = ("pk", "name", "application")


class EnvironmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Environment
        fields = ("pk", "name")


class InstanceSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Instance
        fields = ("pk", "host", "port", "database_or_schema", "login", "password")
