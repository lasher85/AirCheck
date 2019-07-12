from django.urls import path
from . import views
from django.conf.urls import url
from .views import HomeView, get_data, ChartData_Krakow, ChartData_Tenczynek, ChartData_Katowice, ChartData_Krzeszowice, ChartData_Grudziadz, ChartData_Gdansk, ChartData_Gdynia
 
urlpatterns = [
    path('pm1/', views.pm1, name='pm1'),
    path('pm25/', views.pm25, name='pm25'),
    path('pm10/', views.pm10, name='pm10'),
    path('pressure/', views.pressure, name='pressure'),
    path('humidity/', views.humidity, name='humidity'),
    path('temperature/', views.temperature, name='temperature'),

    path('krakow_pm25_compare/', views.krakow_pm25_compare, name='krakow_pm25_compare'),
    path('krakow_pm10_compare/', views.krakow_pm10_compare, name='krakow_pm10_compare'),

    url(r'^$', HomeView.as_view(), name='home'),
    url(r'^api/data$', get_data, name='api-data'),
    url(r'^api/chart/Krakow_data$', ChartData_Krakow.as_view()),
    url(r'^api/chart/Tenczynek_data$', ChartData_Tenczynek.as_view()),
    url(r'^api/chart/Katowice_data$', ChartData_Katowice.as_view()), 
    url(r'^api/chart/Krzeszowice_data$', ChartData_Krzeszowice.as_view()), 
    url(r'^api/chart/Grudziadz_data$', ChartData_Grudziadz.as_view()), 
    url(r'^api/chart/Gdansk_data$', ChartData_Gdansk.as_view()), 
    url(r'^api/chart/Gdynia_data$', ChartData_Gdynia.as_view()), 
]