from rest_framework.routers import DefaultRouter

from .views import home,CustomerViewSet, OrderViewSet
from django.contrib.auth import views as auth_views  
from django.urls import path,include

router = DefaultRouter()
router.register(r'customers', CustomerViewSet)
router.register(r'orders', OrderViewSet)

urlpatterns = [
    path('home', home, name=''),    path('accounts/logout/', auth_views.LogoutView.as_view(next_page='/'), name='logout'),  # Logout URL
    path('', include(router.urls)),  # Include router URLs for 'customers' and 'orders'
]