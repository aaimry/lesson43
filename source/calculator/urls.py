from django.contrib import admin
from django.urls import path

from source.calculator.views import calculator_view

urlpatterns = [
    path('', calculator_view),
    ]