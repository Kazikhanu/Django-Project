from django.urls import path
from . import views
from .views import *

urlpatterns = [
  path('', index , name='home'),
  path('cats/<int:catid>/', categories),

]