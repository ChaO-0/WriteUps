from flask import Flask, render_template, request, render_template_string, session, url_for, redirect, make_response
import sys
import jwt
jwt.algorithms.HMACAlgorithm.prepare_key = lambda self, key : jwt.utils.force_bytes(key) # was causing problems
import os
import random
import collections
import hashlib

app = Flask(__name__, template_folder="templates")
app.secret_key = os.urandom(24)

BOSS_HORSE = "MechaOmkar-YG6BPRJM"

with open("pubkey.pem", "rb") as file:
    PUBLIC_KEY = file.read()

with open("privkey.pem", "rb") as file:
    PRIVATE_KEY = file.read()

Horse = collections.namedtuple("Horse", ["name", "price", "id"])
next_id = 0
valid_horses = {}
with open("horse_names.txt", "r") as file:
    for name in file.read().strip().split("\n"):
        valid_horses[next_id] = Horse(name, 100, next_id)
        next_id += 1

with open("flag.txt", "r") as file:
    flag = file.read()

def validate_token(token):
    try:
        data = jwt.decode(token, PUBLIC_KEY)
        return all(attr in data for attr in ["user","is_omkar","money","horses"]), data
    except:
        return False, None

def generate_token(data):
    token = jwt.encode(data, PRIVATE_KEY, "RS256")
    return token

@app.route("/")
def main_page():
    if "token" in request.cookies:
        is_valid, data = validate_token(request.cookies["token"])
        if is_valid:
            return render_template("main.html", money=data["money"])
        else:
            response = make_response(render_template("new_user.html"))
            response.delete_cookie("token")
            return response
    else:
        return render_template("new_user.html")

@app.route("/join")
def join():
    data = {
        "user": True,
        "is_omkar": False,
        "money": 100,
        "horses": []
    }
    response = make_response(redirect("/"))
    response.set_cookie("token", generate_token(data))
    return response

@app.route("/race")
def race():
    if "token" in request.cookies:
        is_valid, data = validate_token(request.cookies["token"])
        if is_valid:
            error_message = ("error" in request.args)
            owned_horses = data["horses"]
            return render_template("race.html", owned_horses=owned_horses, money=data["money"], \
                boss_horse=BOSS_HORSE, error_message=error_message)
        else:
            return redirect("/")
    else:
        return redirect("/")

@app.route("/do_race")
def do_race():
    if "token" in request.cookies:
        is_valid, data = validate_token(request.cookies["token"])
        if is_valid:
            if "horse" in request.args:
                race_horse = request.args.get("horse")
            else:
                return redirect("/race")
            owned_horses = data["horses"]
            if race_horse not in owned_horses:
                return redirect("/race?error")

            boss_speed = int(hashlib.md5(("Horse_" + BOSS_HORSE).encode()).hexdigest(), 16)
            your_speed = int(hashlib.md5(("Horse_" + race_horse).encode()).hexdigest(), 16)
            if your_speed > boss_speed:
                return render_template("race_results.html", money=data["money"], victory=True, flag=flag)
            else:
                return render_template("race_results.html", money=data["money"], victory=False)
        else:
            return redirect("/")
    else:
        return redirect("/")

@app.route("/store")
def store():
    if "token" in request.cookies:
        is_valid, data = validate_token(request.cookies["token"])
        if is_valid:
            success_message = ("success" in request.args)
            failure_message = ("failure" in request.args)
            all_horse_ids = list(valid_horses.keys())
            random.shuffle(all_horse_ids)
            horses = [valid_horses[horse_id] for horse_id in all_horse_ids[:random.randint(4,6)]]
            return render_template("store.html", horses=horses, money=data["money"], \
                success_message=success_message, failure_message=failure_message)
        else:
            return redirect("/")
    else:
        return redirect("/")

@app.route("/buy_horse")
def buy_horse():
    if "token" in request.cookies:
        is_valid, data = validate_token(request.cookies["token"])
        if is_valid:
            if "id" in request.args:
                buy_id = int(request.args.get("id"))
            else:
                response = make_response(redirect("/store?failure"))
                return response

            if data["money"] >= valid_horses[buy_id].price:
                data["money"] -= valid_horses[buy_id].price
                data["horses"].append(valid_horses[buy_id].name)
                response = make_response(redirect("/store?success"))
                response.set_cookie("token", generate_token(data))
                return response
            else:
                response = make_response(redirect("/store?failure"))
                return response
        else:
            return redirect("/")
    else:
        return redirect("/")


if __name__ == "__main__":
    app.run(debug=False) 
