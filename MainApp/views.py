from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def home(request):
    text = """
    <h1>"Изучаем django"</h1>
    <strong>Автор</strong>: <i>Иванов И.П.</i>
    """
    return HttpResponse(text)

def about(request):
    text1 = """
    Имя: Иван
    Отчество: Петрович
    Фамилия: Иванов
    телефон: 8-923-600-01-02
    email: vasya@mail.ru
    """
    return HttpResponse(text1)