from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    return HttpResponse('hello world!')


def runoob(request):
    context = {}
    context['hello'] = 'Hello World!'
    views_list = ['菜鸟教程1', '菜鸟教程2', '菜鸟教程3']
    context['views_list'] = views_list
    return render(request, 'runoob.html', context)