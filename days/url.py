from django.urls import path
from . import views

urlpatterns = [
    path('<param>', views.param)

]
