# main/serializers.py

from rest_framework import serializers
from .models import students  # Ensure this import matches your model name
from.models import singup
from django.contrib.auth.hashers import check_password

from .models import StudentAdmission
class itemserializer(serializers.ModelSerializer):
    class Meta:
        model = students 
        fields = '__all__'  


class singupSerializer(serializers.ModelSerializer):
    class Meta:
        model = singup
        fields = '__all__'


class LoginSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField()

    def validate(self, data):
        email = data.get("email")
        password = data.get("password")

        try:
            user = singup.objects.get(email=email)  # Ensure correct model reference
        except singup.DoesNotExist:
            raise serializers.ValidationError("Invalid email or password")

        # Check if the provided password matches the stored hashed password
        if not check_password(password, user.password):
            raise serializers.ValidationError("Invalid email or password")

        data["user"] = user  # Add the user object to the validated data
        return data


class StudentAdmissionSerializer(serializers.ModelSerializer):
    class Meta:
        model = StudentAdmission
        fields = ['id', 'student_name', 'email', 'class_name', 'date_of_birth', 'address']
