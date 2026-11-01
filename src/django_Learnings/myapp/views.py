from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
# view needs to accept the incomming request so we need to pass the paramenter 
# if you are passing the request then you need to know what response need to be returned 
# when ever you are sending the response you are sedding the http request for this we get an http response 


def index(request):
  return HttpResponse("Hello World") 