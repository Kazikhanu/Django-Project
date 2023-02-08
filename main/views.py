from django.http import HttpResponse, HttpResponseNotFound, Http404
from django.shortcuts import render, redirect


# Create your views here.


def index(request):
    return render(request, 'main/index.html')


def categories(request , catid):
    if (catid > 10):
        return redirect('home' , permanent=False)
    if(request.GET):
        print(request.GET)
    return HttpResponse(f"<h1>Vibor tipa doma</h1><p>{catid}</p>")



def pageNotFound(request , exception):
    #404
    return HttpResponseNotFound('<h1>Page not Found</h1>')
def accessDenied(request , exception):
    #403
    return HttpResponseNotFound('<h1>Access Denied</h1>')

def unabletoProcessServer(request , exception):
    #400
    return HttpResponseNotFound('<h1>Unable to Process Server</h1>')

def serverError(request , exception):
    #500
    return HttpResponseNotFound('<h1>Server Error</h1>')
