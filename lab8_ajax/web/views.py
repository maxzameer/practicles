from django.shortcuts import render

# Create your views here.

def home(req):
    a = 100
    b = 0
    c = a/b
    
    if req.method == 'POST':
        print("hello world")
        print(req.POST['user'])
    return render(req,"home.html") 
