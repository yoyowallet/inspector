from rest_framework import serializers

from . import models


class CheckGroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.CheckGroup
        fields = ("pk", "name", "description")


class DatacheckSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Datacheck
        fields = (
            "pk",
            "code",
            "description",
            "weight",
            "left_type",
            "left_logic",
            "relation",
            "right_logic",
            "supports_warning",
            "warning_relation",
            "warning_type",
            "warning_logic",
        )


class CheckRunSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.CheckRun
        fields = (
            "pk",
            "start_time",
            "end_time",
            "status",
            "result",
            "left_value",
            "right_value",
            "warning_value",
            "error_message",
            "created_at",
        )


class EnvironmentStatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.EnvironmentStatus
        fields = ("pk", "last_start_time", "last_end_time", "status", "result")


class CheckRunCreateSerializer(serializers.Serializer):
    check_code = serializers.CharField(max_length=20, required=True, allow_blank=False)
    environment = serializers.CharField(max_length=50, required=True, allow_blank=False)


class CheckGroupRunCreateSerializer(serializers.Serializer):
    checkgroup_name = serializers.CharField(
        max_length=100, required=True, allow_blank=False
    )
    environment = serializers.CharField(max_length=50, required=True, allow_blank=False)
