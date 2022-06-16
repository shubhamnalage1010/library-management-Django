from django.urls import path, include
from rest_framework import routers
from api import views

router= routers.DefaultRouter()
router.register('book-records', views.BookRecordView)
router.register('users', views.UserView)

urlpatterns = [
    path('', include(router.urls)),
    path('login', views.UserAuthApi.as_view()),



]
