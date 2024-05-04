from django.shortcuts import render,redirect
from django.contrib import messages

def home(Request):
    return render(Request,"index.html")

def subscribtion(Request):
    if(Request.method=="POST"):
        messages.success(Request,"“Subscribed Successfully”")
    return redirect("/")

def about(Request):
    return render(Request,"about.html")

def enquiry(Request):
    if(Request.method=="POST"):
        messages.success(Request,"“Your form submitted Successfully”")
    return render(Request,"enquiry.html")

def contact(Request):
    if(Request.method=="POST"):
        messages.success(Request,"“Your form submitted Successfully”")
    return render(Request,"contact.html")

def staticGuard(Request):
    return render(Request,"static-guard.html")

def mobilePatrol(Request):
    return render(Request,"mobile-patrol.html")

def eventSecurity(Request):
    return render(Request,"event-security.html")

def retailSecurity(Request):
    return render(Request,"retail-security.html")

def conciergeSecurity(Request):
    return render(Request,"concierge-security.html")

def executiveProtection(Request):
    return render(Request,"executive-protection.html")

# def socialMedia(Request):
#     return render(Request,"social-media.html")

# def emailMarketing(Request):
#     return render(Request,"email-marketing.html")



