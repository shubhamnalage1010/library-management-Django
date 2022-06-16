from django.urls import path
from bookrecord import views

urlpatterns = [
    path('bookrecord/', views.add_show, name="addshow"),
    path('delete/<int:id>/', views.delete_data, name="deletedata"),
    path('bookrecord/<int:id>/', views.update_data, name="updatedata"),
        
    
    ]