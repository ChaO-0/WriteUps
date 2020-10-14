#!/usr/bin/env python3

from flask import Flask, request, render_template, make_response, redirect
from requests import get, post
from functools import wraps
import json

app = Flask(__name__)

@app.route('/', methods=['GET'])
def index():
	top_ten_users = get_top_ten_users()
	all_users = get_all_users()
	if 'jwt' in request.cookies:
		username = decode_jwt(request.cookies.get('jwt'))
		wallet_value = get_wallet_value(username)
		wallet_signature = get_wallet_signature(username)
		recent_transactions = get_recent_transactions(username)
		return render_template('index.html', username=username, wallet_value=wallet_value, wallet_signature=wallet_signature, top_ten_users=top_ten_users, all_users=all_users, recent_transactions=recent_transactions, active="index")
	else:
		return render_template('index.html', top_ten_users=top_ten_users, all_users=all_users, active="index")

@app.route('/login', methods=['GET', 'POST'])
def login():
	if 'jwt' in request.cookies:
		return redirect('/')
	if request.method == 'POST':
		data = {'username': request.form.get('username'), 'password': request.form.get('password')}
		r = post('http://localhost:8000/users/login/', data=data)
		if r.status_code == 200:
			res = make_response(redirect('/'))
			res.set_cookie('jwt', r.text, httponly = True)
			return res
		else:
			return render_template('login.html', error="Invalid Username/Password", active="login")
	else:
		return render_template('login.html', active="login")

@app.route('/register', methods=['GET', 'POST'])
def register():
	if 'jwt' in request.cookies:
		return redirect('/')
	if request.method == 'POST':
		data = {'username': request.form.get('username'), 'password': request.form.get('password')}
		r = post('http://localhost:8000/users/register/', data=data)
		if r.status_code == 200:
			res = make_response(redirect('/'))
			res.set_cookie('jwt', r.text, httponly = True)
			return res
		else:
			return render_template('register.html', error="Username Taken", active="register")
	else:
		return render_template('register.html', active="register")

@app.route('/logout', methods=['GET'])
def logout():
	res = make_response(redirect('/'))
	res.delete_cookie('jwt')
	return res

@app.route('/pay', methods=['POST'])
def pay():
	if 'jwt' in request.cookies:
		jwt_user = decode_jwt(request.cookies.get('jwt'))
		if(jwt_user != request.form.get('from')):
			return "Go away hacker!", 500
		real_signature = get_wallet_signature(request.form.get('from'))
		if(real_signature != request.form.get('signature')):
			return "Go away hacker!", 500
		r = post('http://localhost:8000/transaction/pay_someone/', data=dict(request.form.lists()))
		return r.text, r.status_code
	else:
		return redirect('/')

@app.route('/flag', methods=['POST'])
def buy_flag():
	if 'jwt' in request.cookies:
		jwt_user = decode_jwt(request.cookies.get('jwt'))
		if(jwt_user != request.form.get('from')):
			return "Go away hacker!"
		real_signature = get_wallet_signature(request.form.get('from'))
		if(real_signature != request.form.get('signature')):
			return "Go away hacker!"
		r = post('http://localhost:8000/transaction/buy_flag/', data=dict(request.form.lists()))
		return r.text, r.status_code
	else:
		return redirect('/')

def decode_jwt(jwt):
	r = post('http://localhost:8000/users/decode/', data={'jwt': jwt})
	return r.text

def get_wallet_signature(username):
	r = get('http://localhost:8000/users/wallet_signature/', params={'username': username})
	return r.text

def get_wallet_value(username):
	r = get('http://localhost:8000/users/wallet_value/', params={'username': username})
	return r.text

def get_recent_transactions(username):
	r = get('http://localhost:8000/transaction/recent_transactions/', params={'username': username})
	if r.status_code == 200:
		return json.loads(r.text)
	else:
		return ""

def get_top_ten_users():
	r = get('http://localhost:8000/users/top_ten_users/')
	if r.status_code == 200:
		return json.loads(r.text)
	else:
		return ""

def get_all_users():
	r = get('http://localhost:8000/users/all_users/')
	if r.status_code == 200:
		return json.loads(r.text)
	else:
		return ""

if __name__ == "__main__":
	app.run(host='0.0.0.0', port=8080, debug=False)
