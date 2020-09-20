from django.contrib import admin
from django.urls import path, include
from .views import *
from django.conf.urls import url

urlpatterns = [
    path('', ArticleListView.as_view(), name="article_list"),
    path('new/', ArticleCreateView.as_view(), name="article_new"),
    path('comments/<int:pk>/edit/', CommentUpdateView.as_view(), name="comment_edit"),
    url(r'^new/comment/(?P<article_id>\d+)/$', CommentCreateView.as_view(), name="comment_new"),
    path('comments/<int:pk>/delete/', CommentDeleteView.as_view(), name="comment_delete"),
    path('<int:pk>/edit/', ArticleUpdateView.as_view(), name="article_edit"),
    path('<int:pk>/', ArticleDetailView.as_view(), name="article_detail"),
    path('<int:pk>/delete/', ArticleDeleteView.as_view(), name="article_delete"),
    
   
]