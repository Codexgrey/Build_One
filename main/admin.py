from django.contrib import admin
from .models import Book, Student

# Register your models here.
@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    # list_per_page = 2
    # list_editable = ['isbn']
    list_display = ['id', 'title', 'author']
    list_filter = ['date']
    search_fields = ['title', 'body', 'author', 'isbn']


@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ['name', 'cohort']
    search_fields = ['name', 'cohort', 'gender']