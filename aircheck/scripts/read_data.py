import requests, json
import pandas as pd
import psycopg2
from sqlalchemy import create_engine
import os

apikey = 'aETVrbBycgJAa3TZwgO6y0xiQWwhThOT'  # type: str

headers = {
    'Accept' : 'application/json',
    'Accept-Encoding' : 'gzip',
    'Accept-Language' : 'pl',
    'apikey': apikey
}

# function for adding specific sensor to the table - lista sensorow

#def insert_sensor(sensor_id, latitude, longtitude):
#    # insert a new sensor into the lista_sensorow table
#    sql = "INSERT INTO lista_sensorow VALUES (%s, %s, %s)"
#    conn = psycopg2.connect("dbname=testdb user=lasher85 password=popey889")
#    # create a new cursor
#    cur = conn.cursor()
#    #  execute the INSERT statement
#    cur.execute(sql, (sensor_id, latitude, longtitude))
#    #  commit the changes to the database
#    conn.commit()
#    #  close communication with the database
#    cur.close()
#    conn.close()

# add specific sensor to the table - lista sensorow

# insert_sensor('tenczynek_reymonta', 50.117003, 19.615939)
# insert_sensor('krakow_nowaczynskiego', 50.047612, 19.919443)
# insert_sensor('katowice_miarki', 50.254433, 19.017431)
# insert_sensor('katowice_3maja', 50.2597493, 19.017431)
# insert_sensor('krzeszowice_grunwaldzka', 50.13661, 19.629246)
# insert_sensor('grudziadz_pilsudskiego', 53.493205, 18.761971)
# insert_sensor('gdansk_pocztowa', 54.348525, 18.649805)
# insert_sensor('gdynia_legionow', 54.493517, 18.540916)

# sensor URL list

url_tenczynek_pomiary = 'https://airapi.airly.eu/v2/measurements/nearest?lat=50.117003&lng=19.615939&maxDistanceKM=1'
url_krakow_pomiary = 'https://airapi.airly.eu/v2/measurements/nearest?lat=50.047612&lng=19.919443&maxDistanceKM=1'
url_katowice_pomiary = 'https://airapi.airly.eu/v2/measurements/nearest?lat=50.2597493&lng=19.017431&maxDistanceKM=1'
url_krzeszowice_pomiary = 'https://airapi.airly.eu/v2/measurements/nearest?lat=50.13661&lng=19.629246&maxDistanceKM=1'
url_grudziadz_pomiary = 'https://airapi.airly.eu/v2/measurements/nearest?lat=53.493205&lng=18.761971&maxDistanceKM=1'
url_gdansk_pomiary = 'https://airapi.airly.eu/v2/measurements/nearest?lat=54.348525&lng=18.649805&maxDistanceKM=1'
url_gdynia_pomiary = 'https://airapi.airly.eu/v2/measurements/nearest?lat=54.493517&lng=18.540916&maxDistanceKM=1'

# download sensor data via airly API

req_tenczynek_pomiary = requests.get(url_tenczynek_pomiary, headers=headers)
req_krakow_pomiary = requests.get(url_krakow_pomiary, headers=headers)
req_katowice_pomiary = requests.get(url_katowice_pomiary, headers=headers)
req_krzeszowice_pomiary = requests.get(url_krzeszowice_pomiary, headers=headers)
req_grudziadz_pomiary = requests.get(url_grudziadz_pomiary, headers=headers)
req_gdansk_pomiary = requests.get(url_gdansk_pomiary, headers=headers)
req_gdynia_pomiary = requests.get(url_gdynia_pomiary, headers=headers)

json_tenczynek_pomiary = req_tenczynek_pomiary.json()
json_krakow_pomiary = req_krakow_pomiary.json()
json_katowice_pomiary = req_katowice_pomiary.json()
json_krzeszowice_pomiary = req_krzeszowice_pomiary.json()
json_grudziadz_pomiary = req_grudziadz_pomiary.json()
json_gdansk_pomiary = req_gdansk_pomiary.json()
json_gdynia_pomiary = req_gdynia_pomiary.json()

# write data in lists - short form

a1 = json_tenczynek_pomiary["history"]
a2 = json_krakow_pomiary["history"]
a3 = json_katowice_pomiary["history"]
a4 = json_krzeszowice_pomiary["history"]
a5 = json_grudziadz_pomiary["history"]
a6 = json_gdansk_pomiary["history"]
a7 = json_gdynia_pomiary["history"]

# create empty lists

## tenczynek (1)

