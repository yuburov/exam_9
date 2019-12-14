from django.urls import path

from webapp.views import IndexView, PhotoView, PhotoCreateView, PhotoUpdateView, PhotoDeleteView
from django.contrib.auth.views import LoginView, LogoutView

app_name = 'webapp'

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('photos/<int:pk>/', PhotoView.as_view(), name='photo_detail'),
    path('photos/create/', PhotoCreateView.as_view(), name='photo_create'),
    path('products/<int:pk>/update/', PhotoUpdateView.as_view(), name='photo_update'),
    path('products/<int:pk>/delete/', PhotoDeleteView.as_view(), name='photo_delete'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout')
]