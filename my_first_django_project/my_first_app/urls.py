"""Конечные точки"""


from django.urls import path
from .views import hello_world, HomeView


urlpatterns = [
    path('hello', hello_world, name='hello_world'),
    path('', HomeView.as_view(), name='home'),
]
