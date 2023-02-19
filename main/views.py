from django.http import HttpResponse, HttpResponseNotFound, Http404
from django.shortcuts import render, redirect

from .models import *

# Create your views here.
menu = ["Sait jaily" , "Pikir qosu", "Keri bailanys" , "Kiru"]

def index(request):
    posts = Kvart.objects.all()
    return render(request, 'main/index.html', {'posts':posts, 'menu': menu, 'title': 'Basty bet'})

def about(request):
    return render(request, 'main/about.html', {'menu': menu, 'title': 'Sait jaily'})


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
