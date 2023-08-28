from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, UpdateView, DetailView, DeleteView, CreateView
from .models import Article
from .forms import ArticleForm

class ArticleCreateView(CreateView):
    model = Article
    form_class = ArticleForm
    template_name = 'article_create.html'
    success_url = reverse_lazy('home')

class ArticleListView(ListView):
    model = Article
    context_object_name = 'articles'
    template_name = 'home.html'

class ArticleDetailView(DetailView):
    model = Article
    context_object_name = 'article'
    template_name = 'article_detail.html'

class ArticleUpdateView(UpdateView):
    model = Article
    template_name = 'article_update.html'
    form_class = ArticleForm
    def get_success_url(self):
        return reverse_lazy('article_detail', args=[self.object.id])


class ArticleDeleteView(DeleteView):
    model = Article
    template_name = 'article_delete.html'
    success_url = reverse_lazy('home')