from rest_framework import serializers

from product.models import ProductModel


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductModel
        fields = [
            "id",
            "name",
            "description",
            "product_number",
            "price",
            "image",
            "quantity",
        ]
