from rest_framework import generics
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Category, Product, Review
from .serializers import CategorySerializer, ProductWithReviewsSerializer, ReviewSerializer

@api_view(['GET'])
def products_with_reviews(request):
    products = Product.objects.prefetch_related('reviews').all()
    serializer = ProductWithReviewsSerializer(products, many=True)
    return Response(serializer.data)

class CategoryList(generics.ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class ReviewList(generics.ListAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer


@api_view(['GET'])
def products_with_reviews(request):
    products = Product.objects.prefetch_related('reviews').all()
    serializer = ProductWithReviewsSerializer(products, many=True)
    return Response(serializer.data)


class CategoryList(generics.ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class CategoryDetail(generics.RetrieveAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

# Товары
class ProductList(generics.ListAPIView):
    queryset = Product.objects.select_related('category').all()
    serializer_class = ProductWithReviewsSerializer

class ProductDetail(generics.RetrieveAPIView):
    queryset = Product.objects.select_related('category').all()
    serializer_class = ProductWithReviewsSerializer

# Отзывы
class ReviewList(generics.ListAPIView):
    queryset = Review.objects.select_related('product').all()
    serializer_class = ReviewSerializer

class ReviewDetail(generics.RetrieveAPIView):
    queryset = Review.objects.select_related('product').all()
    serializer_class = ReviewSerializer
