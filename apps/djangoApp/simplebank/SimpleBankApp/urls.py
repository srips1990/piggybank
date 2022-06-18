from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home-page'),
    path('deposit', views.deposit, name='deposit'),
    path('grant_allowance', views.grant_allowance, name='grant_allowance'),
    path('withdraw', views.withdraw, name='withdraw'),
    path('get_allowance', views.get_allowance, name='get_allowance'),
    path('get_balance', views.get_balance, name='get_balance'),
    path('get_contract_balance', views.get_contract_balance, name='get_contract_balance')
]
