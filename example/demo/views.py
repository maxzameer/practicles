from django.shortcuts import render

# Create your views here.
def home(response):
  
    if response.method == "POST":
        print(response.POST['user'])
        print(response.POST['password'])
    
    return render(response,"home.html")
