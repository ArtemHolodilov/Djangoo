from django.urls import path
from . import views

urlpatterns = [
    path('australia/', views.australia),
    path('eurasia/', views.eurasia),
    path('africa/', views.africa),
    path('southamerica/', views.southamerica),
    path('northamerica/', views.northamerica),
    path('antarctica/', views.antarctica),
    path('', views.main),
]
