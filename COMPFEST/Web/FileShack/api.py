from django.http import JsonResponse, Http404
from django.views.static import serve
from .models import File

import os


def list(request):
    file_list = File.objects.order_by('id')
    token_list = []
    for file in file_list:
        token_list.append(file.token)
    return JsonResponse({"Token": token_list})


def download(request, token):
    file_path = None

    try:
        # Protection against "SQL Injection"
        token = token.replace('\'', '')
        token = token.replace(';', '')
        token = token.replace('\\', '')
        file_list = File.objects.raw('SELECT * FROM fileboard_file WHERE token="%s"' % token)
        for file in file_list:
            file_path = file.file_path
    except:
        raise Http404

    if file_path:
        file_dir = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
        file_path = file_dir + '/files/' + file_path
        request.session['last_viewed'] = token
        return serve(request, file_path, '/')
    else:
        raise Http404
