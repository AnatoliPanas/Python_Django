from rest_framework.pagination import CursorPagination


class CustomCursorPagination(CursorPagination):
    page_size = 2
    ordering = 'id'