pm1_history_tenczynek = []
pm25_history_tenczynek = []
pm10_history_tenczynek = []
pressure_history_tenczynek = []
humidity_history_tenczynek = []
temperature_history_tenczynek = []

## krakow (2)

pm1_history_krakow = []
pm25_history_krakow = []
pm10_history_krakow = []
pressure_history_krakow = []
humidity_history_krakow = []
temperature_history_krakow = []

## katowice (3)

pm1_history_katowice = []
pm25_history_katowice = []
pm10_history_katowice = []
pressure_history_katowice = []
humidity_history_katowice = []
temperature_history_katowice = []

## krzeszowice (4)

pm1_history_krzeszowice = []
pm25_history_krzeszowice= []
pm10_history_krzeszowice = []
pressure_history_krzeszowice = []
humidity_history_krzeszowice = []
temperature_history_krzeszowice = []

## grudziadz (5)

pm1_history_grudziadz = []
pm25_history_grudziadz = []
pm10_history_grudziadz = []
pressure_history_grudziadz = []
humidity_history_grudziadz= []
temperature_history_grudziadz = []

## gdansk (6)

pm1_history_gdansk = []
pm25_history_gdansk = []
pm10_history_gdansk = []
pressure_history_gdansk = []
humidity_history_gdansk = []
temperature_history_gdansk = []

## gdynia (7)

pm1_history_gdynia = []
pm25_history_gdynia = []
pm10_history_gdynia = []
pressure_history_gdynia = []
humidity_history_gdynia = []
temperature_history_gdynia = []

## data

history_date = []

# Fill lists with historic data

## tenczynek

for i in range(len(a1)):

    if a1[i]['values'] != []:
        pm1_history_tenczynek.append(a1[i]['values'][0]['value'])               # PM1
        pm25_history_tenczynek.append(a1[i]['values'][1]['value'])              # PM2.5
        pm10_history_tenczynek.append(a1[i]['values'][2]['value'])              # PM10
        pressure_history_tenczynek.append(a1[i]['values'][3]['value'])          # Pressure
        humidity_history_tenczynek.append(a1[i]['values'][4]['value'])          # Humidity
        temperature_history_tenczynek.append(a1[i]['values'][5]['value'])       # Temperature
    else:
        pm1_history_tenczynek.append(0)                                         # PM1
        pm25_history_tenczynek.append(0)                                        # PM2.5
        pm10_history_tenczynek.append(0)                                        # PM10
        pressure_history_tenczynek.append(0)                                    # Pressure
        humidity_history_tenczynek.append(0)                                    # Humidity
        temperature_history_tenczynek.append(0)                                 # Temperature

## krakow

for i in range(len(a2)):

    if a2[i]['values'] != []:
        pm1_history_krakow.append(a2[i]['values'][0]['value'])                  # PM1
        pm25_history_krakow.append(a2[i]['values'][1]['value'])                 # PM2.5
        pm10_history_krakow.append(a2[i]['values'][2]['value'])                 # PM10
        pressure_history_krakow.append(a2[i]['values'][3]['value'])             # Pressure
        humidity_history_krakow.append(a2[i]['values'][4]['value'])             # Humidity
        temperature_history_krakow.append(a2[i]['values'][5]['value'])          # Temperature
    else:
        pm1_history_krakow.append(0)                                            # PM1
        pm25_history_krakow.append(0)                                           # PM2.5
        pm10_history_krakow.append(0)                                           # PM10
        pressure_history_krakow.append(0)                                       # Pressure
        humidity_history_krakow.append(0)                                       # Humidity
        temperature_history_krakow.append(0)                                    # Temperature

## katowice

for i in range(len(a3)):

    if a3[i]['values'] != []:
        pm1_history_katowice.append(a3[i]['values'][0]['value'])                # PM1
        pm25_history_katowice.append(a3[i]['values'][1]['value'])               # PM2.5
        pm10_history_katowice.append(a3[i]['values'][2]['value'])               # PM10
        pressure_history_katowice.append(a3[i]['values'][3]['value'])           # Pressure
        humidity_history_katowice.append(a3[i]['values'][4]['value'])           # Humidity
        temperature_history_katowice.append(a3[i]['values'][5]['value'])        # Temperature
    else:
        pm1_history_katowice.append(0)                                          # PM1
        pm25_history_katowice.append(0)                                         # PM2.5
        pm10_history_katowice.append(0)                                         # PM10
        pressure_history_katowice.append(0)                                     # Pressure
        humidity_history_katowice.append(0)                                     # Humidity
        temperature_history_katowice.append(0)                                  # Temperature

