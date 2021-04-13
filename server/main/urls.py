from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('treners', views.treners, name='treners'),

]