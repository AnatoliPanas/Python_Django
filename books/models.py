from django.db import models

class AuthorBio(models.Model):
    link_site = models.URLField(max_length=250)
    biography = models.TextField(null=True, blank=True)
    date_of_birth = models.DateField(null=True, blank=True)
    created_att = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Author(models.Model):
    name = models.CharField(max_length=30)
    surname = models.CharField(max_length=30)
    bio = models.OneToOneField(
        AuthorBio,
        on_delete=models.PROTECT,
        null=True
    )

    def __str__(self):
        return f"{self.name[0]}. {self.surname}"


class Book(models.Model):
    GENRE_CHOICES = [
        ('Fantasy', 'Fantasy'),
        ('Science', 'Science'),
        ('Cooking', 'Cooking'),
        ('Business', 'Business'),
        ('Psychology', 'Psychology'),
        ('History', 'History'),
    ]

    title = models.CharField(max_length=140)
    rating = models.FloatField(default=0.0)
    genre = models.CharField(max_length=30, choices=GENRE_CHOICES)
    release_year = models.DateField()
    author = models.ForeignKey(Author, on_delete=models.CASCADE, null=True)
    pages = models.SmallIntegerField(null=True, blank=True)
    language = models.CharField(max_length=15, default="English")
    isbn = models.CharField(max_length=50)

    def __str__(self):
        return self.title