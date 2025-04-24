"""
URL configuration for test_proj project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from books.views import BooksListCreateView, BookDetailUpdateDeleteView
from first_app.views import django_greetings, user_greetings, index_page, user_hello
from task_manager.views import user_hello1, get_task_by_id, tasks_count, \
    tasks_count_by_status, tasks_of_overdue, SubTaskListCreateAPIView, SubTaskDetailUpdateDeleteView, \
    TaskListCreateAPIView

urlpatterns = [
    path('index_page/', index_page),
    path('admin/', admin.site.urls),
    path('greetings/', django_greetings),
    path('greetings-f-str/<str:name>/', user_greetings),
    path('greetings-f-str/', user_greetings, name='default_user_greetings'),
    path('hello/<str:name>/', user_hello),
    path('hello1/', user_hello1),

    path('books/', BooksListCreateView.as_view()),
    # path('books/<int:book_id>/', BookDetailUpdateDeleteView.as_view()),
    path('books/<str:target_title>/', BookDetailUpdateDeleteView.as_view()),


    path('tasks/', TaskListCreateAPIView.as_view()),
    path('tasks/<int:task_id>', get_task_by_id),
    path('tasks/count', tasks_count),
    path('tasks/status_count', tasks_count_by_status),
    path('tasks/tasks_of_overdue', tasks_of_overdue),

    path('subtasks/', SubTaskListCreateAPIView.as_view()),
    path('subtasks/<int:subtask_id>', SubTaskDetailUpdateDeleteView.as_view()),


]
