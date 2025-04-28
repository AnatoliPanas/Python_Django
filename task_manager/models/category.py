from django.db import models
from django.utils import timezone

from task_manager.managers.category import SoftDeleteManager


class Category(models.Model):
    name = models.CharField(max_length=100)
    is_deleted = models.BooleanField(default=False)
    deleted_at = models.DateTimeField(null=True, blank=True)

    objects = SoftDeleteManager()

    def delete(self, *arg, **kwargs):
        self.is_deleted = True
        self.deleted_at = timezone.now()

        self.save()

    def __str__(self):
        return self.name

    class Meta:
        db_table = "task_manager_category"
        verbose_name = "Category"
        unique_together = ("name",)


