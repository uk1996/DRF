from rest_framework.serializers import ModelSerializer
from rest_framework import serializers
from .models import Post

class PostSerializer(ModelSerializer):
    username = serializers.ReadOnlyField(source='author.username')

    class Meta:
        model = Post
        fields = ['pk', 'username', 'message', 'created_at', 'updated_at']