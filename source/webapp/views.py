from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin, UserPassesTestMixin
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

class PhotoCreateView(LoginRequiredMixin, CreateView):
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


class PhotoUpdateView(PermissionRequiredMixin, UserPassesTestMixin,UpdateView):
    model = Photo
    form_class = PhotoForm
    context_object_name = 'photo'
    template_name = 'update.html'
    permission_required = 'webapp.change_photo'
    permission_denied_message = 'Доступ ограничен'

    def test_func(self):
        photo = self.get_object()
        return self.request.user == photo.author or self.request.user.is_superuser \
               or self.request.user.has_perm('webapp.change_photo')

    def get_success_url(self):
        return reverse('webapp:photo_detail', kwargs={'pk': self.object.pk})

class PhotoDeleteView(PermissionRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Photo
    context_object_name = 'photo'
    template_name = 'delete.html'
    success_url = reverse_lazy('webapp:index')
    permission_required = 'webapp.delete_photo'
    permission_denied_message = 'Доступ ограничен'

    def test_func(self):
        photo = self.get_object()
        return self.request.user == photo.author or self.request.user.is_superuser \
               or self.request.user.has_perm('webapp.change_photo')


