from django.db.models import Model, CharField, DateField, BooleanField, IntegerField
from rest_framework.serializers import ModelSerializer
class Product(Model):
    name = CharField(max_length=30)
    stock = IntegerField()
    created_at = DateField(auto_now_add=True)
    is_deleted = BooleanField(default=False)

    def __str__(self) -> str:
        return self.name
    
class ProductSerializer(ModelSerializer):
    class Meta: 
        model = Product
        fields = ['id', 'name', 'stock', 'created_at']
        read_only_fields = ['is_deleted']