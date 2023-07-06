from django.contrib import admin
from .models import Books

# Register your models here.
class BooksView(admin.ModelAdmin):
    list_display = ('id', 'name', 'author', 'pages', 'publish_date', 'quantity')

admin.site.register(Books, BooksView)