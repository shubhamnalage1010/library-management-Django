from dataclasses import field
import imp
from rest_framework import serializers
from bookrecord.models import Book
from django.contrib.auth.models import User

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields= '__all__' 


class UsersSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            
            'id','username','first_name','last_name','password','email'
        ]
        extra_kwargs = {
            'password' : {'write_only':True}
        }