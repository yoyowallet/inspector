from rest_framework import viewsets, permissions, authentication, status
from rest_framework.generics import CreateAPIView
from rest_framework.response import Response

from . import models
from . import serializers
from .service import CheckRunService


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


class RunCheck(CreateAPIView):
    authentication_classes = (authentication.TokenAuthentication,
                              authentication.SessionAuthentication)
    permission_classes = (permissions.IsAdminUser,)
    serializer_class = serializers.CheckRunCreateSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        try:
            checkrun_id = CheckRunService.create_check_run_api(
                serializer['check_code'].value,
                serializer['environment'].value,
                request.user)
        except (models.Datacheck.DoesNotExist,
                models.Environment.DoesNotExist) as exc:
            return Response(str(exc), status=400)

        return Response({'checkrun_id': checkrun_id}, status=status.HTTP_200_OK)


class RunCheckGroup(CreateAPIView):
    authentication_classes = (authentication.TokenAuthentication,
                              authentication.SessionAuthentication)
    permission_classes = (permissions.IsAdminUser,)
    serializer_class = serializers.CheckGroupRunCreateSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        try:
            CheckRunService.run_check_group_api(
                serializer['checkgroup_name'].value,
                serializer['environment'].value,
                request.user)
        except (models.CheckGroup.DoesNotExist,
                models.Environment.DoesNotExist) as exc:
            return Response(str(exc), status=400)

        return Response({serializer['checkgroup_name'].value: 'success'},
                        status=status.HTTP_200_OK)
