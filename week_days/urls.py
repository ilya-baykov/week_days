"""week_days URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from days import views as views_days

urlpatterns = [
    path('admin/', admin.site.urls),
    path('week_days/monday', views_days.monday),
    path('week_days/tuesday', views_days.tuesday),
    path('week_days/wednesday', views_days.wednesday),
    path('week_days/thursday', views_days.thursday),
    path('week_days/friday', views_days.friday),
    path('week_days/saturday', views_days.saturday),
    path('week_days/sunday', views_days.sunday),

]
