from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.


def param(request, param):
    if param == "monday":
        return HttpResponse("Понедельник день тяжелый ;с")
    elif param == "tuesday":
        return HttpResponse("Вторник день тяжелый ;с")
    elif param == "wednesday":
        return HttpResponse("Среда день тяжелый ;с")
    elif param == "thursday":
        return HttpResponse("Четверг день тяжелый ;с")
    elif param == "friday":
        return HttpResponse("Пятница день тяжелый ;с")
    elif param == "saturday":
        return HttpResponse("Суббота день тяжелый ;с")
    elif param == "sunday":
        return HttpResponse("Воскресенье  день тяжелый ;с")
    else:
        return HttpResponse("Я не знаю так день недели ((((", param)
