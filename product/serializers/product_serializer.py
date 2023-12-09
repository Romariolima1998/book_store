from rest_framework import serializers

from product.models.product import Product
from product.serializers.category_serializer import CategorySerializer

from product.models import Category


class ProductSerializer(serializers.ModelSerializer):
    category = CategorySerializer(required=True, many=True)
    categories_id = serializers.PrimaryKeyRelatedField(queryset=Category.objects.all(), write_only=True, many=True)

    class Meta:
        model = Product
        fields = [
            'id',
            'title',
            'description',
            'price',
            'active',
            'category',
            'categories_id',
        ]

    def create(self, validated_data):
        category_data = validated_data.pop('categories_id')
        product = Product.objects.create(**validated_data)

        for category in category_data:
            product.category.add(category)

        return product