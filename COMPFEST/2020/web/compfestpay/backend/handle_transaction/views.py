

import os
from django.shortcuts import render
from django.contrib.auth.models import User
from django.http import HttpResponse, HttpResponseNotAllowed, HttpResponseServerError, JsonResponse
from django.views.decorators.http import require_http_methods
from .models import Transaction

@require_http_methods(["POST"])
def pay_someone(request):
	try:
		from_user = User.objects.get(username=request.POST.get('from'))
		to_user = User.objects.get(username=request.POST.get('to'))
		amount = int(request.POST.get('amount'))
		assert request.POST.get('from') != request.POST.get('to'), "You can't pay yourself"
		assert from_user.userwallet.signature == request.POST.get('signature'), "Invalid Signature"
		assert amount > 0, "You can't owe people lol"
		assert amount <= 5000000, "Dangerous amount"
		assert from_user.userwallet.value >= amount, "Not enough money"
		from_user.userwallet.value -= amount
		from_user.save()
		to_user.userwallet.value += amount
		to_user.save()
		new_transaction = Transaction(to_user=to_user.username, from_user=from_user.username, amount=amount)
		new_transaction.save()
		return HttpResponse('Transaction successful')
	except AssertionError as e:
		return HttpResponseServerError(str(e))
	except:
		return HttpResponseServerError("Error")

@require_http_methods(["POST"])
def buy_flag(request):
	try:
		user = User.objects.get(username=request.POST.get('from'))
		assert user.userwallet.signature == request.POST.get('signature'), "Invalid Signature"
		assert user.userwallet.value >= 1000000, "Not enough money"
		user.userwallet.value -= 1000000
		user.save()
		return HttpResponse('Flag: ' + os.environ.get('FLAG'))
	except AssertionError as e:
		return HttpResponseServerError(str(e))
	except:
		return HttpResponseServerError("Error")

@require_http_methods(["GET"])
def get_recent_transactions(request):
	try:
		username = request.GET.get('username')
		transactions = Transaction.objects.filter(to_user=username)
		json_data = []
		for transaction in transactions:
			json_data.append({'from': transaction.from_user, 'amount': transaction.amount})
		transactions.delete()
		return JsonResponse(json_data, safe=False)
	except:
		return HttpResponseServerError("Error")