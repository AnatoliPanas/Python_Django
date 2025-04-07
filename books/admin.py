from django.contrib import admin
from django.contrib.auth.models import Group
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.utils.translation import gettext_lazy as _
from books.models import Book, Author, AuthorBio, User


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'release_year', 'genre')
    list_filter = ('rating', 'release_year', 'language')
    search_fields = ('title', 'author__surname')
    list_per_page = 2

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

admin.site.unregister(Group)
admin.site.register(Group)
# admin.site.register(Book, BookAdmin)
admin.site.register(Author)
admin.site.register(AuthorBio)
