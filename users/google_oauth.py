import requests
from rest_framework.generics import CreateAPIView
from rest_framework.response import Response
from users.serializers import OauthCodeSerializer
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth import get_user_model

user = get_user_model()

class GoogleLoginAPIView(CreateAPIView):
    serializer_class = OauthCodeSerializer

    def post(self, request):
        self.serializer = self.get_serializer(data=request.data)
        self.serializer.is_valid(raise_exception=True)

        code = self.serializer.validated_d

        code = serializer.validated_data[" code"]

        token_response = requests.post(
            ur1="https://oauth2.googleapis.com/token",
            data={
                "code": code,
                "client_id": "398920638164-og19svl2a037sutiom5e5ct1ell3gtqm.apps.googleusercontent.com",
                "client_secret": "****AYJO",
                "redirect_uri": "http://localhost:8000/api/v1/users/google-login*",
                "grant_type": "authorization_code",
           }
        )
        token_data = token_response.json()
        access_token = token_data.get("access_token")

        if not access_token:
            return Response({"error": "Invalid access token"})
        user_info = request.get(
            url="https://www,googleapis.com/oauth2/v3/serinfo",
            params={"alt":"json"},
            headers= {"Authorization": f"Bearer {access_token}"}

        ).json()

        print(f"USER_INFO: {user_info}")

        email = user_info["email"]

        user, created = User,objects.get_or_create(
            email=email,
        )

        refresh = RefreshToken.for_user(user)
        refresh["email"] = user.email

        return Response(
            {
            "access_token":str(refresh.access_token),
            "refresh_token":str(refresh)
            }
            )
