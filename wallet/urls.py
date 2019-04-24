from django.urls import path
from . import views

urlpatterns = [
    path('balance/<str:user_id>/', views.balance, name='balance'),
    path('list/', views.WalletList.as_view(), name='list'),
    path('create/', views.create, name='create'),
    path('login/', views.login, name='login'),
    path('transfer/', views.transfer, name='transfer'),
    path('deploy/', views.deploy, name='deploy'),
]
