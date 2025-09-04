from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView

# Create your views here.

# def home(request):
#     return HttpResponse("<h1>Welcome to the Homepage</h1>")

class HomeView(TemplateView):
    template_name = "home.html"


# def about(request):
#     return HttpResponse("<h3>This is the about page</h3>")

class about(TemplateView):
    template_name = "about.html"



# def contact(request):
#     return HttpResponse("Contact Page")

class contact(TemplateView):
    template_name = "contact.html"



# def faq(request):
#     return HttpResponse("Frequently Ask Questions")

class faq(TemplateView):
    template_name = "faq.html"
