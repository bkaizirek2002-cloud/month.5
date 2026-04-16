from rest_framework import viewsets
from product.models import Category, Product, Review
from product.serializers import CategorySerializer, ReviewSerializer, ProductWithReviewsSerializer

class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

# Товары
class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.select_related('category').all()
    serializer_class = ProductWithReviewsSerializer

# Отзывы
class ReviewViewSet(viewsets.ModelViewSet):
    queryset = Review.objects.select_related('product').all()
    serializer_class = ReviewSerializer