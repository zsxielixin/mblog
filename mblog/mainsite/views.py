from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from .models import Post
from datetime import datetime
from django.template.loader import get_template
from django.shortcuts import redirect

def index(request):
    return HttpResponse('this is my mblog')

def homepage(request):
    posts = Post.objects.all()
    post_lists = list()
    for count ,post in enumerate(posts):
        post_lists.append("No.{}:".format(str(count))+':'+str(post)+"<br>")
        post_lists.append("<small>"+str(post.body)+"</small><br><br>")
    return HttpResponse(post_lists)

def homepage1(request):
    template= get_template('index.html')
    posts = Post.objects.all()
    now = datetime.now()
    html = template.render(locals())
    return HttpResponse(html)

def showpost(request,slug):
    template= get_template('post.html')
    try:
        post=Post.objects.get(slug=slug)
        if post != None:
            html=template.render(locals())
            return HttpResponse(html)

    except:
        return redirect('/')