from django.shortcuts import render

from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm

# Create your views here.

def signin(req):
    
     if req.method == 'POST':
        username = req.POST['username']
        password = req.POST['password']
        user = authenticate(req, username=username, password=password)
        if user is not None:
            login(req, user)
            return redirect('/home')
        else:
            return render(req, 'login.html', {'error': 'Invalid credentials'})
     else:
        return render(req, 'login.html')
    
    
    
def signup(req):
    if req.method == 'POST':
        form = UserCreationForm(req.POST)
        if form.is_valid():
            form.save()
            return redirect('/login')
    else:
        form = UserCreationForm()
    return render(req, 'signup.html', {'form': form})



def home(req):
    if req.method == "POST":
        logout(req)
        return redirect('/login')
        
    if req.user.is_authenticated:        
        return render(req, 'user.html',{'message': req.user})
    
    else:        
        return redirect('/login')
    
    
    

    