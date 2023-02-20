from django.contrib import admin
from .models.customer import Customer
from .models.product import Product
from .models.cart import Cart
admin.site.register(Customer)
admin.site.register(Product)
admin.site.register(Cart)