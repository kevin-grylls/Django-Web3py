from django.urls import path
from . import views

urlpatterns = [
    path('balance/<str:user_id>/', views.balance, name='balance'),
    path('list/', views.WalletList.as_view(), name='list'),
    path('create/', views.create, name='create'),
    path('login/', views.login, name='login'),
    path('transfer_ether/', views.transfer_ether, name='transfer_ether'),
    path('transfer_token/', views.transfer_token, name='transfer_token'),
    path('transfer_token_from/', views.transfer_token_from,
         name='transter_token_from'),
    path('deploy/', views.deploy, name='deploy'),
    path('all_functions/', views.all_functions, name='all_functions'),
    path('balance_of/', views.balance_of, name='balance_of'),
    path('balance_of_all/', views.balance_of_all, name='balance_of_all'),
    path('total_supply/', views.total_supply, name='total_supply'),
    path('unlock_all/', views.unlock_all, name='unlock_all'),
    path('get_coinbase/', views.get_coinbase, name='get_coinbase'),
    path('set_miner/', views.set_miner, name='set_miner'),
    path('status_miner/', views.status_miner, name='status_miner'),
    path('get_latest_block/', views.get_latest_block, name='get_latest_block'),
    path('get_transaction_of/', views.get_transaction_of,
         name='get_transaction_of'),
    path('get_transaction_all/', views.get_transaction_all,
         name='get_transaction_all'),
    path('transaction_list/', views.TransactionList.as_view(),
         name='transaction_list'),
]
