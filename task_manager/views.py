from django.db.models import Count, QuerySet
from django.http import HttpResponse
from django.utils import timezone
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework.views import APIView

from task_manager.models import Task, SubTask
from task_manager.serializers import (TaskCreateSerialize,
                                      TaskDetailSerializer,
                                      TaskStatusCountSerializer,
                                      SubTaskCreateSerializer, SubTaskSerializer)


# Задание 5: Создание классов представлений
# Создайте классы представлений для работы с подзадачами (SubTasks), включая создание, получение, обновление и удаление подзадач.
# Используйте классы представлений (APIView) для реализации этого функционала.
# Шаги для выполнения:
# Создайте классы представлений для создания и получения списка подзадач (SubTaskListCreateView).
# Создайте классы представлений для получения, обновления и удаления подзадач (SubTaskDetailUpdateDeleteView).
# Добавьте маршруты в файле urls.py, чтобы использовать эти классы.

class SubTaskListCreateAPIView(APIView):
    def get(self, request: Request) -> Response:
        subtasks: QuerySet[SubTask] = SubTask.objects.all()
        serializer = SubTaskSerializer(subtasks, many=True)
        return Response(
            data=serializer.data,
            status=status.HTTP_200_OK
        )

    def post(self, request: Request) -> Response:
        serializer = SubTaskCreateSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class SubTaskDetailUpdateDeleteView(APIView):
    def get(self, request: Request, **kwargs) -> Response:
        try:
            subtask = SubTask.objects.get(id=kwargs['subtask_id'])
        except SubTask.DoesNotExist:
            return Response(
                data={
                    "message": "Подзадача не найдена!"
                },
                status=status.HTTP_404_NOT_FOUND
            )
        serializer = SubTaskSerializer(subtask)

        return Response(
            data=serializer.data,
            status=status.HTTP_200_OK
        )

    def put(self, request: Request, **kwargs) -> Response:
        try:
            subtask = SubTask.objects.get(id=kwargs['subtask_id'])
        except SubTask.DoesNotExist:
            return Response(
                data={
                    "message": "Подзадача не найдена!"
                },
                status=status.HTTP_404_NOT_FOUND
            )

        serializer = SubTaskCreateSerializer(instance=subtask, data=request.data)

        if serializer.is_valid():
            serializer.save()

            return Response(
                data=serializer.data,
                status=status.HTTP_200_OK
            )

        else:
            return Response(
                data=serializer.errors,
                status=status.HTTP_400_BAD_REQUEST
            )

    def delete(self, request: Request, **kwargs) -> Response:
        try:
            subtask = SubTask.objects.get(id=kwargs['subtask_id'])
        except SubTask.DoesNotExist:
            return Response(
                data={
                    "message": "Подзадача не найдена!"
                },
                status=status.HTTP_404_NOT_FOUND
            )

        subtask.delete()

        return Response(
            data={
                "message": "Книга была успешно удалена."
            },
            status=status.HTTP_202_ACCEPTED
        )

def user_hello1(request):
    return HttpResponse(
        f"<h1>Hello, Prog2!!! :)</h1>"
    )


@api_view(['POST'])
def tasks_create(request: Request) -> Response:
    serializer = TaskCreateSerialize(data=request.data)

    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    else:
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def list_of_tasks(request) -> Response:
    tasks = Task.objects.all()
    serializer = TaskDetailSerializer(tasks, many=True)

    return Response(data=serializer.data, status=status.HTTP_200_OK)


@api_view(['GET'])
def get_task_by_id(request, task_id: int) -> Response:
    try:
        task = Task.objects.get(id=task_id)
    except Task.DoesNotExist:
        return Response(
            data={
                "message": "TASK NOT FOUND"
            },
            status=404
        )

    serializer = TaskDetailSerializer(task)

    return Response(
        data=serializer.data,
        status=200
    )


@api_view(['GET'])
def tasks_count(request) -> Response:
    tasks_cn = Task.objects.count()

    return Response(data=f"{tasks_cn=}", status=status.HTTP_200_OK)


@api_view(['GET'])
def tasks_count_by_status(request) -> Response:
    statuses_count_by_task = Task.objects.values("status").annotate(Count("id"))
    serializer = TaskStatusCountSerializer(statuses_count_by_task, many=True)
    return Response(data=serializer.data, status=status.HTTP_200_OK)


@api_view(['GET'])
def tasks_of_overdue(request) -> Response:
    count_of_overdue_task = Task.objects.filter(deadline__lt=timezone.now()).count()

    return Response(data=f"{count_of_overdue_task=}", status=status.HTTP_200_OK)
