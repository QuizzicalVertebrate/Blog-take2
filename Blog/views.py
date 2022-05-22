from django.shortcuts import render
from django.views.generic import ListView, DetailView, DeleteView, CreateView
from .models import Post

# Create your views here.




class PostListView(ListView):
    model = Post
    template_name = 'Home.html'


class PostDetailView(DetailView):
    model = Post
    template_name = 'Post_detail.html'

#By default, DetailView will provide a context object we can use in our template called either object or the 
# lowercased name of our model, which would be post. Also, DetailView expects either a primary key or a slug 
# passed to it as the identifier.


