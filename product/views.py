from rest_framework import generics
from rest_framework import generics
from .models import Category, Product, Review
from .serializers import CategorySerializer, ReviewSerializer, ProductWithReviewsSerializer


# Категории
class CategoryList(generics.ListCreateAPIView): 
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class CategoryDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

# Товары
class ProductList(generics.ListCreateAPIView): 
    queryset = Product.objects.select_related('category').all()
    serializer_class = ProductWithReviewsSerializer

class ProductDetail(generics.RetrieveUpdateDestroyAPIView): 
    queryset = Product.objects.select_related('category').all()
    serializer_class = ProductWithReviewsSerializer

# Отзывы
class ReviewList(generics.ListCreateAPIView): 
    queryset = Review.objects.select_related('product').all()
    serializer_class = ReviewSerializer

class ReviewDetail(generics.RetrieveUpdateDestroyAPIView): 
    queryset = Review.objects.select_related('product').all()
    serializer_class = ReviewSerializer