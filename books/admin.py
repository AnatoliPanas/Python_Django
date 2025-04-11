

from django.contrib import admin
from django.contrib.auth.models import Group
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.db.models import QuerySet
from django.utils import timezone
from django.utils.translation import gettext_lazy as _
from books.models import Book, Author, AuthorBio, User


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'release_year', 'genre')
    list_filter = ('rating', 'release_year', 'language')
    search_fields = ('title', 'author__surname')
    list_per_page = 10
    actions = ['update_release_year']



    def update_release_year(self, request, objects: QuerySet) -> None:
        for obj in objects:
            obj.release_year = timezone.now()

            obj.save()

        self.message_user(request, f"Год выпуска обновлен для {objects.count()} книги(книг).")

    update_release_year.short_description = "Обновить дату релиза"

@admin.register(User)
class UserAdmin(BaseUserAdmin):
    fieldsets = (
        (None, {'fields': ('username', 'password', 'role')}),
        (_('Personal info'), {'fields': ('first_name', 'last_name', 'email', 'phone', 'birth_day')}),
        (_('Permissions'), {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
        (_('Important dates'), {'fields': ('last_login', 'date_joined')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'password1', 'password2'),
        }),
    )
    list_display = ('username', 'email', 'first_name', 'last_name', 'is_staff', 'role')
    search_fields = ('username', 'first_name', 'last_name', 'email')
    ordering = ('username',)

# class BookAdmin(admin.ModelAdmin):
#     list_display = ('title', 'author', 'release_year', 'genre')
#     list_filter = ('rating', 'release_year', 'language')
#     search_fields = ('title', 'author__surname')
#     list_per_page = 2

class AuthorInline(admin.TabularInline):
    model = Author
    extra = 1

@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    pass

@admin.register(AuthorBio)
class AuthorBioAdmin(admin.ModelAdmin):
    inlines = [AuthorInline]
    list_display = ('author_fullname', 'date_of_birth', 'short_bio')

    def short_bio(self, obj: AuthorBio) -> str:
        return f"{obj.biography[:30]}..."

    def author_fullname(self, obj: AuthorBio) -> str:
        return f"{obj.author.name[0]}. {obj.author.surname}"



admin.site.unregister(Group)
admin.site.register(Group)
# admin.site.register(Book, BookAdmin)
# admin.site.register(Author)
# admin.site.register(AuthorBio)
