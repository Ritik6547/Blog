from django.shortcuts import render,HttpResponse
from home.models import Blog

# Create your views here.
def index(request):
    return render(request,'index.html')

def blog(request):
    blogs = Blog.objects.all()
    context = {'blogs':blogs}
    return render(request,'bloghome.html',context)

def blogpost(request,slug):
    blog = Blog.objects.filter(slug=slug).first()
    context = {'blog':blog}
    return render(request,'blogpost.html',context)

def contact(request):
    return render(request,'contact.html')

def search(request):
    return render(request,'search.html')