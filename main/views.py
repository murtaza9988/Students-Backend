from rest_framework import viewsets
from .models import students, singup  # Keep only the necessary models
from .serializers import itemserializer, singupSerializer  # Keep only the necessary serializers
from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.permissions import AllowAny 
from dj_rest_auth.registration.views import SocialLoginView

from allauth.socialaccount.providers.google.views import GoogleOAuth2Adapter
from .serializers import LoginSerializer 
from rest_framework.decorators import action # Ensure you have this serializer defined
from django.contrib.auth.hashers import check_password

from rest_framework_simplejwt.tokens import RefreshToken
class ItemViewSet(viewsets.ModelViewSet):
    permission_classes = [AllowAny]
    queryset = students.objects.all()  
    serializer_class = itemserializer
class GoogleLogin(SocialLoginView):
    permission_classes = [AllowAny]  # Allow any user (authenticated or not)
    adapter_class = GoogleOAuth2Adapter  # Use Google OAuth adapter

class singupViewSet(viewsets.ModelViewSet):
    queryset = singup.objects.all()
    permission_classes = [AllowAny]
    serializer_class = singupSerializer
    @action(detail=True, methods=['post'])
    def createuser(self, request):
        serializer = singupSerializer(data=request.data)
        print(serializer)
        # Check if the data is valid
        if serializer.is_valid():
            serializer.save()  # Save the user data if valid
            return Response({"message": "Signup successful"}, status=status.HTTP_201_CREATED)
        
        # Return validation errors if any
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
     
    @action(detail=True, methods=['get'])
    def Users(self,request):
        serializer = singupSerializer(data=request.data)
        # Save the user data if valid
        return Response({"message": "Signup successful"},serializer.data, status=status.HTTP_201_CREATED)
        
     


class LoginViewSet(viewsets.ViewSet):
    permission_classes = [AllowAny]  # Allow any user (authenticated or not) to access

    def create(self, request):
        serializer = LoginSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.validated_data["user"]  # Get the validated user object
            
            # Generate JWT token
            refresh = RefreshToken.for_user(user)
            return Response({
                "message": "Login successful",
                "user": user.username,
                "refresh": str(refresh),
                "access": str(refresh.access_token),  # Include access token
            }, status=status.HTTP_200_OK)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)