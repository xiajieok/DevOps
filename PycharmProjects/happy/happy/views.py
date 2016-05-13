from django.http import HttpResponse

def index(request):
    return HttpResponse(u"hello ni mei!")