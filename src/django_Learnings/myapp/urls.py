"""
1. Keep remmeber that this is not the exact urals.py file that created during the start 
2. This is app related url.py files 
3. If u create the url.py file in apps then you need to connect this url.py file to the main app url.py file in our case it is mysite 
"""

from . import views
from django.urls import path

urlpatterns = [
    path('' , views.index),
]
