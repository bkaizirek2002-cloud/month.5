from rest_framework import generics
from .models import Category, Product, Review
from .serializers import CategorySerializer, ProductSerializer, ReviewSerializer

# Категории
class CategoryList(generics.ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class CategoryDetail(generics.RetrieveAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

# Товары
class ProductList(generics.ListAPIView):
    queryset = Product.objects.select_related('category').all()
    serializer_class = ProductSerializer

class ProductDetail(generics.RetrieveAPIView):
    queryset = Product.objects.select_related('category').all()
    serializer_class = ProductSerializer

# Отзывы
class ReviewList(generics.ListAPIView):
    queryset = Review.objects.select_related('product').all()
    serializer_class = ReviewSerializer

class ReviewDetail(generics.RetrieveAPIView):
    queryset = Review.objects.select_related('product').all()
    serializer_class = ReviewSerializer
