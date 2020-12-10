from django.urls import include, path
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register(r'notification', views.NotificationViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('notification/', include('rest_framework.urls', namespace='rest_framework'))
]