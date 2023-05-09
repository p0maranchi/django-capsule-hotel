from django.shortcuts import render, redirect
from datetime import datetime, timedelta
from .models import *
from django.contrib import messages
from capsule.models import Capsule

peoplelist = [1,2,3,4,5]


def index(request):
    return render(request, "index.html",{})

def booking(request):
    dayA1 = dayMake(22, t=1)
    dayA2 = dayMake(22, t=2)
    names = Capsule.objects.all()
    if request.method == 'POST':
        capsule = request.POST.get('capsule')
        dayIn = request.POST.get('dayIn')
        dayOut = request.POST.get('dayOut')
        people = request.POST.get('people')
        if dayIn > dayOut:
            messages.error(request, "Неправильна дата!")
            return redirect('booking')

        request.session['dayIn'] = dayIn
        request.session['dayOut'] = dayOut
        request.session['capsule'] = capsule
        request.session['people'] = people

        return redirect('bookingSubmit')


    return render(request, 'booking.html', {
         'dayA1':dayA1, 
         'dayA2':dayA2, 
         'peoplelist': peoplelist,
         'names': names,
         })

def bookingSubmit(request):
    user = request.user

    dayIn = request.session.get('dayIn')
    dayOut = request.session.get('dayOut')
    capsule = request.session.get('capsule')
    people = request.session.get('people')
    names = Capsule.objects.get(name=capsule)
    price = int(names.price) * int(people) 

    if request.method == 'POST':
        booking = Booking.objects.get_or_create(
            user = user,
            capsule = capsule,
            dayIn = dayIn,
            dayOut = dayOut,
            price = price,
        )
        messages.success(request, "Бронювання збережено!")
        return redirect('index')
                         
    return render(request, 'bookingSubmit.html', {
        'capsule': capsule,
        'dayIn': dayIn,
        'dayOut': dayOut,
        'price': price,
        'people': people,
        
    })

def userPanel(request):
    user = request.user
    bookings = Booking.objects.filter(user=user).order_by('dayIn', 'dayOut')
    
    return render(request, 'userPanel.html', {
        'user':user,
        'bookings':bookings,
    })

def userUpdate(request, id):
    booking = Booking.objects.get(pk=id)
    userdatepicked = booking.dayIn
    today = datetime.today()
    
    delta24 = (userdatepicked).strftime('%Y-%m-%d') >= (today + timedelta(days=1)).strftime('%Y-%m-%d')
   
    dayA1 = dayMake(22, t=1)
    dayA2 = dayMake(22, t=2)
    names = Capsule.objects.all()
    if request.method == 'POST':
        capsule = request.POST.get('capsule')
        dayIn = request.POST.get('dayIn')
        dayOut = request.POST.get('dayOut')
        people = request.POST.get('people')
        if dayIn > dayOut:
            messages.error(request, "Wrong date!")
            return redirect('booking')

        request.session['dayIn'] = dayIn
        request.session['dayOut'] = dayOut
        request.session['capsule'] = capsule
        request.session['people'] = people

        return redirect('userUpdateSubmit', id=id)


    return render(request, 'userUpdate.html', {
            'dayA1':dayA1, 
            'dayA2':dayA2, 
            'delta24': delta24,
            'peoplelist': peoplelist,
            'id': id,
            'names': names,
        })

def userUpdateSubmit(request, id):
    
    user = request.user
    
    dayIn = request.session.get('dayIn')
    dayOut = request.session.get('dayOut')
    capsule = request.session.get('capsule')
    people = request.session.get('people')

    price = 250 * int(people)
    
    if request.method == 'POST':
        booking = Booking.objects.get_or_create(
            user = user,
            capsule = capsule,
            dayIn = dayIn,
            dayOut = dayOut,
            price = price,
        )
        messages.success(request, "Бронювання змінено!")
        return redirect('userPanel')


    return render(request, 'userUpdateSubmit.html', {
        'capsule': capsule,
        'dayIn': dayIn,
        'dayOut': dayOut,
        'price': price,
        'people': people,
        'id': id,
    })

def dayMake(days,t = 0):
    today = datetime.now()
    weekdays = []
    for i in range (t, days):
        x = today + timedelta(days=i)
        weekdays.append(x.strftime('%Y-%m-%d'))
    return weekdays