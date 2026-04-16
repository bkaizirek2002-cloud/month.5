from rest_framework import serializers
from .models import User
from django.contrib.auth import get_user_model

User = get_user_model()

class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ['username', 'password', 'email']

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        user.is_active = False  # На всякий случай дублируем
        user.generate_code()
        # Тут обычно отправляется письмо с кодом
        print(f"Код для {user.username}: {user.confirmation_code}") 
        return user

class ConfirmSerializer(serializers.Serializer):
    username = serializers.CharField()
    code = serializers.CharField(max_length=6)