## krzeszowice

for i in range(len(a4)):

    if a4[i]['values'] != []:
        pm1_history_krzeszowice.append(a4[i]['values'][0]['value'])             # PM1
        pm25_history_krzeszowice.append(a4[i]['values'][1]['value'])            # PM2.5
        pm10_history_krzeszowice.append(a4[i]['values'][2]['value'])            # PM10
        pressure_history_krzeszowice.append(a4[i]['values'][3]['value'])        # Pressure
        humidity_history_krzeszowice.append(a4[i]['values'][4]['value'])        # Humidity
        temperature_history_krzeszowice.append(a4[i]['values'][5]['value'])     # Temperature
    else:
        pm1_history_krzeszowice.append(0)                                       # PM1
        pm25_history_krzeszowice.append(0)                                      # PM2.5
        pm10_history_krzeszowice.append(0)                                      # PM10
        pressure_history_krzeszowice.append(0)                                  # Pressure
        humidity_history_krzeszowice.append(0)                                  # Humidity
        temperature_history_krzeszowice.append(0)                               # Temperature

## grudziadz

for i in range(len(a5)):

    if a5[i]['values'] != []:
        pm1_history_grudziadz.append(a5[i]['values'][0]['value'])               # PM1
        pm25_history_grudziadz.append(a5[i]['values'][1]['value'])              # PM2.5
        pm10_history_grudziadz.append(a5[i]['values'][2]['value'])              # PM10
        pressure_history_grudziadz.append(a5[i]['values'][3]['value'])          # Pressure
        humidity_history_grudziadz.append(a5[i]['values'][4]['value'])          # Humidity
        temperature_history_grudziadz.append(a5[i]['values'][5]['value'])       # Temperature
    else:
        pm1_history_grudziadz.append(0)                                         # PM1
        pm25_history_grudziadz.append(0)                                        # PM2.5
        pm10_history_grudziadz.append(0)                                        # PM10
        pressure_history_grudziadz.append(0)                                    # Pressure
        humidity_history_grudziadz.append(0)                                    # Humidity
        temperature_history_grudziadz.append(0)                                 # Temperature

## gdansk

for i in range(len(a6)):

    if a6[i]['values'] != []:
        pm1_history_gdansk.append(a6[i]['values'][0]['value'])                  # PM1
        pm25_history_gdansk.append(a6[i]['values'][1]['value'])                 # PM2.5
        pm10_history_gdansk.append(a6[i]['values'][2]['value'])                 # PM10
        pressure_history_gdansk.append(a6[i]['values'][3]['value'])             # Pressure
        humidity_history_gdansk.append(a6[i]['values'][4]['value'])             # Humidity
        temperature_history_gdansk.append(a6[i]['values'][5]['value'])          # Temperature
    else:
        pm1_history_gdansk.append(0)                                            # PM1
        pm25_history_gdansk.append(0)                                           # PM2.5
        pm10_history_gdansk.append(0)                                           # PM10
        pressure_history_gdansk.append(0)                                       # Pressure
        humidity_history_gdansk.append(0)                                       # Humidity
        temperature_history_gdansk.append(0)                                    # Temperature

## gdynia

for i in range(len(a7)):

    if a7[i]['values'] != []:
        pm1_history_gdynia.append(a7[i]['values'][0]['value'])                  # PM1
        pm25_history_gdynia.append(a7[i]['values'][1]['value'])                 # PM2.5
        pm10_history_gdynia.append(a7[i]['values'][2]['value'])                 # PM10
        pressure_history_gdynia.append(a7[i]['values'][3]['value'])             # Pressure
        humidity_history_gdynia.append(a7[i]['values'][4]['value'])             # Humidity
        temperature_history_gdynia.append(a7[i]['values'][5]['value'])          # Temperature
    else:
        pm1_history_gdynia.append(0)                                            # PM1
        pm25_history_gdynia.append(0)                                           # PM2.5
        pm10_history_gdynia.append(0)                                           # PM10
        pressure_history_gdynia.append(0)                                       # Pressure
        humidity_history_gdynia.append(0)                                       # Humidity
        temperature_history_gdynia.append(0)                                    # Temperature

## data

for i in range(len(a1)):
    history_date.append(a1[i]['tillDateTime'])                                  # measurements - date

# create DATA FRAME for specific sensors

## tenczynek DATA FRAME (1)

