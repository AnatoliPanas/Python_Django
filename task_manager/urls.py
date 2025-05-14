from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from task_manager.views import (tasks_count,
                                tasks_count_by_status,
                                tasks_of_overdue,
                                SubTaskListCreateView,
                                SubTaskDetailUpdateDeleteView,
                                TaskListCreateView,
                                TaskDetailUpdateDeleteView,
                                CategoryViewSet)

router = DefaultRouter()

router.register('categories', CategoryViewSet)

urlpatterns = [
    path('tasks/', TaskListCreateView.as_view()),
    path('tasks/<int:task_id>', TaskDetailUpdateDeleteView.as_view()),

    path('tasks/count', tasks_count),
    path('tasks/status_count', tasks_count_by_status),
    path('tasks/tasks_of_overdue', tasks_of_overdue),

    path('subtasks/', SubTaskListCreateView.as_view()),
    path('subtasks/<int:subtask_id>', SubTaskDetailUpdateDeleteView.as_view()),
    path('', include(router.urls)),
    path('auth-login-jwt/', TokenObtainPairView.as_view()),
    path('token_refresh/', TokenRefreshView.as_view()),

]
