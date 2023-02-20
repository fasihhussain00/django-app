from django.db.models import Model, CharField, DateField, BooleanField
from rest_framework.serializers import ModelSerializer
from . import CartSerializer

class Customer(Model):
    _statues = (
        ('allowed', 'Allowed'),
        ('unallowed', 'Unallowed'),
    )
    name = CharField(max_length=30)
    date_of_birth = DateField(max_length=30)
    status = CharField(max_length=30, choices=_statues)
    created_at = DateField(auto_now_add=True)
    is_deleted = BooleanField(default=False)

    def __str__(self) -> str:
        return self.name
    
class CustomerSerializer(ModelSerializer):
    cart = CartSerializer(many=True, read_only=True)
    class Meta: 
        model = Customer
        fields = ['id', 'name', 'date_of_birth', 'status', 'cart']
        read_only_fields = ['is_deleted']