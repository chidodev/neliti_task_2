from django.shortcuts import render
import requests
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json



def index(request):
    return render(request,"index.html",{})
# Create your views here.

def get_weather(request):
    result = {'success': True, 'msg': ''}
    try:
        lat = request.POST['lat']
        lon = request.POST['lon']
        URL = "https://api.met.no/weatherapi/locationforecast/2.0/compact"
        PARAMS = {'lat': lat, 'lon': str(lon)}
        HEADERS = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Safari/537.36',
            'From': 'youremail@domain.example'
        }
        res = requests.get(url = URL, headers= HEADERS, params = PARAMS)
        json_data = json.loads(res.text)
        result['data'] = json_data
    except Exception as e:
        result['success'] = False
        result['msg'] = str(e)
        print(str(e))
    return JsonResponse(result)
