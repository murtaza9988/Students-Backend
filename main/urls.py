from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import GoogleLogin, ItemViewSet, singupViewSet,LoginViewSet # Only import the necessary view sets
from .views import StudentAdmissionViewSet
router = DefaultRouter()
router.register(r'items', ItemViewSet,basename='ITEMS'),
router.register(r'singup', singupViewSet,basename='SINGUP'), # Keep only login and item routes
router.register(r'login', LoginViewSet, basename='login') 
router.register(r'Students', StudentAdmissionViewSet, basename='StudentAdmission') 
 # Use basename for non-model viewsets

urlpatterns = [
    path('', include(router.urls)), 
     # Includes all routes registered with the router
    path('auth/google/', GoogleLogin.as_view(), name='google_login'),
]+ router.urls

