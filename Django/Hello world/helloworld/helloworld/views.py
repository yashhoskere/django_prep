from django.http import HttpResponse

def helloworld(request):
    return HttpResponse('Hello everyone, Welcome to my channel')

def Wrong_url(request):
    return HttpResponse('Error 404')
    