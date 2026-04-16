from django.urls import path, include
from rest_framework.routers import SimpleRouter
from .views import CategoryViewSet, ProductViewSet, ReviewViewSet

router = SimpleRouter()
router.register(r'categories', CategoryViewSet)
router.register(r'products', ProductViewSet)
router.register(r'reviews', ReviewViewSet)


urlpatterns = [
    path('', include(router.urls)),
]