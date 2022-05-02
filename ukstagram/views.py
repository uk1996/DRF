from django.shortcuts import render
from rest_framework.decorators import api_view, action
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet
from rest_framework.generics import ListCreateAPIView, ListAPIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import PostSerializer
from .models import Post
from .permissions import IsAuthorOrReadOnly
from rest_framework.filters import SearchFilter, OrderingFilter

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
# @api_view(['GET'])
# def public_post_list(request):
#     qs = Post.objects.filter(is_public=True)
#     serializer = PostSerializer(instance=qs, many=True)
#     return Response(serializer.data)


class PostViewSet(ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

    permission_classes = [IsAuthorOrReadOnly]

    filter_backends = [SearchFilter, OrderingFilter]
    # "^": Start-with search, "=":Exact matches, "@":Full-text search, "$":Regex search
    # get_search_fields 함수로 구현 가능
    search_fields = ['message']
    ordering_fields = ['id'] # 미지정시 serializer_class에 지정된 필드들.
    ordering = ['-id'] # 디폴트 정렬을 지정

    # 자신이 적은 포스팅만 조회하기
    # def get_queryset(self):
    #     qs = super().get_queryset().filter(author=self.request.user)
    #     return qs

    # Filtering, Ordering 예시
    # def get_queryset(self):
    #     q = self.request.query_params.get('q', '')
    #     qs = super().get_queryset()
    #     if q:
    #         qs = qs.filter(message__icontains=q)
    #     return qs.order_by('-id')

    # def create(self, request):
    #     serializer = self.get_serializer(data=request.data)
    #     if serializer.is_valid():
    #         serializer.save(author=request.user)
    #         return Response(serializer.data, status=status.HTTP_201_CREATED)
    #     return Response(status=status.HTTP_400_BAD_REQUEST)

    def perform_create(self, serializer):
        serializer.save(author=self.request.user, ip=self.request.META['REMOTE_ADDR'])

    @action(detail=False, methods=['GET'])
    def public(self, request):
        qs = self.get_queryset().filter(is_public=True).order_by('-id')

        page = self.paginate_queryset(qs)
        if page:
            serializer = self.get_serializer(instance=page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(instance=qs, many=True)
        return Response(serializer.data)

    @action(detail=True, methods=['PATCH'])
    def set_public(self, request, pk):
        instance = self.get_object()
        instance.is_public = True
        instance.save(update_fields=['is_public'])
        serializer = self.get_serializer(instance=instance)
        return Response(serializer.data)


# post_list = PostViewSet.as_view({
#     'get':'list',
#     'post':'create',
# })
# post_detail = PostViewSet.as_view({
#     'get':'retrieve',
#     'put':'update',
#     'patch':'partial_update',
#     'delete':'destroy',
# })