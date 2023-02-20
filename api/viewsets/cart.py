from rest_framework.viewsets import ModelViewSet
from ..models.cart import Cart, CartSerializer

class CartViewSet(ModelViewSet):
    queryset = Cart.objects.all()
    serializer_class = CartSerializer