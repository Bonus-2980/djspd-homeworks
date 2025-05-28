from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status

from main.models import Product
from main.serializers import ReviewSerializer, ProductListSerializer, ProductDetailsSerializer


@api_view(['GET'])
def products_list_view(request):
    """Получение всех товаров и сериализация через ProductListSerializer"""
    products = Product.objects.all()
    serializer = ProductListSerializer(products, many=True)
    return Response(serializer.data)


class ProductDetailsView(APIView):
    def get(self, request, product_id):
        """Получение одного товара по id, если не найден — 404"""
        product = get_object_or_404(Product, id=product_id)
        serializer = ProductDetailsSerializer(product)
        return Response(serializer.data)


class ProductFilteredReviews(APIView):
    def get(self, request, product_id):
        """Фильтрация отзывов по оценке mark (если передана), иначе все отзывы"""
        product = get_object_or_404(Product, id=product_id)
        mark = request.query_params.get('mark')

        if mark is not None:
            try:
                mark = int(mark)
                reviews = product.comments.filter(mark=mark)
            except ValueError:
                return Response({'error': 'Параметр mark должен быть числом от 1 до 5'}, status=status.HTTP_400_BAD_REQUEST)
        else:
            reviews = product.comments.all()

        serializer = ReviewSerializer(reviews, many=True)
        return Response(serializer.data)

