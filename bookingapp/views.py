import datetime
from decimal import Decimal
from email import message
from pyexpat.errors import messages

from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect
from .forms import UserLoginForm, UserRegFrom,FindbusForm,BookForm,Addbus,datesearchForm
from django.shortcuts import render, redirect
from django.contrib.auth.models import User


# Create your views here.
from .models import Bus,Book


def home(request):
    form=UserLoginForm
    if request.user.is_authenticated:
        # return render(request, 'myapp/home.html')
        return HttpResponse("ok")
    else:
        return HttpResponse("sorry")
        # return render(request, 'myapp/signin.html')
    # return render(request,'login.html',{'form':form})
def view_login(request):
    context={}
    form=UserLoginForm
    context={'form':form}
    if request.method=='POST':
        form=UserLoginForm(request.POST)
        if form.is_valid():
            context={}
            username=form.cleaned_data.get("username")
            password=form.cleaned_data.get("password")
            user=authenticate(username=username,password=password)
            if user:
                if username=='admin':
                    return render(request,'admin_index.html')
                login(request,user)
                context["user"] =username
                context["id"] = request.user.id
                print(context)
                return render(request,'user_index.html',context)
            #
            # elif admin:
            #     login(request,admin)
            #     return HttpResponse("admin")
            else:
                messages.info(request, 'Your password has been changed successfully!')
                return HttpResponseRedirect('signin')
                # messages.info(request, 'Login Successfull!')
                # login(request, user)
        else:
            form=UserLoginForm()
    return render(request,'login.html',context)
def signup(request):
    form=UserRegFrom
    context={}
    context["form"]=form
    if request.method=='POST':

        form=UserRegFrom(request.POST)
        if form.is_valid():
            print(form)
            form.save()
            return HttpResponseRedirect('signin')
        else:
            form=UserRegFrom(request.POST)
            context["form"]=form
            return HttpResponse("sorry")
            return HttpResponseRedirect('start')

    return render(request,'signup.html',context)

@login_required(login_url='signin')
def findbus(request):
    context={}
    form1=FindbusForm
    form2=BookForm
    context={'form':form1}
    if request.method=='POST':
        ob1=FindbusForm(request.POST)
        source_r=ob1['source'].value()
        dest_r=ob1['dest'].value()
        date_r=ob1['date'].value()
        bus_list=Bus.objects.filter(source=source_r, dest=dest_r, date=date_r)
        if bus_list:
            return render(request,'bus_list.html',{'list':bus_list,'form3':form2})
        else:
            # message.info(request,"No Buses are avaialable....Please try with another date")
            return redirect(findbus)
    return render(request,'findbus.html',context)

@login_required(login_url='signin')
def bookings(request):
    context = {}
    if request.method == 'POST':
        form=BookForm(request.POST)
        id_r = form['id'].value()
        seats_r = form['nos'].value()
        bus = Bus.objects.get(id=id_r)
        if bus:
            if bus.rem > int(seats_r):
                name_r = bus.bus_name
                cost = int(seats_r) * bus.price
                source_r = bus.source
                dest_r = bus.dest
                nos_r = Decimal(bus.nos)
                price_r = bus.price
                date_r = bus.date
                time_r = bus.time
                username_r = request.user.username
                email_r = request.user.email
                userid_r = request.user.id
                rem_r = bus.rem-Decimal(seats_r)
                Bus.objects.filter(id=id_r).update(rem=rem_r)
                book = Book.objects.create(name=username_r, email=email_r, userid=userid_r,  bus_name=name_r,
                                           source=source_r, busid=id_r,
                                           dest=dest_r, price=price_r, nos=nos_r, date=date_r, time=time_r,status='BOOKED')
                print('------------book id-----------', book.id)
                # book.save()
                return render(request,'success.html')
            else:
                # context["error"] = "Sorry select fewer number of seats"
                return HttpResponse("sorry")

    else:
        return render(request, 'login.html')

#view Booking
@login_required(login_url='signin')
def seebooking(request,new={}):
    context={}
    id_r=request.user.id
    booklist=Book.objects.filter(userid=id_r)
    if booklist:
        return render(request,'view_booking.html',locals())
    else:
        return HttpResponse("no booking")

#cancel ticket
def cancellation(request,id):
    book=Book.objects.get(id=id)
    bus=Bus.objects.get(id=book.busid)
    rem_r=bus.rem+book.nos
    Bus.objects.filter(id=book.busid).update(rem=rem_r)
    Book.objects.filter(id=id).update(status='CANCELLED')
    Book.objects.filter(id=id).update(nos=0)
    return redirect(seebooking)
#view ticket
def viewticket(request,id):
    context={}
    book=Book.objects.get(id=id)
    context={'ticket':book}
    return render(request,'view_ticket.html',context)

#add bus (admin)
def addbus(request):
    context={}
    form=Addbus
    context={'form':form}
    if request.method=='POST':
        form=Addbus(request.POST)
        if form.is_valid():
            form.save()
            return render(request,'bus_success.html')
        else:
            return HttpResponse("form invalid")
    return render(request,'add_bus.html',context)
#view bus
def viewbus(request):
    ob2=Bus.objects.all()
    return render(request,'view_bus.html',{'list':ob2})


#delete bus
def deletebus(request,id):
    ob1=Bus.objects.get(id=id)
    ob1.delete()
    return redirect(viewbus)

#update bus

def updatebus(request,id):
    b1=Bus.objects.get(id=id)
    form=Addbus(instance=b1)
    context={}
    context['form']=form
    if request.method=='POST':
        form=Addbus(request.POST,instance=b1)
        if form.is_valid():
            form.save()
            return redirect(viewbus)
    return render(request,'busedit.html',context)

#total booking
def totalbooking(request):
    ob1=Book.objects.all()
    return render(request,'total_booking.html',{'list':ob1})

#Today booking
def todaybooking(request):
    context={}
    date=datetime.date.today()
    ob1=Book.objects.filter(date=date)
    if ob1:
        context['list']=ob1
        return render(request, 'today_booking.html', context)
    else:
        return HttpResponse("No Booking")

def logout_view(request):
    logout(request)
    return HttpResponseRedirect('signin')

def view_user(request):
    context={}
    ob1=User.objects.all()
    context['list']=ob1
    return render(request,'view_users.html',context)