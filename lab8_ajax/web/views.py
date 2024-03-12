from django.shortcuts import render

# Create your views here.

def home(req):
    if req.method == 'POST':
        print("hello world")
        print(req.POST['user'])
    return render(req,"home.html") 
