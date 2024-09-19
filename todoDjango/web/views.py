from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    host = request.META['HTTP_HOST']
    user_agent = request.META['HTTP_USER_AGENT']
    path = request.path

    return HttpResponse(f'''
        <p>Host: {host}</p>
        <p>Path: {path}</p>
        <p>User-agent: {user_agent}</p>  
    ''')


def set_cookie(request):
    return HttpResponse()


def tasks(request):
    return HttpResponse('Все задачи')


def new_task(request):
    return HttpResponse('Добавление задачи')


def delete_task(request):
    return HttpResponse('Удаление задачи')