# blog/urls.py
from django.urls import path
from . import views

app_name = 'blog'
urlpatterns = [
    path('', views.index, name='index'),
    path('counter1/', views.counter1),
    path('counter2/', views.counter2),
    path('<int:pk>/' , views.post_detail,name='post_detail'),
    path('postcreate/', views.post_create, name='post_create'),
    
    
    # Generic views
    # path('posts/', views.PostListView.as_view()),
    # path('posts/<int:pk>/' , views.PostDetailView.as_view()),
    # path('posts/create/' , views.PostCreateView.as_view()),
]
