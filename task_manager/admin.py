from django.contrib import admin
from django.db.models import QuerySet

from task_manager.models import Task, SubTask, Category

class SubTaskInline(admin.StackedInline):
    model = SubTask
    extra = 1

@admin.register(SubTask)
class SubTaskAdmin(admin.ModelAdmin):
    actions = ['set_subtask_status_in_done',]
    list_display = ('task__title', 'title', 'description', 'deadline', 'status')

    def set_subtask_status_in_done(self, request, objs: QuerySet) -> None:
        for obj in objs:
            obj.status = "Done"
            obj.save()
        self.message_user(request, f"Статус обновлен для {objs.count()} подзадачь.")

    set_subtask_status_in_done.short_description = "Обновить статусы на Done"

@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    inlines = [SubTaskInline]
    list_display = ('short_title', 'description', 'categories__name', 'deadline', 'status')
    list_filter = ('title', 'categories__name', 'deadline', 'status')
    list_per_page = 5

    def short_title(self, obj: Task) -> str:
        return f"{obj.title[:10]}..."

# admin.site.register(Task)
# admin.site.register(SubTask)
admin.site.register(Category)
