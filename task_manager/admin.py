from django.contrib import admin
from task_manager.models import Task, SubTask, Category

@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'categories__name', 'deadline', 'status')
    list_filter = ('title', 'categories__name', 'deadline', 'status')
    list_per_page = 5

# admin.site.register(Task)
admin.site.register(SubTask)
admin.site.register(Category)
