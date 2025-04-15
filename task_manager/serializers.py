from rest_framework import serializers

from task_manager.models import Task


class TaskListSerialize(serializers.ModelSerializer):
    class Meta:
        model = Task,
        fields = [
            'title',
            'description',
            'categories',
            'status',
            'deadline',
        ]
