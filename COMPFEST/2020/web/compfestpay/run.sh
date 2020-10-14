cd /home/compfest12/backend 
python3 manage.py makemigrations 
python3 manage.py migrate 
python manage.py loaddata seed
gunicorn backend.wsgi:application --bind 0.0.0.0:8000 &
python /home/compfest12/frontend/app.py