tenczynek_dataframe = pd.DataFrame({'PM1' : pm1_history_tenczynek,
                                    'PM25' : pm25_history_tenczynek,
                                    'PM10' : pm10_history_tenczynek,
                                    'Pressure' : pressure_history_tenczynek,
                                    'Humidity' : humidity_history_tenczynek,
                                    'Temperature' : temperature_history_tenczynek
                                    }, index=history_date,
                                   columns=['PM1', 'PM25', 'PM10', 'Pressure', 'Humidity', 'Temperature'])

tenczynek_dataframe.index = pd.to_datetime(tenczynek_dataframe.index)
tenczynek_dataframe.index.name = "Data"

## krakow DATA FRAME (2)

krakow_dataframe = pd.DataFrame({'PM1' : pm1_history_krakow,
                                    'PM25' : pm25_history_krakow,
                                    'PM10' : pm10_history_krakow,
                                    'Pressure' : pressure_history_krakow,
                                    'Humidity' : humidity_history_krakow,
                                    'Temperature' : temperature_history_krakow
                                    }, index=history_date,
                                   columns=['PM1', 'PM25', 'PM10', 'Pressure', 'Humidity', 'Temperature'])

krakow_dataframe.index = pd.to_datetime(krakow_dataframe.index)
krakow_dataframe.index.name = "Data"

## katowice DATA FRAME (3)

katowice_dataframe = pd.DataFrame({'PM1' : pm1_history_katowice,
                                    'PM25' : pm25_history_katowice,
                                    'PM10' : pm10_history_katowice,
                                    'Pressure' : pressure_history_katowice,
                                    'Humidity' : humidity_history_katowice,
                                    'Temperature' : temperature_history_katowice
                                    }, index=history_date,
                                   columns=['PM1', 'PM25', 'PM10', 'Pressure', 'Humidity', 'Temperature'])

katowice_dataframe.index = pd.to_datetime(katowice_dataframe.index)
katowice_dataframe.index.name = "Data"

## krzeszowice DATA FRAME (4)

krzeszowice_dataframe = pd.DataFrame({'PM1' : pm1_history_krzeszowice,
                                    'PM25' : pm25_history_krzeszowice,
                                    'PM10' : pm10_history_krzeszowice,
                                    'Pressure' : pressure_history_krzeszowice,
                                    'Humidity' : humidity_history_krzeszowice,
                                    'Temperature' : temperature_history_krzeszowice
                                    }, index=history_date,
                                   columns=['PM1', 'PM25', 'PM10', 'Pressure', 'Humidity', 'Temperature'])

krzeszowice_dataframe.index = pd.to_datetime(krzeszowice_dataframe.index)
krzeszowice_dataframe.index.name = "Data"

## grudziadz DATA FRAME (5)

grudziadz_dataframe = pd.DataFrame({'PM1' : pm1_history_grudziadz,
                                    'PM25' : pm25_history_grudziadz,
                                    'PM10' : pm10_history_grudziadz,
                                    'Pressure' : pressure_history_grudziadz,
                                    'Humidity' : humidity_history_grudziadz,
                                    'Temperature' : temperature_history_grudziadz
                                    }, index=history_date,
                                   columns=['PM1', 'PM25', 'PM10', 'Pressure', 'Humidity', 'Temperature'])

grudziadz_dataframe.index = pd.to_datetime(grudziadz_dataframe.index)
grudziadz_dataframe.index.name = "Data"

## gdansk DATA FRAME (6)

gdansk_dataframe = pd.DataFrame({'PM1' : pm1_history_gdansk,
                                    'PM25' : pm25_history_gdansk,
                                    'PM10' : pm10_history_gdansk,
                                    'Pressure' : pressure_history_gdansk,
                                    'Humidity' : humidity_history_gdansk,
                                    'Temperature' : temperature_history_gdansk
                                    }, index=history_date,
                                   columns=['PM1', 'PM25', 'PM10', 'Pressure', 'Humidity', 'Temperature'])

gdansk_dataframe.index = pd.to_datetime(gdansk_dataframe.index)
gdansk_dataframe.index.name = "Data"

## gdynia DATA FRAME (7)

gdynia_dataframe = pd.DataFrame({'PM1' : pm1_history_gdynia,
                                    'PM25' : pm25_history_gdynia,
                                    'PM10' : pm10_history_gdynia,
                                    'Pressure' : pressure_history_gdynia,
                                    'Humidity' : humidity_history_gdynia,
                                    'Temperature' : temperature_history_gdynia
                                    }, index=history_date,
                                   columns=['PM1', 'PM25', 'PM10', 'Pressure', 'Humidity', 'Temperature'])

gdynia_dataframe.index = pd.to_datetime(gdynia_dataframe.index)
gdynia_dataframe.index.name = "Data"

