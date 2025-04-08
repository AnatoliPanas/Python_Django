import os
from enum import global_enum_repr

import django
from django.template.defaultfilters import title

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'test_proj.settings')
django.setup()


from books.models import Book


all_books = Book.objects.all() # select * from book;
sql_query = "SELECT * FROM book"
all_books1 = Book.objects.raw(sql_query)
print(all_books1)
# for book in all_books1:
#     print(book.title, book.author)

print(all_books.query)
print(all_books)

books_count = Book.objects.count()
books_count_exists = Book.objects.exists()
print(books_count)
print(books_count_exists)

books = Book.objects.values('title', 'rating').all()
print(books)

book = Book.objects.get(title="Django Test ORM Query Result1")
print(book)

#========Insert=========
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