import json

from rest_framework.decorators import action
from rest_framework.permissions import SAFE_METHODS, AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet
from .serializers import CommentSerializer, PhotoSerializer
from webapp.models import Comment, Photo


class CommentViewSet(ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [IsAuthenticated]

    def get_permissions(self):
        method = self.request.method
        if method in SAFE_METHODS:
            return [AllowAny()]
        else:
            return super().get_permissions()

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

class PhotoViewSet(ModelViewSet):
    queryset = Photo.objects.all()
    serializer_class = PhotoSerializer
    permission_classes = [IsAuthenticated]

    @action(methods=['post'], detail=True)
    def rate_up(self, request, pk=None):
        photo = self.get_object()
        photo.likes += 1
        photo.save()
        return Response({'id': photo.pk, 'likes': photo.likes})

    @action(methods=['post'], detail=True)
    def rate_down(self, request, pk=None):
        photo = self.get_object()
        photo.likes -= 1
        photo.save()
        return Response({'id': photo.pk, 'likes': photo.likes})
