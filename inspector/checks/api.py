from rest_framework import viewsets, permissions

from . import models
from . import serializers


class CheckGroupViewSet(viewsets.ModelViewSet):
    """ViewSet for the CheckGroup class"""

    queryset = models.CheckGroup.objects.all()
    serializer_class = serializers.CheckGroupSerializer
    permission_classes = [permissions.IsAuthenticated]


class DatacheckViewSet(viewsets.ModelViewSet):
    """ViewSet for the Datacheck class"""

    queryset = models.Datacheck.objects.all()
    serializer_class = serializers.DatacheckSerializer
    permission_classes = [permissions.IsAuthenticated]


class CheckRunViewSet(viewsets.ModelViewSet):
    """ViewSet for the CheckRun class"""

    queryset = models.CheckRun.objects.all()
    serializer_class = serializers.CheckRunSerializer
    permission_classes = [permissions.IsAuthenticated]


class EnvironmentStatusViewSet(viewsets.ModelViewSet):
    """ViewSet for the EnvironmentStatus class"""

    queryset = models.EnvironmentStatus.objects.all()
    serializer_class = serializers.EnvironmentStatusSerializer
    permission_classes = [permissions.IsAuthenticated]
