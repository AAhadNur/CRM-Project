from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
from django.contrib.auth.models import User

from .forms import MyUserCreationForm
from .models import UserProfile






def registerPage(request):
    form = MyUserCreationForm()

    if request.method == "POST":
        form = MyUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.username = user.username.lower()
            user.save()
            UserProfile.objects.create(user=user)
            login(request, user)
            return redirect('index')
        
        else:
            messages.error(request, 'An error occured during registration')
    
    context = {'form':form}

    return render(request, 'userprofile/signup.html', context)



def loginPage(request):

    if request.user.is_authenticated:
        return redirect('dashboard')
    
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        try:
            user = User.objects.get(username=username)
        except:
            messages.error(request, 'User does not exist')
        
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('dashboard')
        else:
            messages.error(request, 'Username or Password is not correct')

    return render(request, 'userprofile/login.html')



def logoutUser(request):
    logout(request)
    return redirect('index')
