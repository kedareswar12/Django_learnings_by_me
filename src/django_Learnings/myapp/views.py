from django.shortcuts import render
from django.http import HttpResponse
from .models import Item

# Create your views here.
# view needs to accept the incomming request so we need to pass the paramenter 
# if you are passing the request then you need to know what response need to be returned 
# when ever you are sending the response you are sedding the http request for this we get an http response 


def index(request):
  # queryset = model + manager + method 
  Items_list = Item.objects.all() #queryset 
  return HttpResponse(Items_list) 

def item(request):
  return HttpResponse("<h1>This is an Item View</h1>")
  #here httpresonce could able to send the html responses to server but the good way is to create a templetes 