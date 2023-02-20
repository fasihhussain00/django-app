from api.viewsets.cart import CartViewSet
from api.viewsets.product import ProductViewSet
from .viewsets.customer import CustomerViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'customer', CustomerViewSet, basename='customer')
router.register(r'product', ProductViewSet, basename='product')
router.register(r'cart', CartViewSet, basename='cart')