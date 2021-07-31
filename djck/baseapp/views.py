from django.db import models
from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView
from django.views.generic.detail import DetailView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import CreatePost
from .forms import CreatePostForm
from django.urls import reverse_lazy
# Create your views here.


class home(ListView):
    model = CreatePost
    context_object_name = 'posts'
    template_name = 'baseapp/index.html'
    ordering = ['-pub_date']


class create(CreateView):
    model = CreatePost
    form_class = CreatePostForm
    success_url = reverse_lazy('home')
    template_name = 'baseapp/create.html'

    def form_valid(self, form):
        # form.instance.post_id = self.kwargs['pk']
        form.instance.author = self.request.user
        return super().form_valid(form)


class PostDetailView(DetailView):
    model = CreatePost
