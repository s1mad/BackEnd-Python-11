"""Функции-представления"""


from django.shortcuts import render
from django.views.generic import TemplateView


class HomeView(TemplateView):
    """Представление домашней страницы"""
    template_name = 'extended.html'
    extra_context = {"names": ["Bob", "Anton"]}


def hello_world(request):
    """Возвращает шаблон base.html и передаёт туда список имён"""
    names = ['Artyom', 'Vladimir', 'Tom']
    return render(request, 'extended.html', {'names': names})
