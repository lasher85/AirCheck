from django.db import models

# Create your models here.

class Tenczynek(models.Model):
    data = models.DateTimeField(primary_key=True)
    pm1 = models.FloatField()
    pm25 = models.FloatField()
    pm10 = models.FloatField()
    pressure = models.FloatField()
    humidity = models.FloatField()
    temperature = models.FloatField()

class Krakow(models.Model):
    data = models.DateTimeField(primary_key=True)
    pm1 = models.FloatField()
    pm25 = models.FloatField()
    pm10 = models.FloatField()
    pressure = models.FloatField()
    humidity = models.FloatField()
    temperature = models.FloatField()

class Katowice(models.Model):
    data = models.DateTimeField(primary_key=True)
    pm1 = models.FloatField()
    pm25 = models.FloatField()
    pm10 = models.FloatField()
    pressure = models.FloatField()
    humidity = models.FloatField()
    temperature = models.FloatField()

class Krzeszowice(models.Model):
    data = models.DateTimeField(primary_key=True)
    pm1 = models.FloatField()
    pm25 = models.FloatField()
    pm10 = models.FloatField()
    pressure = models.FloatField()
    humidity = models.FloatField()
    temperature = models.FloatField()

class Grudziadz(models.Model):
    data = models.DateTimeField(primary_key=True)
    pm1 = models.FloatField()
    pm25 = models.FloatField()
    pm10 = models.FloatField()
    pressure = models.FloatField()
    humidity = models.FloatField()
    temperature = models.FloatField()

class Gdansk(models.Model):
    data = models.DateTimeField(primary_key=True)
    pm1 = models.FloatField()
    pm25 = models.FloatField()
    pm10 = models.FloatField()
    pressure = models.FloatField()
    humidity = models.FloatField()
    temperature = models.FloatField()

class Gdynia(models.Model):
    data = models.DateTimeField(primary_key=True)
    pm1 = models.FloatField()
    pm25 = models.FloatField()
    pm10 = models.FloatField()
    pressure = models.FloatField()
    humidity = models.FloatField()
    temperature = models.FloatField()
