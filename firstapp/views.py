import datetime

from django.http import HttpRequest, HttpResponse
from django.shortcuts import render


def hellodjango(request: HttpRequest):
    return HttpResponse('Hello Django!')


def date(request: HttpRequest):
    return HttpResponse(datetime.date.today())


def year(request: HttpRequest):
    return HttpResponse(datetime.date.today().year)


def day(request: HttpRequest):
    return HttpResponse(datetime.date.today().day)


def month(request: HttpRequest):
    return HttpResponse(datetime.date.today().month)


def user_name(request: HttpRequest, name):
    return HttpResponse(f"Hello {name}!")
