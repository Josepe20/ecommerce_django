from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect, HttpResponse
from django.db import IntegrityError
from django.contrib.auth import login, logout, authenticate
from .models import Profile, Cart


# Create your views here.
def register_page(request):

    if request.method == 'POST':
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        password = request.POST.get('password')

        try:
            user_obj = User.objects.create_user(
                first_name=first_name,
                last_name=last_name,
                email=email,
                username=email,
            )
            user_obj.set_password(password)
            user_obj.save()

            messages.success(request, "An email has been sent on your mail")
            return HttpResponseRedirect(request.path_info)

        except IntegrityError:
            user_obj = User.objects.filter(username=email)

            if user_obj.exists():
                messages.warning(request, "Email is already taken")
                return HttpResponseRedirect(request.path_info)

    return render(request, 'accounts/register.html')


def login_page(request):

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user_obj = User.objects.filter(username=username)

        if not user_obj.exists():
            print("Account not found")
            messages.warning(request, "Account not found")
            return HttpResponseRedirect(request.path_info)

        elif not user_obj[0].profile.is_email_verified:
            print("Your account is not verified yet")
            messages.warning(request, "Your account is not verified yet")
            return HttpResponseRedirect(request.path_info)

        else:
            user_obj = authenticate(request, username=username, password=password)
            print("login")
            login(request, user_obj)
            return redirect('/')

        messages.warning(request, "invalid credentials")
        return HttpResponseRedirect(request.path_info)

    return render(request, 'accounts/login.html')


def sing_out(request):
    logout(request)
    return redirect('/')


def activate_account(request, email_token):
    try:
        user = Profile.objects.get(email_token=email_token)
        user.is_email_verified = True
        user.save()

        return redirect('/')

    except Exception as e:
        return HttpResponse('Invalid Email token')


def cart(request):
    context = {'cart': Cart.objects.get(is_paid=False, user=request.user)}
    return render(request, 'accounts/cart.html', context=context)



