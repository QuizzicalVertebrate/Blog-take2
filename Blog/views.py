from django.shortcuts import render
from django.views.generic import ListView, DetailView, DeleteView, CreateView, UpdateView

from django.contrib.auth import login, logout
from .models import Post
from django.urls import reverse_lazy

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

class PostNewView(CreateView):
    model = Post 
    template_name = 'new_post.html'
    fields = ['Title', 'Author', 'Body', 'Date']

class PostUpdateView(UpdateView):
    model = Post
    template_name = 'Update_Post.html'
    fields = ['Title', 'Body'] 

class PostDeleteView(DeleteView):
    model = Post
    template_name = 'Delete_Post.html'
    success_url = reverse_lazy('Home')


def Test(request):
    return render(request, 'Test.html')

#ust found this - there's an easier way to convert all of the href= to {% static %}. 
#pip install djangify
#navigate to directory with the html file.
#djangify -d

#You'll then get a new folder with the html files with all the references converted.

#16

#Ah you also then need to do a find and replace: [static '] with: [static 'website/] or [static 'appname/]. Works like a charm

