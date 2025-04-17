from django.db import models

from task_manager.models import Category


class Task(models.Model):
    STATUS_CHOICES = [
        ("New", "New"),
        ("In Progress", "In Progress"),
        ("Pending", "Pending"),
        ("Blocked", "Blocked"),
        ("Done", "Done")
    ]

    title = models.CharField(max_length=50, unique_for_date="deadline")
    description = models.TextField()
    categories = models.ManyToManyField(Category)
    status = models.CharField(max_length=100, choices=STATUS_CHOICES, default="New")
    deadline = models.DateTimeField()
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = "task_manager_task"
        verbose_name = "Task"
        ordering = ("-created_at",)
        unique_together = ("title",)

    def __str__(self):
        return self.title