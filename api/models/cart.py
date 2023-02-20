from django.db.models import Model, DateField, BooleanField, IntegerField, ForeignKey, CASCADE
from rest_framework.serializers import ModelSerializer

class Cart(Model):
    customer = ForeignKey(to='api.Customer', on_delete=CASCADE, related_name='cart')
    product = ForeignKey(to='api.Product', on_delete=CASCADE, related_name='cart')
    quantity = IntegerField(default=1)
    created_at = DateField(auto_now_add=True)
    is_deleted = BooleanField(default=False)

    def __str__(self) -> str:
        return self.name
    
class CartSerializer(ModelSerializer):
    class Meta: 
        model = Cart
        fields = ['id', 'customer', 'product', 'quantity', 'created_at']
        read_only_fields = ['is_deleted']
