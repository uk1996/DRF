from django.contrib.auth import get_user_model
from rest_framework.serializers import ModelSerializer
from rest_framework import serializers
from .models import Post

# class AuthSerializer(ModelSerializer):
#     class Meta:
#         model = get_user_model()
#         fields = ['username', 'email']

class PostSerializer(ModelSerializer):
    username = serializers.ReadOnlyField(source='author.username')
    # author = AuthSerializer()

    class Meta:
        model = Post
        fields = ['pk', 'username', 'message', 'created_at', 'updated_at', 'is_public']