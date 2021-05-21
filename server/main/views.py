from django.shortcuts import render


def index(request):
    return render(request, 'main/index.html')


def treners(request):
    return render(request, 'main/treners.html')
def master_classes(request):
    return render(request, 'main/master_classes.html')
