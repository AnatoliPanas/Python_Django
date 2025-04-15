from rest_framework import serializers

from task_manager.models import Task


class TaskCreateSerialize(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = [
            "title",
            "description",
            "categories",
            "deadline"
        ]

class TaskListSerialize(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = "__all__"

class TaskStatusCountSerializer(serializers.Serializer):
    status = serializers.CharField()
    id__count = serializers.IntegerField()