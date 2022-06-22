from django.shortcuts import render
import requests
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt



def index(request):
    return render(request,"index.html",{})
# Create your views here.

@csrf_exempt
def get_weather(request):
    print("========", request.POST)
    lat = request.POST['lat']
    lon = request.POST['lon']
    URL = "https://api.met.no/weatherapi/locationforecast/2.0/compact"
    PARAMS = {'lat':'51.5', 'lon': '0.25'}
    
    res = requests.get(url = URL, params = PARAMS)
    print("res:===============")
    print(res)
    return JsonResponse(res)
