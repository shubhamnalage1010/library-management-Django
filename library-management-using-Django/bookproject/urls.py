from django.contrib import admin
from django.urls import path, include
from bookrecord import views
from rest_framework_swagger.views import get_swagger_view
schema_view = get_swagger_view(title='Pastebin API')



urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('authentication.urls')),
    path('book/', include('bookrecord.urls')),
    path('api/', include('api.urls')),


]