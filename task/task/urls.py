"""
URL configuration for task project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.1/topics/http/urls/
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
from myapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('bmicalc/',views.BmiCalculatorView.as_view()),
    path('age/',views.AgeCalaculatorView.as_view()),
    path('percentage/',views.PercentageCalcView.as_view()),
    path('si/',views.SimpleInterestView.as_view()),
    path('bill/',views.ElectricityView.as_view()),
    path('discount/',views.DiscountView.as_view()),
    path('profit/',views.ProfitView.as_view()),
    path('salary/',views.SalaryView.as_view()),
    path('time/',views.TimeView.as_view()),
    path('fuel/',views.FuelView.as_view()),
    path('product_profit/',views.ProductProfitView.as_view()),
    path('age-details/',views.AgeDetailsView.as_view()),
    
]
