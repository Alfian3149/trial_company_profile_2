from django.urls import path
from companyprofile import views

urlpatterns = [
    path('', views.index, name='index'),
    path('contact-us', views.contactus, name='contactus'),
    path('services', views.services, name='services'),
    path('qad-customization-list', views.qad_customization_list, name='qad_customization_list'),

]