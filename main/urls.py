from django.urls import path
from . import views
from .views import *

urlpatterns = [
  path('', index),
  path('cats/<int:catid>/', categories),
  # path('errors403/', views.error403, name='403'),
  # path('errors404/', views.error403, name='404'),
  # path('errors400/', views.error403, name='400'),
  # path('errors500/', views.error403, name='500')

]