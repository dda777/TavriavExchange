from django.urls import path

from .views import *

urlpatterns = [
    path('', data_info, name='data_info'),
    path('enterprise/', enterprise_list, name='enterprise_list_url'),
]