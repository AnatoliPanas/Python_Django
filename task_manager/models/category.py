from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=100)

    class Meta:
        db_table = "task_manager_category"
        verbose_name = "Category"
        unique_together = ("name",)

    def __str__(self):
        return self.name