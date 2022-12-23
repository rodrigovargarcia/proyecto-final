from django.shortcuts import render
from django.views.generic import DetailView, ListView, CreateView, UpdateView, DeleteView
from blog_app.models import Post
from django.urls import reverse_lazy

def index(request):
    return render(request, "blog_app/index.html", {})

class PostDetalle(DetailView):
    model = Post

class PostListar(ListView):
    model = Post  

class PostCrear(CreateView):
    model = Post
    success_url = reverse_lazy("blog-app-listar")
    fields = '__all__'


class PostBorrar(DeleteView):
    model = Post
    success_url = reverse_lazy("blog-app-listar")

class PostActualizar(UpdateView):
    model = Post
    success_url = reverse_lazy("blog-app-listar")
    fields = "__all__"