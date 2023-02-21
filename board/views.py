<<<<<<< HEAD
from django.shortcuts import render

# Create your views here.
=======
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from .models import Post

# Create your views here.
class PostList(ListView):
    model = Post
    ordering = '-pk' # 최신데이터를 가장 마지막에 꺼내오는 속성
    template_name = 'blog/index.html'

class PostDetail(DetailView):
    model = Post
>>>>>>> ffa52d4a9521118ceee6cf9ce2a372a58f5bf6c7
