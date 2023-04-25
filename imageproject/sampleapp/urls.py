# from django.urls import path  
# from .views import image_request  
  
# app_name = 'sampleapp'  
# urlpatterns = [  
#     path('', image_request, name = "image-request")
# ]


from django.urls import path
from .import views

urlpatterns = [
    path('', views.index, name='index'),
]