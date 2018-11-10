from django.shortcuts import render
from  django.http import HttpResponse

# Create your views here.
def do_normalmap(request):
    return HttpResponse('this is normalmap')