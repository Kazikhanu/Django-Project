
from django.contrib import admin
from django.urls import path, include

from main.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('main.urls')),
    path('about/', about, name='about'),

]

handler404 = pageNotFound
handler403 = accessDenied
handler400 = unabletoProcessServer
handler400 = serverError

