from django.shortcuts import render
from django.http import HttpResponse
from .models import BlogPosts, Book
from django.views import View



def blog_list(request):
    # Fetch all blogs and their related authors
    blogs = BlogPosts.objects.select_related('author').all()
    
    context = ""
    
    # Iterate over the blogs
    for blog in blogs:
        
        context += f"<li>{blog.title} - {blog.author.first_name}</li>"  # No additional queries executed
    return HttpResponse(f"<h2>All Blog Posts</h2></br><ul>{context}</ul>")


# def blog_list(request, BlogPosts):
#     # Fetch all blogs
#     blogs = BlogPosts.objects.all()
    
#     context = ""
    
#     # Iterate over the blogs
#     for blog in blogs:
        
#         # Performs another query in order to retrieve dat from the Author model
#         author = blog.author  # Lazy loading
        
#         context += f"<li>{blog.title} - {author}</li>"
#     return HttpResponse(f"<h2>All Blog Posts</h2></br><ul>{context}</ul>")

def blog_detail(request, blog_id):
    blog =  BlogPosts.objects.get(pk=blog_id)
    content = blog.body
    return HttpResponse(content)

class BooksView(View):
    
    def get(self, request):
        books = Book.objects.select_related('author').all()
        return render(request, "books.html", {"books" : books}) #the third will define the content of the html file    
    