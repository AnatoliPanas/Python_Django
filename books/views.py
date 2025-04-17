from idlelib.rpc import request_queue

from django.db.models import QuerySet
from rest_framework import status
from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework.pagination import PageNumberPagination

from books.serializers import BookListSerializer, BookDetailSerializer, BookCreateSerializer
from books.models import Book


# @api_view(['GET'])
# def list_of_books(request) -> Response:
#     books = Book.objects.all()  # Queryset[<Book obj1>, ..., <Book obj150>]
#
#     serializer = BookListSerializer(books, many=True)
#
#     return Response(
#         data=serializer.data,
#         status=200
#     )

class BooksListCreateAPIView(APIView, PageNumberPagination):
    page_size = 5

    def get_queryset(self, request: Request):
        allowed_sort_field = {'rating', 'price', 'release_year'}
        queryset: QuerySet[Book] = Book.objects.all()  # Queryset[<Book obj1>, ..., <Book obj150>]

        # Filter Params
        authors = request.query_params.getlist('author')
        year = request.query_params.get('year')

        # Sort Params
        sort_by = request.query_params.get('sort_by', 'rating')
        sort_order = request.query_params.get('order', 'asc')

        if authors:
            queryset = queryset.filter(author__surname__in=authors)

        if year:
            try:
                year = int(year)
                queryset = queryset.filter(release_year__year=year)
            except ValueError:
                queryset = queryset.none()

        if sort_by not in allowed_sort_field:
            sort_by = 'rating'

        if sort_order == 'desc':
            sort_by = f"-{sort_by}"

        queryset = queryset.order_by(sort_by)

        return queryset

    def get_page_size(self, request: Request):
        page_size = request.query_params.get('page_size')

        if page_size and page_size.isdigit():
            return int(page_size)
        return self.page_size

    def get(self, request: Request) -> Response:
        books = self.get_queryset(request=request)
        # serializer = BookListSerializer(books, many=True)
        # return Response(
        #     data=serializer.data,
        #     status=status.HTTP_200_OK
        # )

        results = self.paginate_queryset(queryset=books, request=request, view=self)

        serializer = BookListSerializer(results, many=True)

        return self.get_paginated_response(data=serializer.data)


    def post(self, request: Request) -> Response:
        serializer = BookCreateSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class BookDetailUpdateDeleteAPIView(APIView):
    def get(self, request: Request, **kwargs) -> Response:
        try:
            book = Book.objects.get(id=kwargs['book_id'])
        except Book.DoesNotExist:
            return Response(
                data={
                    "message": "BOOK NOT FOUND"
                },
                status=status.HTTP_404_NOT_FOUND
            )
        serializer = BookDetailSerializer(book)

        return Response(
            data=serializer.data,
            status=status.HTTP_200_OK
        )

    def put(self, request: Request, **kwargs) -> Response:
        try:
            book = Book.objects.get(id=kwargs['book_id'])
        except Book.DoesNotExist:
            return Response(
                data={
                    "message": "Book not found"
                },
                status=status.HTTP_404_NOT_FOUND
            )

        serializer = BookCreateSerializer(instance=book, data=request.data)

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
            book = Book.objects.get(id=kwargs['book_id'])
        except Book.DoesNotExist:
            return Response(
                data={
                    "message": "Book not found"
                },
                status=status.HTTP_404_NOT_FOUND
            )

        book.delete()

        return Response(
            data={
                "message": "Book was deleted successfully."
            },
            status=status.HTTP_202_ACCEPTED
        )

# @api_view(['GET', 'POST'])
# def book_list_create(request) -> Response | None:
#     if request.method == "GET":
#         books = Book.objects.all()  # Queryset[<Book obj1>, ..., <Book obj150>]
#         serializer = BookListSerializer(books, many=True)
#         return Response(
#             data=serializer.data,
#             status=200
#         )
#     elif request.method == "POST":
#         serializer = BookCreateSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         else:
#             return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#     return None


# @api_view(['GET', 'PUT', 'DELETE'])
# def book_detail_update_delete(request, book_id: int) -> Response | None:
#     if request.method == "GET":
#         try:
#             book = Book.objects.get(id=book_id)
#         except Book.DoesNotExist:
#             return Response(
#                 data={
#                     "message": "BOOK NOT FOUND"
#                 },
#                 status=404
#             )
#         serializer = BookDetailSerializer(book)
#
#         return Response(
#             data=serializer.data,
#             status=200
#         )
#
#     elif request.method == "PUT":
#         try:
#             book = Book.objects.get(id=book_id)
#         except Book.DoesNotExist:
#             return Response(
#                 data={
#                     "message": "Book not found"
#                 },
#                 status=404
#             )
#
#         serializer = BookCreateSerializer(instance=book, data=request.data)
#
#         if serializer.is_valid():
#             serializer.save()
#
#             return Response(
#                 data=serializer.data,
#                 status=200
#             )
#
#         else:
#             return Response(
#                 data=serializer.errors,
#                 status=400
#             )
#     elif request.method == "DELETE":
#         try:
#             book = Book.objects.get(id=book_id)
#         except Book.DoesNotExist:
#             return Response(
#                 data={
#                     "message": "Book not found"
#                 },
#                 status=404
#             )
#
#         book.delete()
#
#         return Response(
#             data={
#                 "message": "Book was deleted successfully."
#             },
#             status=204
#         )
#     return None

# @api_view(['POST'])
# def book_create(request):
#     serializer = BookCreateSerializer(data=request.data)
#
#     if serializer.is_valid():
#         serializer.save()
#         return Response(serializer.data, status=status.HTTP_201_CREATED)
#     else:
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# @api_view(['PUT'])
# def update_book(request, book_id: int) -> Response:
#     try:
#         book = Book.objects.get(id=book_id)
#     except Book.DoesNotExist:
#         return Response(
#             data={
#                 "message": "Book not found"
#             },
#             status=404
#         )
#
#     serializer = BookCreateSerializer(instance=book, data=request.data)
#
#     if serializer.is_valid():
#         serializer.save()
#
#         return Response(
#             data=serializer.data,
#             status=200
#         )
#
#     else:
#         return Response(
#             data=serializer.errors,
#             status=400
#         )


# @api_view(['DELETE'])
# def delete_book(request, book_id: int) -> Response:
#     try:
#         book = Book.objects.get(id=book_id)
#     except Book.DoesNotExist:
#         return Response(
#             data={
#                 "message": "Book not found"
#             },
#             status=404
#         )
#
#     book.delete()
#
#     return Response(
#         data={
#             "message": "Book was deleted successfully."
#         },
#         status=204
#     )
