from django.shortcuts import render, redirect
from django.contrib import messages
from . models import Contact
from django.core.mail import send_mail


def contact(request):
    if request.method == 'POST':
        dish_id = request.POST['dish_id']
        dish = request.POST['dish']
        name = request.POST['fullname']
        email = request.POST['email']
        phone = request.POST['phone']
        address = request.POST['address']
        user_id = request.POST['user_id']
        chef_email = request.POST['chef_email']

        contact = Contact(dish=dish, dish_id=dish_id, name=name,
                          email=email, phone=phone,
                          message=address, user_id=user_id)
        contact.save()

        # sending of mail
        # turn on lss secured settings in gmail account
        send_mail(
            'FOOD DELIVERY INQUIRY',
            'There has been an inquiry for'+ dish + '. Sign into the admin',
            'testemail@cryptonfttrademining.com',
            [chef_email],
            fail_silently=False
        )

        messages.success(request, 'your request is being processed')
        return redirect('/dish/' + dish_id)
    else:
        return redirect(request, 'dishes/dishes.html')