# insert measurements into SQL database table

def insert_measurement(Table, Data, PM1, PM25, PM10, Pressure, Humidity, Temperature):
    sql1 = "INSERT INTO "
    sql2 = Table
    sql3 = " VALUES (%s, %s, %s, %s, %s, %s, %s)"
    sql = sql1 + sql2 + sql3
    DATABASE_URL = os.environ['DATABASE_URL']
    conn = psycopg2.connect(DATABASE_URL, sslmode='require')
    # create a new cursor
    cur = conn.cursor()
    #  execute the INSERT statement
    cur.execute(sql, (Data, PM1, PM25, PM10, Pressure, Humidity, Temperature))
    #  commit the changes to the database
    conn.commit()
    #  close communication with the database
    cur.close()
    conn.close()

for i in range(len(a1)):
    insert_measurement(
        "aircheck_tenczynek",
        tenczynek_dataframe.index[i],
        float(tenczynek_dataframe.iloc[i]['PM1']),
        float(tenczynek_dataframe.iloc[i]['PM25']),
        float(tenczynek_dataframe.iloc[i]['PM10']),
        float(tenczynek_dataframe.iloc[i]['Pressure']),
        float(tenczynek_dataframe.iloc[i]['Humidity']),
        float(tenczynek_dataframe.iloc[i]['Temperature'])
    )

for i in range(len(a1)):
    insert_measurement(
        "aircheck_krakow",
        krakow_dataframe.index[i],
        float(krakow_dataframe.iloc[i]['PM1']),
        float(krakow_dataframe.iloc[i]['PM25']),
        float(krakow_dataframe.iloc[i]['PM10']),
        float(krakow_dataframe.iloc[i]['Pressure']),
        float(krakow_dataframe.iloc[i]['Humidity']),
        float(krakow_dataframe.iloc[i]['Temperature'])
    )

for i in range(len(a1)):
    insert_measurement(
        "aircheck_katowice",
        katowice_dataframe.index[i],
        float(katowice_dataframe.iloc[i]['PM1']),
        float(katowice_dataframe.iloc[i]['PM25']),
        float(katowice_dataframe.iloc[i]['PM10']),
        float(katowice_dataframe.iloc[i]['Pressure']),
        float(katowice_dataframe.iloc[i]['Humidity']),
        float(katowice_dataframe.iloc[i]['Temperature'])
    )

    insert_measurement(
        "aircheck_krzeszowice",
        krzeszowice_dataframe.index[i],
        float(krzeszowice_dataframe.iloc[i]['PM1']),
        float(krzeszowice_dataframe.iloc[i]['PM25']),
        float(krzeszowice_dataframe.iloc[i]['PM10']),
        float(krzeszowice_dataframe.iloc[i]['Pressure']),
        float(krzeszowice_dataframe.iloc[i]['Humidity']),
        float(krzeszowice_dataframe.iloc[i]['Temperature'])
    )

for i in range(len(a1)):
    insert_measurement(
        "aircheck_grudziadz",
        grudziadz_dataframe.index[i],
        float(grudziadz_dataframe.iloc[i]['PM1']),
        float(grudziadz_dataframe.iloc[i]['PM25']),
        float(grudziadz_dataframe.iloc[i]['PM10']),
        float(grudziadz_dataframe.iloc[i]['Pressure']),
        float(grudziadz_dataframe.iloc[i]['Humidity']),
        float(grudziadz_dataframe.iloc[i]['Temperature'])
    )

for i in range(len(a1)):
    insert_measurement(
        "aircheck_gdansk",
        gdansk_dataframe.index[i],
        float(gdansk_dataframe.iloc[i]['PM1']),
        float(gdansk_dataframe.iloc[i]['PM25']),
        float(gdansk_dataframe.iloc[i]['PM10']),
        float(gdansk_dataframe.iloc[i]['Pressure']),
        float(gdansk_dataframe.iloc[i]['Humidity']),
        float(gdansk_dataframe.iloc[i]['Temperature'])
    )

for i in range(len(a1)):
    insert_measurement(
        "aircheck_gdynia",
        gdynia_dataframe.index[i],
        float(gdynia_dataframe.iloc[i]['PM1']),
        float(gdynia_dataframe.iloc[i]['PM25']),
        float(gdynia_dataframe.iloc[i]['PM10']),
        float(gdynia_dataframe.iloc[i]['Pressure']),
        float(gdynia_dataframe.iloc[i]['Humidity']),
        float(gdynia_dataframe.iloc[i]['Temperature'])
    )