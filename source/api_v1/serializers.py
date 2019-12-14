from rest_framework.serializers import ModelSerializer
from webapp.models import Photo, Comment

class CommentSerializer(ModelSerializer):
    class Meta:
        model = Comment
        fields = ('id', 'text', 'photo', 'author', 'created_at')

class PhotoSerializer(ModelSerializer):
    comments = CommentSerializer(many=True, read_only=True)
    class Meta:
        model = Photo
        fields = ('id', 'photo', 'caption', 'created_at','likes','author', 'comments')