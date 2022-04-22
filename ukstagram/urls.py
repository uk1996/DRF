from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register('posts', views.PostViewSet, basename='posts')


urlpatterns = [
    path('', include(router.urls)),
    # path('posts/', views.post_list, name='post_list'),
    # path('posts/<int:pk>/', views.post_detail, name='post_detail'),
    # path('public/', views.public_post_list, name='public_post_list'),
]