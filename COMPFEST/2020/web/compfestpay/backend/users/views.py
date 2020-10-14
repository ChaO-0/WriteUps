

import os
from datetime import datetime, timedelta
from django.shortcuts import render
from django.contrib.auth.models import User
from django.http import HttpResponse, HttpResponseServerError, JsonResponse
from django.views.decorators.http import require_http_methods
from jwt import encode, decode
from .models import UserWallet


@require_http_methods(["POST"])
def login(request):
	username = request.POST.get('username')
	password = request.POST.get('password')
	try:
		jwt = init_auth_token(username, password)
		return HttpResponse(jwt, status=200)
	except:
		return HttpResponseServerError("Error")


@require_http_methods(["POST"])
def register(request):
	try:
		username = request.POST.get('username')
		password = request.POST.get('password')
		assert len(username) <= 200, "Username too long"
		assert len(password) <= 200, "Password too long"
		user = User(username=username, password=password)
		user.save()
		jwt = init_auth_token(username, password)
		return HttpResponse(jwt)
	except AssertionError as e:
		return HttpResponseServerError(str(e))
	except:
		return HttpResponseServerError("Error")

@require_http_methods(["POST"])
def decode_jwt(request):
	try:
		jwt = request.POST.get('jwt')
		jwt = decode(jwt, key=os.environ.get('SECRET_KEY'))
		return HttpResponse(jwt['sub']['username'])
	except:
		return HttpResponseServerError("Error")

@require_http_methods(["GET"])
def get_all_users(request):
	users = list(User.objects.values('username'))
	return JsonResponse(users, safe=False)

@require_http_methods(["GET"])
def get_wallet_signature(request):
	try:
		username = request.GET.get('username')
		user = User.objects.get(username=username)
		signature = user.userwallet.signature
		return HttpResponse(signature)
	except:
		return HttpResponseServerError("Error")

@require_http_methods(["GET"])
def get_wallet_value(request):
	try:
		username = request.GET.get('username')
		user = User.objects.get(username=username)
		value = user.userwallet.value
		return HttpResponse(value)
	except:
		return HttpResponseServerError("Error")

@require_http_methods(["GET"])
def get_top_ten_users(request):
	top_values = UserWallet.objects.order_by('-value').values('id', 'value')[:10]
	top_users = []
	for i in top_values:
		top_users.append({'username': User.objects.get(id=i['id']).username, 'value': i['value']})
	return JsonResponse(top_users, safe=False)

def init_auth_token(username, password):
	uid = User.objects.get(username=username, password=password).id
	username = User.objects.get(username=username, password=password).username
	jwt = {'exp': datetime.utcnow() + timedelta(days=14, minutes=0), 'iat': datetime.utcnow(), 'sub': {"id" : uid, "username" : username}}
	return encode(jwt, os.environ.get('SECRET_KEY'), algorithm='HS256')