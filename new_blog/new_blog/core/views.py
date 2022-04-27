import re
from django.http.response import Http404, JsonResponse
from django.shortcuts import redirect, render
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

from core.models import Post


# Create your views here.

def login_user(request):
    return render(request, 'login.html')

def logout_user(request):
    logout(request)
    return redirect('/')

def create_posts(request):
    return render(request, "posts.html")

def submit_login(request):
    if request.POST:
        username = request.POST.get('username')
        password = request.POST.get('password')
        usuario = authenticate(username=username, password=password)
        if usuario is not None:
            login(request, usuario)
            return redirect('/')
        else:
            messages.error(request, "Invalid username or password")
    return redirect('/')

@login_required(login_url='/login/')
def home(request):
    return render(request, "home.html")

@login_required(login_url='/login/')
def list_post(request):
    usuario = request.user
    post = Post.objects.filter(usuario=usuario)
    
    dados = {'posts':post}
    return render(request, "home.html", dados)
    
@login_required(login_url="/login/")
def submit_post(request):
    if request.POST:
        title = request.POST.get('title')
        text = request.POST.get('text')
        author = request.POST.get("author")
        usuario = request.user
        id_post = request.POST.get('id_post')
    if id_post:
        post = Post.objects.get(id=id_post)
        if post.usuario == usuario:
            post.title = title 
            post.text = text
            post.author = author
            post.save()
        Post.objects.filter(id=id_post).update(title=title,
                                               text=text,
                                               author=author)
    else:
        Post.objects.create(title=title,
                            text=text,
                            author=author,
                            usuario = usuario)
    return redirect("/")
        

@login_required(login_url= "/login/")
def delete_post(request, id_post):
    usuario = request.user
    try:
        post = Post.objects.get(id=id_post)
    except Exception:
        raise Http404()
    if usuario == post.usuario:
        post.delete()
    else:
        raise Http404()
    return redirect('/')


def json_list_post(request, id_usuario):
    usuario = User.objects.get(id=id_usuario)
    post = Post.objects.filter(usuario=usuario).values('id', 'title', 'slug', 'author', 'text',
                                                       'published', 'data_creation', 'changed', 'usuario',
                                                        'up_image', 'status' )
    return JsonResponse(list(post), safe=False)