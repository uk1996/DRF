from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet
from rest_framework.generics import ListCreateAPIView, ListAPIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import PostSerializer
from .models import Post

class PostViewSet(ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer



# 방법 1
# class PublicPostListAPIView(ListAPIView):
#     queryset = Post.objects.filter(is_public=True)
#     serializer_class = PostSerializer
# public_post_list = PublicPostListAPIView.as_view()

# 방법 2
# class PublicPostListAPIView(APIView):
#     def get(self, request):
#         qs = Post.objects.filter(is_public=True)
#         serializer = PostSerializer(instance=qs, many=True)
#         return Response(serializer.data)
# public_post_list = PublicPostListAPIView.as_view()


# 방법 3
@api_view(['GET'])
def public_post_list(request):
    qs = Post.objects.filter(is_public=True)
    serializer = PostSerializer(instance=qs, many=True)
    return Response(serializer.data)