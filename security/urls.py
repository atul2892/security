from django.contrib import admin
from django.urls import path
from mainApp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.home),
    path('subscribtion/',views.subscribtion),
    path('about/',views.about),
    path('enquiry/',views.enquiry),
    path('contact/',views.contact),
    path('static-guard/',views.staticGuard),
    path('mobile-patrol/',views.mobilePatrol),
    path('event-security/',views.eventSecurity),
    path('retail-security/',views.retailSecurity),
    path('concierge-security/',views.conciergeSecurity),
    path('executive-protection/',views.executiveProtection),
    # path('social-media/',views.socialMedia),
    # path('email-marketing/',views.emailMarketing),
]
