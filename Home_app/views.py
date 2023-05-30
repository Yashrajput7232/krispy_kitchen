from django.shortcuts import render ,HttpResponse
from Home_app.models import *
from django.contrib import messages



# Create your views here.
def index(request):
    return render (request,"index.html")
    # return HHttpResponsettpResponse("This is our Home Page")
def contact(request):
    if (request.method=='POST'):
        name=request.POST.get('name')
        email=request.POST.get('email')
        phone=request.POST.get('phone')
        people=request.POST.get('people')
        date=request.POST.get('date')
        time=request.POST.get('time')
        message=request.POST.get('message')
        r=Reservations(name=name,email=email,phone=phone,people=people,date=date, time=time,message=message);
        r.save();
        messages.success(request, 'Your message has been sent.') 

    return render(request,'contact.html')
def review(request):
    if request.method=="POST":
        print("in review")
        name=request.POST.get('name')
        food=request.POST.get('food')
        review=request.POST.get('review')
        print(name,food,review)
        s=Review(name=name,food=food,review=review)
        s.save()
        messages.success(request, 'Your message has been sent.') 
    return render(request,'review.html')

def about(request):
    return render(request,'about.html')
def services (request):
    return render(request,'menu.html')
def news (request):
    return render(request,'news.html')
def news_detail (request):
    return render(request,'news-detail.html')

def franchise(request):
    if request.method=="POST":
        print("in review")
        name=request.POST.get('name')
        phone=request.POST.get('phone')
        email=request.POST.get('email')
        message=request.POST.get('message')
        print(name,phone,email,message)
        s=Franchise(name=name,phone=phone,email=email,message=message)
        s.save()
    return render(request,'franchise.html')