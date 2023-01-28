from django.shortcuts import render,HttpResponse
from home.models import Blog
import math

# Create your views here.
def index(request):
    return render(request,'index.html')

def blog(request):
    no_of_posts = 3
    page = request.GET.get('page')
    # print(page)
    if page is None:
        page = 1
    else:
        page = int(page)
    
    
    blogs = Blog.objects.all()[(page-1)*no_of_posts : page*no_of_posts]
    length = len(Blog.objects.all())
    # print(length)
    if page>1:
        prev = page-1
    else:
        prev = None

    if page<math.ceil(length/no_of_posts):
        nxt = page+1
    else :
        nxt = None

    context = {'blogs':blogs,'prev':prev,'nxt':nxt}
    return render(request,'bloghome.html',context)

def blogpost(request,slug):
    blog = Blog.objects.filter(slug=slug).first()
    context = {'blog':blog}
    return render(request,'blogpost.html',context)

def contact(request):
    return render(request,'contact.html')

def search(request):
    return render(request,'search.html')
