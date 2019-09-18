#!/usr/bin/env python3

from flask import Flask, session, redirect, url_for, escape, request, send_file, render_template
from uuid import uuid4
from PIL import Image
from io import BytesIO
import base64
import os
import pickle
import redis
import urllib.request

app = Flask(__name__)
app.secret_key = os.getenv('SECRET_KEY')
app.session_cookie_name = 'olivia_session'
redis_db = redis.from_url('redis://redis:6379')

@app.route('/', methods=['GET', 'POST'])
def index():
    if 'sid' not in session:
        session['sid'] = str(uuid4())
    sid = session['sid']

    if request.method == 'GET':
        return render_template('index.html', sid=sid)

    url = str(request.form['url'])
    if not url or not url.startswith('http'):
        return redirect(url_for('index'))

    try:
        cache_key = f'{sid}:{url}'
        cache = redis_db.get(cache_key)
        if cache is None:
            with urllib.request.urlopen(url, timeout=3.0) as res:
                image = Image.open(BytesIO(res.read()))
            image = image.resize((64,64))
            image = image.convert('L')

            image_io = BytesIO()
            image.save(image_io, format='JPEG', optimize=True)
            image_io.seek(0)

            cache = base64.b64encode(pickle.dumps(image_io))
            redis_db.set(cache_key, cache, ex=60)
        else:
            image_io = pickle.loads(base64.b64decode(cache))
    except Exception as e:
        return escape(repr(e))

    return send_file(image_io, mimetype='image/jpeg')

if __name__ == '__main__':
    app.run(host='0.0.0.0')
