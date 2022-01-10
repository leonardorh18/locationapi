from django.shortcuts import render
from bs4 import BeautifulSoup
import requests
# Create your views here.
from django.http import response
from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse, Http404
import re

def getLatLong(req, address):
    print("HEREE")
    print(address)
    try:
        rua = "potiguara"
        bairro = "Colatto"
        cidade = "Xanxere"
        nmr = "499"
        pais = "Brasil"
        estado = 'Santa Catarina'
        #response = requests.get(f'https://www.bing.com/maps/overlaybfpr?q=rua%20{rua}%20{nmr}%2C%20{cidade}%20{estado}%20{pais}')
        resp = requests.get(f'https://www.bing.com/maps/overlaybfpr?q={address}')
        
        soup = BeautifulSoup(resp.content, "html.parser")
        lat = soup.find("div", class_= 'geochainModuleLatLong')
        print(lat.text)
        coordList = lat.text.split(',')
        lat = coordList[0] + '.' + coordList[1]
        lon = coordList[2] + '.' + coordList[3]
        lon = re.sub(' ', '', lon)
        
        
    except Exception as e:
        raise Http404("Erro ao buscar as coordenadas!", e)

    return JsonResponse({'lat': lat, 'long': lon})