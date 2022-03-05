from django.urls import path
from .import views
from .models import Post
from django.views.generic import ListView, DetailView
urlpatterns = [
   
   path('', ListView.as_view(
      queryset = Post.objects.all().order_by('-date'),
      template_name = 'blog/blog.html',
      context_object_name = 'Post',
      paginate_by = 1)
      , name='blog'),
   path('<int:pk>/', views.post, name='post'),
]