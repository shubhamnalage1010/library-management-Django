from . import serializers
from rest_framework import viewsets ,filters,authentication, views, response, status
from bookrecord.models import Book
from django.contrib.auth.models import User
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.settings import api_settings
from rest_framework.permissions import IsAuthenticated


class UserAuthApi(ObtainAuthToken):
    renderer_classes = api_settings.DEFAULT_RENDERER_CLASSES

class BookRecordView(viewsets.ModelViewSet):
    """Book-Record API Model ViewSet"""

    """if you want only get method use this below ""GET method "" Otherwise you can keep as it is """
    # http_method_names = ['get']
    authentication_classes = (authentication.TokenAuthentication,)
    permissions_classes = (IsAuthenticated)
    serializer_class=serializers.BookSerializer
    filter_backends = (filters.SearchFilter, filters.OrderingFilter)
    search_fields=('product_category__id','name')
    queryset=Book.objects.all()


class UserView(viewsets.ModelViewSet):
    """All-User Api """
    """if you want only get method use this below ""GET method "" Otherwise you can keep as it is """
    http_method_names = ['get']
    serializer_class = serializers.UsersSerializer
    filter_backends = (filters.SearchFilter, filters.OrderingFilter)
    search_fields=('product_category__id','name')
    queryset = User.objects.all()

    """if you want Only User Excluding SUPER User then Use This Query set """
    # queryset = User.objects.filter(is_superuser=False, is_staff=False)