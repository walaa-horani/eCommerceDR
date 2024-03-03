from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ProductViewSet, CartItemViewSet

router = DefaultRouter()
router.register('products', ProductViewSet, basename='product')
# router.register('cart', CartViewSet, basename='cart')
router.register('cartItems', CartItemViewSet, basename='cartitem')

urlpatterns = [
    path('', include(router.urls))
]
