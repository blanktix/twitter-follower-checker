from django.shortcuts import HttpResponse


def index(request):
    return(HttpResponse("Ini adalah halaman utama"))