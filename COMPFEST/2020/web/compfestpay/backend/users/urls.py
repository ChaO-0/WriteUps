

from django.urls import path, include
from .views import *

urlpatterns = [
    path('login/', login),
    path('register/', register),
    path('all_users/', get_all_users, name="all_users"),
    path('decode/', decode_jwt, name="decode"),
    path('wallet_signature/', get_wallet_signature, name="wallet_signature"),
    path('wallet_value/', get_wallet_value, name="wallet_value"),
    path('top_ten_users/', get_top_ten_users, name="top_ten_users"),
]