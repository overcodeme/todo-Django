from django.http import HttpResponse

def index(request):
    host = request.META['HTTP_HOST']
    user_agent = request.META['HTTP_USER_AGENT']
    path = request.path

    return HttpResponse(f'''
        <p>Host: {host}</p>
        <p>Path: {path}</p>
        <p>User-agent: {user_agent}</p>  
    ''')


def contacts(request):
    return HttpResponse('<h1>Контакты</h1>')