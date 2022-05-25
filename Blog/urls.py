from django.urls import path
from . import views
from .views import (PostListView, PostDetailView, PostNewView, 
                    PostUpdateView,PostDeleteView, Test)




urlpatterns = [
    path('',PostListView.as_view(), name = 'Base'),
    path('home/',PostListView.as_view(), name = 'Home'),
    path('post/<int:pk>/',PostDetailView.as_view(), name = 'Post_Detail'),
    path('post/new',PostNewView.as_view(), name = 'Post_New'),
    path('test/',views.Test, name = 'Test'),
    path('post/<int:pk>/update',PostUpdateView.as_view(), name = 'post_update'),
#seems the name must match the route for it to work down to the casing. No idea why
    path('post/<int:pk>/delete',PostDeleteView.as_view(), name = 'post_delete'),
    


    
]
