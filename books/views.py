from django.core.serializers import serialize
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.decorators import api_view
from books.serializers import BookListSerializer, BookDetailSerializer, BookCreateSerializer
from books.models import Book


@api_view(['GET'])
def list_of_books_(request) -> Response:
    return Response(
        data={
            "message": "Hello, World"
        },
        status=200
    )


@api_view(['GET'])
def list_of_books(request) -> Response:
    books = Book.objects.all()
    serializer = BookListSerializer(books, many=True)

    return Response(
        data=serializer.data,
        status=200
    )


@api_view(['GET'])
def get_book_detail(request, book_id: int) -> Response:
    try:
        book = Book.objects.get(id=book_id)
    except Book.DoesNotExist:
        return Response(
            data={
                "message": "BOOK NOT FOUND"
            },
            status=404
        )

    serializer = BookDetailSerializer(book)

    return Response(
        data=serializer.data,
        status=200
    )

@api_view(['POST'])
def create_book(request: Request):
    row_data = request.data
    serializer = BookCreateSerializer(data=row_data)
    if serializer.is_valid():
        serializer.save()
        return Response(
            data=serializer.data,
            status=201
        )
    else:
        return Response(
            data=serializer.errors,
            status=400
        )
