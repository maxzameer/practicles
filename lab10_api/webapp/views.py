from django.shortcuts import render
import requests

def home(req):
    
    url = 'https://api.publicapis.org/entries'
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
       
    else:
        data = {'error': 'Failed to retrieve data from the API'}
    return render(req, 'index.html', {'data': data})
