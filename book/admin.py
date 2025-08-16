from django.contrib import admin

from .models import Book, Author, BookAuthor, BookReview


class BookAdmin(admin.ModelAdmin):
    search_fields = ('title', 'isbn',)
    fields = ('title', 'description', 'isbn',)
    list_display = ('title', 'isbn',)


class AuthorAdmin(admin.ModelAdmin):
    search_fields = ('first_name',)
    list_display = ('first_name', 'last_name', 'email')


class BookAuthorAdmin(admin.ModelAdmin):
    list_display = ('book', 'author')


class BookReviewAdmin(admin.ModelAdmin):
    list_display = ('user', 'book', 'stars_given',)


admin.site.register(Book, BookAdmin)
admin.site.register(Author, AuthorAdmin)
admin.site.register(BookAuthor, BookAuthorAdmin)
admin.site.register(BookReview, BookReviewAdmin)
