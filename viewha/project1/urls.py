from django.urls import path
from .views import *

urlpatterns = [
    path('', data_view, name='data_view'),
    path('form/', form_view, name='form_view'),
    path('data/', data_view, name='data_view'),
    path('form/add/', add_data, name='add_data'),
    path('success.html', success_view, name='success_view')
]
