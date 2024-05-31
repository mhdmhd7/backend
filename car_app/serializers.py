# car_app/serializers.py
from rest_framework import serializers
from django.contrib.auth import authenticate
from .models import User

# class SignupSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = User
#         fields = ['name', 'email', 'phone_number', 'password']

#     def create(self, validated_data):
#         user = User.objects.create(
#             name=validated_data['name'],
#             email=validated_data['email'],
#             phone_number=validated_data['phone_number'],
#             role='user'
#         )
#         user.set_password(validated_data['password'])
#         user.save()
#         return user
from rest_framework import serializers
from .models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'name', 'email', 'phone_number', 'password', 'role', 'is_staff', 'is_active']
        extra_kwargs = {
            'password': {'write_only': True},
            'role': {'required': False},  # Make role not required
            'is_staff': {'required': False},  # Make is_staff not required
            'is_active': {'required': False},  # Make is_active not required
        }

    def create(self, validated_data):
        role = validated_data.get('role', 'user')  # Set default role to 'user'
        is_staff = validated_data.get('is_staff', False)  # Set default is_staff to False
        is_active = validated_data.get('is_active', True)  # Set default is_active to True
        user = User(
            name=validated_data['name'],
            email=validated_data['email'],
            phone_number=validated_data['phone_number'],
            role=role,
            is_staff=is_staff,
            is_active=is_active,
        )
        user.set_password(validated_data['password'])
        user.save()
        return user

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.phone_number = validated_data.get('phone_number', instance.phone_number)
        password = validated_data.get('password', None)
        if password:
            instance.set_password(password)
        instance.save()
        return instance

#############################
class LoginSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField(write_only=True)

    def validate(self, data):
        email = data.get('email')
        password = data.get('password')

        if email and password:
            user = authenticate(username=email, password=password)
            if not user:
                raise serializers.ValidationError("Invalid email or password.")
        else:
            raise serializers.ValidationError("Must include 'email' and 'password'.")

        data['user'] = user
        return data
###############
from .models import Category

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name', 'image_url']
#############            

from .models import Item

class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = ['category', 'name', 'image_url', 'price', 'additional_info']
#########################
class ItemNameSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = ['id','name']

class ItemDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = ['id', 'name', 'image_url', 'price', 'additional_info', 'category']
###################