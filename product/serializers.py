from rest_framework import serializers
from .models import Category, Product, Review

class CategorySerializer(serializers.ModelSerializer):
    products_count = serializers.SerializerMethodField()
    def validate_name(self, value):
        if len(value) < 2:
            raise serializers.ValidationError("Название категории слишком короткое!")
        return value

    class Meta:
        model = Category
        fields = ['id', 'name', 'products_count']

    def get_products_count(self, obj):
        return obj.products.count()

class ReviewSerializer(serializers.ModelSerializer):
    def validate_stars(self, value):
        if value < 1 or value > 5:
            raise serializers.ValidationError("Оценка должна быть от 1 до 5.")
        return value

    def validate_text(self, value):
        if len(value) < 10:
            raise serializers.ValidationError("Отзыв слишком короткий, напишите подробнее.")
        return value
    class Meta:
        model = Review
        fields = ['id', 'author', 'text', 'stars', 'product', 'created_at']
        

class ProductWithReviewsSerializer(serializers.ModelSerializer):
    reviews = ReviewSerializer(many=True, read_only=True)
    rating = serializers.SerializerMethodField()
    def validate(self, data):
        price = data.get('price')
        title = data.get('title')
        description = data.get('description')

        if price is not None and price <= 0:
            raise serializers.ValidationError({"price": "Цена должна быть больше нуля!"})

        if title and description and title == description:
            raise serializers.ValidationError({"detail": "Описание не должно совпадать с названием."})

        return data

    class Meta:
        model = Product
        fields = ['id', 'title', 'description', 'price', 'category', 'reviews', 'rating']

    def get_rating(self, obj):
        reviews = obj.reviews.all()
        if reviews.exists():
            total_stars = sum([review.stars for review in reviews])
            return round(total_stars / reviews.count(), 2)
        return 0.0