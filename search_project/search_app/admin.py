from django.contrib import admin

from .models import Book, Review, Like

admin.site.register(Book)
admin.site.register(Review)
admin.site.register(Like)
