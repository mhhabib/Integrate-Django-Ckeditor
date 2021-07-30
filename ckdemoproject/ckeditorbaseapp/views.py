from django.db import models
from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView
from .models import CreateCkPost
from .forms import CreateCkPostForm
# Create your views here.


class create(CreateView):
    model = CreateCkPost
    form_class = CreateCkPostForm
    # success_url = reverse_lazy('home')
    template_name = 'ckeditorbaseapp/create.html'

    def form_valid(self, form):
        # form.instance.post_id = self.kwargs['pk']
        form.instance.author = self.request.user
        return super().form_valid(form)
