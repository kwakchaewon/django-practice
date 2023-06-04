from django.urls import include, path
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register('', views.PostViewSet) # 2개의 URL 을 만들어줍니다.
# router.urls # url pattern list

urlpatterns = [
    path('', include(router.urls)),
    ]