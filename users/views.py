from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import RegisterSerializer, ConfirmSerializer
from .models import User

class RegisterAPIView(APIView):
    def post(self, request):
        serializer = RegisterSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "User created. Check your code."}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ConfirmAPIView(APIView):
    def post(self, request):
        serializer = ConfirmSerializer(data=request.data)
        if serializer.is_valid():
            username = serializer.validated_data['username']
            code = serializer.validated_data['code']
            try:
                user = User.objects.get(username=username, confirmation_code=code)
                user.is_active = True
                user.confirmation_code = None # Сбрасываем код
                user.save()
                return Response({"message": "Account activated!"}, status=status.HTTP_200_OK)
            except User.DoesNotExist:
                return Response({"error": "Invalid code or username"}, status=status.HTTP_400_BAD_REQUEST)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)