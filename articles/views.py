from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin 
from django.shortcuts import render
from django.views.generic import CreateView, ListView, DeleteView, UpdateView, DetailView
from .models import Article, Comment
from django.urls import reverse_lazy

class ArticleCreateView(LoginRequiredMixin, CreateView):
    template_name = 'article_new.html'
    model = Article
    fields = ('title', 'body')
    login_url = 'login'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
    
    def test_func(self):
        obj = self.get_object()
        return obj.author == self.request.user

class ArticleListView(LoginRequiredMixin,  ListView):
    template_name = 'article_list.html'
    model = Article
    context_object_name = 'articles'
    login_url = 'login'

class ArticleUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    template_name = 'article_edit.html'
    fields = ('title', 'body')
    model = Article
    login_url = 'login'

    def test_func(self):
        obj = self.get_object()
        return obj.author == self.request.user

class ArticleDetailView(LoginRequiredMixin, UserPassesTestMixin, DetailView):
    template_name = 'article_detail.html'
    model = Article
    login_url = 'login'

    def test_func(self):
        obj = self.get_object()
        return obj.author == self.request.user

class ArticleDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    template_name = 'article_delete.html'
    model = Article
    success_url = reverse_lazy('article_list')
    login_url = 'login'

    def test_func(self):
        obj = self.get_object()
        return obj.author == self.request.user

class CommentCreateView(LoginRequiredMixin, CreateView):
    template_name = 'comment_new.html'
    model = Comment
    fields = ('comment',)
    login_url = 'login'

    def form_valid(self, form):
        form.instance.author = self.request.user
        form.instance.article = Article.objects.get(id=self.kwargs['article_id'])
        return super().form_valid(form)

class CommentUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    template_name = 'comment_edit.html'
    model = Comment
    fields = ('comment',)
    login_url = 'login'

    def test_func(self):
        obj = self.get_object()
        return obj.author == self.request.user

class CommentDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    template_name = 'comment_delete.html'
    model = Comment
    success_url = reverse_lazy('article_list')

    def test_func(self):
        obj = self.get_object()
        return obj.author == self.request.user
