from django.shortcuts import render
from django.http import  HttpResponse

def do_normalmap(request):
    print('in do_naomalmap')
    return HttpResponse('this is normalmap')
