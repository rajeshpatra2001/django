from django.shortcuts import render, HttpResponse
from datetime import datetime
from home.models import Contact
from django.contrib import messages

def index(request):
    
    context = {
        'variable':"Variable Testing"
    }
    return render(request, "index.html", context)
    
    #return HttpResponse ("This is Home Page")

def about(request):
    return render(request, "about.html")
    #return HttpResponse ("Working towards a sustainable planet for the future not just by Ecological Conservation but by Emotional Sanity as well. Catch our unbiased and diversified outflow.")

def services(request):
    return render(request, "services.html")
    #return HttpResponse ("Ideas that shape the World. Ideas that stir the world.")

def services2(request):
    return render(request, "servicestwo.html")
    #return HttpResponse ("This is second service page")

def contact(request):
    
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        desc = request.POST.get('desc')
        contact = Contact(name= name, email= email, phone= phone, desc=desc)
        contact.save()  
        messages.success(request, 'We have heard you. We will be right back with the solution. Stay Tuned!')
    return render(request, "contacts.html")
    #return HttpResponse ("Website Hosted by: Rajesh Patra. Please Contact Phone: +91 8016999353, Email: rajeshpatra2001@gmail.com")


