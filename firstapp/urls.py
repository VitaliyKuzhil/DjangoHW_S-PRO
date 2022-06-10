from django.urls import path
from .views import hellodjango, user_name, date, year, day, month

urlpatterns = [
    path('', hellodjango),
    path('date/', date),
    path('date/year/', year),
    path('date/day/', day),
    path('date/month/', month),
    path('<str:name>/', user_name),
]
