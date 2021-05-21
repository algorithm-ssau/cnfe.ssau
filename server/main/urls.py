from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('index', views.index, name='home1'),
    path('treners', views.treners, name='treners'),
    path('master_classes', views.master_classes, name='master_classes'),

]