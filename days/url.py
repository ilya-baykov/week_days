from django.urls import path
from . import views

urlpatterns = [

    path('monday', views.monday),
    path('tuesday', views.tuesday),
    path('wednesday', views.wednesday),
    path('thursday', views.thursday),
    path('friday', views.friday),
    path('saturday', views.saturday),
    path('sunday', views.sunday),

]
