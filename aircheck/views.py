# -*- coding: utf-8 -*-

from django.views.generic import TemplateView 
from .models import Krakow, Tenczynek, Katowice, Krzeszowice, Grudziadz, Gdansk, Gdynia
from django.views.generic import View
from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.views import APIView 
from rest_framework.response import Response
from aircheck.serializers import KrakowSerializer, TenczynekSerializer, KatowiceSerializer, KrzeszowiceSerializer, GrudziadzSerializer, GdanskSerializer, GdyniaSerializer

class HomeView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'pm1.html', {})

def get_data(request, *args, **kwargs):
    return JsonResponse(data) 

class ChartData_Krakow(APIView):

    def get(self, request, format=None):
       
        list_model = Krakow.objects.all().order_by('data')
        serializer = KrakowSerializer(list_model, many=True)
 
        return Response(serializer.data)
 
class ChartData_Tenczynek(APIView):

    def get(self, request, format=None):
       
        list_model = Tenczynek.objects.all().order_by('data')
        serializer = TenczynekSerializer(list_model, many=True)
 
        return Response(serializer.data)

class ChartData_Katowice(APIView):

    def get(self, request, format=None):
       
        list_model = Katowice.objects.all().order_by('data')
        serializer = KatowiceSerializer(list_model, many=True)
 
        return Response(serializer.data)

class ChartData_Krzeszowice(APIView):

    def get(self, request, format=None):
       
        list_model = Krzeszowice.objects.all().order_by('data')
        serializer = KrzeszowiceSerializer(list_model, many=True)
 
        return Response(serializer.data)

class ChartData_Grudziadz(APIView):

    def get(self, request, format=None):
       
        list_model = Grudziadz.objects.all().order_by('data')
        serializer = GrudziadzSerializer(list_model, many=True)
 
        return Response(serializer.data)

class ChartData_Gdansk(APIView):

    def get(self, request, format=None):
       
        list_model = Gdansk.objects.all().order_by('data')
        serializer = GdanskSerializer(list_model, many=True)
 
        return Response(serializer.data)

class ChartData_Gdynia(APIView):

    def get(self, request, format=None):
       
        list_model = Gdynia.objects.all().order_by('data')
        serializer = GdyniaSerializer(list_model, many=True)
 
        return Response(serializer.data)

# Pre-configured views.

pm1 = TemplateView.as_view(template_name='pm1.html')
pm25 = TemplateView.as_view(template_name='pm25.html')
pm10 = TemplateView.as_view(template_name='pm10.html')
pressure = TemplateView.as_view(template_name='pressure.html')
humidity = TemplateView.as_view(template_name='humidity.html')
temperature = TemplateView.as_view(template_name='temperature.html')

krakow_pm25_compare = TemplateView.as_view(template_name='krakow_pm25_compare.html')
krakow_pm10_compare = TemplateView.as_view(template_name='krakow_pm10_compare.html')