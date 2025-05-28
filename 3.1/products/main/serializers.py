from rest_framework import serializers
from .models import Product, Review


class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = ['text', 'mark']


class ProductListSerializer(serializers.Serializer):
    title = serializers.CharField()
    price = serializers.DecimalField(max_digits=10, decimal_places=2)


class ProductDetailsSerializer(serializers.ModelSerializer):
    comments = ReviewSerializer(many=True, read_only=True)  # reviews → comments (related_name)

    class Meta:
        model = Product
        fields = ['title', 'description', 'price', 'comments']

