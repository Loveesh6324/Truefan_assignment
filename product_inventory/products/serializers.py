from rest_framework import serializers
from .models import Product


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model: type = Product
        fields: list[str] = ["id", "name", "category", "price"]
