from . import models
from . import serializers
from rest_framework import viewsets, permissions


class SystemViewSet(viewsets.ModelViewSet):
    """ViewSet for the System class"""

    queryset = models.System.objects.all()
    serializer_class = serializers.SystemSerializer
    permission_classes = [permissions.DjangoModelPermissions]


class EnvironmentViewSet(viewsets.ModelViewSet):
    """ViewSet for the Environment class"""

    queryset = models.Environment.objects.all()
    serializer_class = serializers.EnvironmentSerializer
    permission_classes = [permissions.DjangoModelPermissions]


class InstanceViewSet(viewsets.ModelViewSet):
    """ViewSet for the Instance class"""

    queryset = models.Instance.objects.all()
    serializer_class = serializers.InstanceSerializer
    permission_classes = [permissions.DjangoModelPermissions]
