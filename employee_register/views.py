from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages



def home(request):
    #check to see if logging in
    if request.method == "POST":
       username = request.POST['username']
       password = request.POST['password']
       #Authenticate
       user = authenticate(request, username=username, password=password)
       if user is not None:
           login(request, user)
           messages.success(request, "You have been logged In")
           return redirect('home')
       else:
           messages.success(request, 'there was an error login In, Please try again...')
    else:     
        return render(request, 'home.html', {})



def logout_user(request):
    logout(request)
    messages.success(request, 'You have been logged Out...')
    return redirect('home')


def register_user(request):
     return render(request, 'register.html', {})
    
    