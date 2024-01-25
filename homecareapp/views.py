from django.shortcuts import render
from .models import *

# Create your views here.
def index(request):
    return render(request, "homecareapp/index.html")

def about(request):
    return render(request, "homecareapp/about.html")

def faq(request):
    template = 'homecareapp/faq.html'     
    faq_results = FAQ.objects.all;
     
    context = {
        'faq_results' : faq_results
    }    
    return render(request, template, context)            

def dashboard(request):
    return render(request, "homecareapp/dashboard.html")

def search(request):
    return render(request, "homecareapp/search.html")

def searchResults(request):
    return render(request, "homecareapp/searchResults.html")
                                