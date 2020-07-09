from django.shortcuts import render,redirect
from django.http import HttpResponse,HttpResponseRedirect
from django.contrib import messages
from django.contrib.auth.models import User # To Create User In database
from django.contrib.auth import authenticate, login, logout # To Login User In Data Base
from . models import HomeSlide,Feature,Team
from . models import Gold_Plan, Platinum_Plan
from . models import EventsImage,EventStat
from math import ceil
from . models import Contact
# Create your views here.

def index(request) :
    homeslides = HomeSlide.objects.all()
    features = Feature.objects.all()
    goldplans = Gold_Plan.objects.all()
    platinumplans = Platinum_Plan.objects.all()
    teams = Team.objects.all()
    
    para = {'homeslide' : homeslides, 'feature' : features,'goldplan' : goldplans, 'platinumplan' : platinumplans,'team' : teams}
    return render(request, 'index.html',para)

def about(request) :
    eventstats = EventStat.objects.all()    # Grabbing All Objects From EventStat Model and Storing In Object
    para = {'eventstat' : eventstats}       # Passing That To an Variable of Dictionary 
    return render(request, 'about.html',para)   # Passing Dictionary Variable To render

def contact(request) :
    if request.method == 'POST' :
        fname = request.POST['fname']
        lname = request.POST['lname']
        email = request.POST['email']
        phone = request.POST['phone']
        msg = request.POST['msg']
        if len(phone) < 10 or fname == ""or lname == "" or email == "" or phone == "" or msg=="" :
            messages.error(request,"please Fill Form Correctly ")
        else :
            contact = Contact(fname = fname, lname = lname, email=email,phone=phone,msg=msg)
            contact.save()
            messages.success(request,"Success! Your Message Has Been Sent ")
            return redirect('contact')

    return render(request, 'contact.html')

def portfolio(request) :
    allevents = []
    catevents = EventsImage.objects.values('EI_category','EI_id')
    events = {item['EI_category'] for item in catevents}
    for eve in events :
        even = EventsImage.objects.filter(EI_category=eve)
        n = len(even)
        nslides = n//3 * ceil((n/3)-(n//3))
        allevents.append([even, range(1,nslides), nslides])
    para = {'allevents' : allevents}
    return render(request, 'portfolio.html',para)

def register(request) :
    if request.method == 'POST' :
        s_fname = request.POST['s_fname']
        s_lname = request.POST['s_lname']
        s_email = request.POST['s_email']
        s_phone = request.POST['s_phone']
        s_pass = request.POST['s_pass']
        s_cpass = request.POST['s_cpass']

        # Creating User 
        if len(s_phone) < 10 or len(s_pass) < 4 :
            messages.error(request," Wrong Contact Number ")
        elif  s_pass != s_cpass : 
            messages.error(request," Both Password Must Be Same ")
        elif not s_fname.isalnum() or not s_lname.isalnum() :
             messages.error(request," Enter Correct Name ")
        else :
            myuser = User.objects.create_user(s_email,s_email,s_pass)
            myuser.first_name = s_fname
            myuser.last_name = s_lname
            myuser.save()
            messages.success(request,"Your Account Has Been Created Succesfullt Now Login To Continue")
            return redirect('register')

    return render(request, 'register.html')

def loginhandel(request) :
    if request.method == 'POST' :
        login_email = request.POST['login_email']
        login_pass = request.POST['login_pass']

        user = authenticate(username = login_email, password = login_pass)
        if user is not None :
            login(request,user)
            messages.success(request,"Login Succesfull")
            return redirect('home')
        else :
            messages.error(request,"Login Failed! Plaease Enter Your Credentials Correctly ")
            return redirect('register')
    
    return HttpResponse('404 - Error')  # If Not Post Request Return 404  Error

def logouthandel(request) :
    logout(request)
    messages.success(request,"You have Loged Out Succesfully")
    return redirect('home')

    return HttpResponse("Logout")