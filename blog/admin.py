from django.contrib import admin

from .models import BlogPosts, Book, BookData, Author

admin.site.register(BlogPosts)
admin.site.register(Book)
admin.site.register(BookData)
admin.site.register(Author)

