from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.视图
'''
视图函数需要一个参数，类型应该是HttpRequest
'''

def do_normalmap():
    return HttpResponse('this is noamalmap')

