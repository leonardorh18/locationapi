from django.urls import path
from . import views


urlpatterns = [ 
    path('getLatLong/<str:address>', views.getLatLong, name = 'getLatLong'),
    
      
]
