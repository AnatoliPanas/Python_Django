from django.db import models
from task_manager.models import Task


class SubTask(models.Model):
    STATUS_CHOICES = [
        ("New", "New"),
        ("In Progress", "In Progress"),
        ("Pending", "Pending"),
        ("Blocked", "Blocked"),
        ("Done", "Done")
    ]

    title = models.CharField(max_length=50)
    description = models.TextField()
    task = models.ForeignKey(Task, on_delete=models.CASCADE)
    status = models.CharField(max_length=100, choices=STATUS_CHOICES)
    deadline = models.DateTimeField()
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = "task_manager_subtask"
        ordering= ("-created_at",)
        verbose_name = "SubTask"
        unique_together = ("title",)

    def __str__(self):
        return self.title