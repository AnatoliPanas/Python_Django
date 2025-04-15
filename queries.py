import os
from enum import global_enum_repr

import django
from django.template.defaultfilters import title
from django.db.models import Count, Avg, Min, Subquery, OuterRef, ExpressionWrapper, F, fields, Q
from django.utils import timezone



os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'test_proj.settings')
django.setup()

from books.models import Book
from books.serializers import BookSerializer

# books = Book.objects.filter(
#     (Q(genre="Fantasy") | Q(rating__lte=6)) & ~Q(release_year="2009-03-20")
# )
#
# print(books)

#
# all_books = Book.objects.all() # select * from book;
# sql_query = "SELECT * FROM book"
# all_books1 = Book.objects.raw(sql_query)
# print(all_books1)
# # for book in all_books1:
# #     print(book.title, book.author)
#
# print(all_books.query)
# print(all_books)
#
# books_count = Book.objects.count()
# books_count_exists = Book.objects.exists()
# print(books_count)
# print(books_count_exists)
#
# books = Book.objects.values('title', 'rating').all()
# print(books)
#
# book = Book.objects.get(title="Django Test ORM Query Result1")
# print(book)

# ========Insert=========
# from datetime import datetime
#
# book = Book.objects.create(
#     title = "Django Test ORM Query Result",
#     rating = 5.98,
#     genre = "Fiction",
#     release_year = datetime.strptime("2005-07-09", "%Y-%m-%d"),
#     isbn = "1234-4342-4564-5675"
# )
#
# print("Книга создана")
#
# new_book = Book(
#     title = "Django Test ORM Query Result1",
#     rating = 5.98,
#     genre = "Fiction",
#     release_year = datetime.strptime("2005-07-09", "%Y-%m-%d"),
#     isbn = "1234-4342-4564-5675"
# )
#
# new_book.pages = 433
#
# new_book.save()

# ========Update=========
# book = Book.objects.get(id = 152)
# book.pages = 293
# book.save()

# ----------
# Book.objects.filter(genre = "Busines").update(
#     range = 8.88
# )

# Book.objects.update(price = 22.45)

# -----------
# from django.db.models import F
#
# # Book.objects.filter(id__in=[1, 2, 3]).update(rating=F('rating')-1)
#
# Book.objects.update(
#     discounted_price=F('price') * 0.8)

# ========Delete=========
# Book.objects.get(title="Django Test ORM Query Result1").delete()
# deleted, _ = Book.objects.filter(rating=1.1).delete()
# print(f"Удалено {deleted} записей -> {_}")
# =======================
# ========Agregate=========


result = Book.objects.aggregate(
    total_books=Count('id'),
    avg_price=Avg('price')
)

# print(f"Общее количество книг = {result['total_books']}")
# print(f"Средня цена = {result['avg_price']}")
# =======================
print('-' * 50)
author_books = Book.objects.values('author').annotate(
    books_count=Count('id')
)

# print(author_books.query)
# print(author_books)
# =======================
print('-' * 50)
sorted_books = Book.objects.order_by("-title")
# print(sorted_books.query)
# for book in sorted_books:
#     print(book.id, book.title)
# =======================
print('-' * 50)

sorted_books2 = Book.objects.order_by(
    "author__name",
    "title"
)

# print(sorted_books2.query)
# for book in sorted_books2:
#     print(book.author, book.title)

# ========Limit=========
books = Book.objects.all()[:5]
# print(books.query)
# for book in books:
#     print(book.id, book.title)

# ========Подзапросы=========

avg_price_subq = Book.objects.aggregate(avg_price=Avg('price'))['avg_price']
filtered_books = Book.objects.filter(
    price__lte=avg_price_subq
)

# print(filtered_books.query)

# =======================
print('-' * 50)

subquery = (Book.objects.filter(author=OuterRef('author'))
            .values('author')
            .annotate(min_price=Min('price'))
            .values('min_price'))

main_query = Book.objects.annotate(min_price_by_author=Subquery(subquery))

# print(main_query.query)

# =======================
print('-' * 50)

data = Book.objects.annotate(
    comission_price = ExpressionWrapper(
        expression=F('price') * 1.18,
        output_field=fields.FloatField()
    )
)
# print(data.query)
# print(data)


# =======================
print('-' * 50)

data = {
    "title": "TEST TITLE",
    "rating": 10.00,
    "pages": 255,
    "release_year": timezone.now().date(),
}

book_serializer = BookSerializer(data=data)
book_serializer.is_valid()
print(book_serializer.errors)
print(book_serializer.validated_data)