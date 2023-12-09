from rest_framework import serializers

from product.models import Product
from product.serializers.product_serializer import ProductSerializer

from order.models import Order


class OrderSerializer(serializers.ModelSerializer):
    product_id = serializers.PrimaryKeyRelatedField(queryset=Product.objects.all(), write_only=True, many=True)
    product = ProductSerializer(required=True, many=True)
    total = serializers.SerializerMethodField()

    def get_total(self, instance):
        total = sum([product.price for product in instance.product.all()])
        return total

    class Meta:
        model = Product
        fields = ['product', 'total', 'product_id']
        extra_kwars = {'product': {'required': False}}

    def create(self, validated_data):
        product_data = validated_data.pop('products_id')
        user_data = validated_data('user')
        order = Order.objects.create(user=user_data)

        for product in product_data:
            order.product.add(product)
        return order