

from django.urls import path, include
from .views import *

urlpatterns = [
    path('pay_someone/', pay_someone),
    path('buy_flag/', buy_flag),
    path('recent_transactions/', get_recent_transactions, name="recent_transactions"),
]