from django.shortcuts import render
from .models import Design
# Create your views here.

def index(request):
    designs = Design.objects.all()
    cpage = 'Home'
    return render(request,'index.html',{'designs': designs, 'cpage': cpage })

def contact(request):
    cpage = 'Contact'
    return render(request,'contact.html',{'cpage': cpage })

def about(request):
    cpage = 'About'
    return render(request,'about.html',{'cpage': cpage })

