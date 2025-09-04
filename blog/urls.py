from django.urls import path, include
from . import views

app_name = "blog"

urlpatterns = [
    
    path("", views.blog_list, name="blog-list"),
    path("<int:blog_id>/", views.blog_detail, name="blog-detail"),
    path("books/", views.BooksView.as_view(), name="Books-list")
]