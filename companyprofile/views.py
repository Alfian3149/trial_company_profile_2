from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return render(request, 'companyprofile/index.html')

def contactus(request):
    return render(request, 'companyprofile/contactus.html')

def qad_customization_list(request):
    return render(request, 'companyprofile/qad_customization_list.html')

def services(request):
    return render(request, 'companyprofile/services_list.html')
