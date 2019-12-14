from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404
from django.urls import reverse_lazy, reverse
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from webapp.forms import PhotoForm
from webapp.models import Photo


class IndexView(ListView):
    model = Photo
    template_name = 'index.html'
    ordering = ['-created_at']

class PhotoView(DetailView):
    model = Photo
    template_name = 'detail.html'

class PhotoCreateView(CreateView):
    model = Photo
    template_name = 'create.html'
    form_class = PhotoForm

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.author = self.request.user
        self.object.save()
        return HttpResponseRedirect(self.get_success_url())

    def get_success_url(self):
        return reverse('webapp:index')


class PhotoUpdateView(UpdateView):
    model = Photo
    form_class = PhotoForm
    context_object_name = 'photo'
    template_name = 'update.html'

    def get_success_url(self):
        return reverse('webapp:photo_detail', kwargs={'pk': self.object.pk})

class PhotoDeleteView(DeleteView):
    model = Photo
    context_object_name = 'photo'
    template_name = 'delete.html'
    success_url = reverse_lazy('webapp:index')

