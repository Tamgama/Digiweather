# Phase 1 #

import pandas as pd
import numpy as np 
import requests as rq 
import re
import folium
from folium import plugins


pd.set_option('display.max_columns', None)

#%%

def call_api(url_aemet):
    call = rq.get(url_aemet)
    if call.status_code != 200: 
        print(f"Reason why the call failed {call.reason}")
    else:
        return call.json()

api_aemet = 'eyJhbGciOiJIUzI1NiJ9.eyJzdWIiOiJ0YW1hcmEuZ2FybWFydEBnbWFpbC5jb20iLCJqdGkiOiI0YzA3ZTdkZi01ZDA0LTRkMmUtOTczYy00ODEzYTJlZTQ3YzkiLCJpc3MiOiJBRU1FVCIsImlhdCI6MTcwNTMwODIzNiwidXNlcklkIjoiNGMwN2U3ZGYtNWQwNC00ZDJlLTk3M2MtNDgxM2EyZWU0N2M5Iiwicm9sZSI6IiJ9.lDZnCL3w1hr95P1D2x945REizy7mbTwhQeBWT67DXOY'

url_aemet = f"https://opendata.aemet.es/opendata/api/maestro/municipios?api_key={api_aemet}"

json_municipios = call_api(url_aemet)

#%%

df_municipios = pd.DataFrame(json_municipios)

df_municipios.drop(labels=["url", "latitud", "longitud", "num_hab", "zona_comarcal", "destacada", "id_old", 'altitud'], axis = 1, inplace=True)
df_municipios.rename(columns={'latitud_dec':'latitud', 'longitud_dec':'longitud'},inplace = True)

df_municipios
#%%

muni_list= df_municipios["id"].unique().tolist()

df_municipios['id'] = [id[2:] for id in df_municipios['id']]

muni_list = df_municipios['id']

#%%

results = {
            "fecha": [],
            "precipitacion": [],
            "cota_nieve": [],
            "cielo": [],
            "viento": [],
            "temp_min": [],
            "temp_max": [],
            "humedad_min": [],
            "humedad_max": [],
            "municipio": [],
            "provincia": []
        }

def clean_prediction(results, prediction):    
    prediccion = prediction[0]

    day = prediccion['prediccion']['day'][0]

    results["fecha"].append(day["fecha"])
    results["precipitacion"].append(day["probPrecipitacion"][0]["value"])
    results["cota_nieve"].append(day["cotaNieveProv"][0]["value"])
    results["cielo"].append(day["estadoCielo"][0]["descripcion"])
    results["viento"].append(day["viento"][0]["velocidad"])
    results["temp_min"].append(day["temperatura"]["minima"])
    results["temp_max"].append(day["temperatura"]["maxima"])
    results['municipio'].append(prediccion['nombre'])
    results['provincia'].append(prediccion['provincia'])


    return results

#%%

for muni in muni_list:
    url_pred = f'https://opendata.aemet.es/opendata/api/prediccion/especifica/municipio/diaria/{muni}?api_key={api_aemet}'
    json_pred = call_api(url_pred)

    prediction = call_api(json_pred['datos'])

    df_prediccion = clean_prediction(results, prediction)

df_clean = pd.DataFrame(results)

df_clean

