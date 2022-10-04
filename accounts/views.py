from django.shortcuts import render, redirect
from django.contrib import auth, messages
from django.contrib.auth.models import User
from contact.models import Contact


def register(request):
    if request.method == 'POST':
        fname = request.POST['firstname']
        lname = request.POST['lastname']
        uname = request.POST['username']
        email = request.POST['email']
        pwd = request.POST['password']
        pwd2 = request.POST['password2']

        # check if password match
        if pwd == pwd2:
            # check username
            if User.objects.filter(username=uname).exists():
                messages.error(request, 'username already taken')
                return redirect('register')
            else:
                # check email
                if User.objects.filter(email=email).exists():
                    messages.error(request, 'email address already exists')
                    return redirect('register')
                else:
                    # create register object
                    user = User.objects.create_user(username=uname,
                            password=pwd, email=email, first_name=fname,
                            last_name=lname)

                    # login after register
                    # auth.login(request, user)
                    # messages.success(request, 'you are now logged in')
                    # return redirect('index')

                    user.save()
                    messages.success(request, 'registration successful')
                    return redirect('login')
        else:
            messages.error(request, 'password mismatch')
            return redirect('register')
    else:
        return render(request, 'accounts/register.html')


def login(request):
    if request.method == 'POST':
        uname = request.POST['username']
        upass = request.POST['password']

        user = auth.authenticate(username=uname, password=upass)
        if user is not None:
            auth.login(request, user)
            messages.success(request, 'login successful')
            return redirect('dashboard')
        else:
            messages.error(request, 'invalid user')
            return redirect('login')
    else:
        return render(request, 'accounts/login.html')


def dashboard(request):
    udish = Contact.objects.order_by('-contact_date')\
        .filter(user_id=request.user.id)
    context = {
        'contacts': udish
    }
    return render(request, 'accounts/dashboard.html', context)


def logout(request):
    if request.method == 'POST':
        auth.logout(request)
        messages.success(request, 'you are logged out')
        return redirect('index')
