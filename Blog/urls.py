from django.urls import path
from .views import (PostListView, PostDetailView)




urlpatterns = [
    path('',PostListView.as_view(), name = 'Base'),
    path('home/',PostListView.as_view(), name = 'Home'),
    path('post/<int:pk>/',PostDetailView.as_view(), name = 'Post_detail'),
    
]
