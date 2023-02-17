from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.

def monday(request):
    return HttpResponse("Понедельник день тяжелый ;с")


def tuesday(request):
    return HttpResponse("Вторник день тяжелый ;с")


def wednesday(request):
    return HttpResponse("Среда день тяжелый ;с")


def thursday(request):
    return HttpResponse("Четверг день тяжелый ;с")


def friday(request):
    return HttpResponse("Пятница день тяжелый ;с")


def saturday(request):
    return HttpResponse("Суббота день тяжелый ;с")


def sunday(request):
    return HttpResponse("Воскресенье  день тяжелый ;с")

