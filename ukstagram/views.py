from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from rest_framework.generics import ListCreateAPIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import PostSerializer
from .models import Post

class PostViewSet(ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer



class PublicPostListAPIView(ListCreateAPIView):
    queryset = Post.objects.all() # filter(is_public=True)
    serializer_class = PostSerializer

    # def post(self, request, format=None):
    #     serializer = PostSerializer(data=request.data)
    #     if serializer.is_valid():
    #         serializer.save(author=request.user)
    #         return Response(serializer.data, status=status.HTTP_201_CREATED)
    #     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


public_post_list = PublicPostListAPIView.as_view()