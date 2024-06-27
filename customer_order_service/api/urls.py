from rest_framework.routers import DefaultRouter

from .views import home,CustomerViewSet, OrderViewSet
from django.contrib.auth import views as auth_views  
from django.urls import path,include

router = DefaultRouter()
router.register(r'customers', CustomerViewSet)
router.register(r'orders', OrderViewSet)

urlpatterns = [
    path('home', home, name=''),    
    path('', include(router.urls)),  
]