from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register('posts', views.PostViewSet) # 3개의 URL을 만들어줌(list, detail, root)


urlpatterns = [
    path('', include(router.urls)),
    path('public/', views.public_post_list, name='public_post_list'),
]