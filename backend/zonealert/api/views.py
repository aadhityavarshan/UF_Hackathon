from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.http import HttpResponse



# @api_view(['GET'])
# def hello_world(request):
#     return Response({"message": "Hello, world!"})

def home(request):
    return HttpResponse("Hello, welcome to my site!")