# Phase 1 #
#%%
import pandas as pd
import numpy as np 
import requests as rq 
import re
from time import sleep

pd.set_option('display.max_columns', None)

#%%

def call_api(url):
    response = rq.get(url)
    if response.status_code == 200: 
        print(f"API call failed: {response.reason}")
    else:
        return response.json()

api_aemet = 'eyJhbGciOiJIUzI1NiJ9.eyJzdWIiOiJ0YW1hcmEuZ2FybWFydEBnbWFpbC5jb20iLCJqdGkiOiI0YzA3ZTdkZi01ZDA0LTRkMmUtOTczYy00ODEzYTJlZTQ3YzkiLCJpc3MiOiJBRU1FVCIsImlhdCI6MTcwNTMwODIzNiwidXNlcklkIjoiNGMwN2U3ZGYtNWQwNC00ZDJlLTk3M2MtNDgxM2EyZWU0N2M5Iiwicm9sZSI6IiJ9.lDZnCL3w1hr95P1D2x945REizy7mbTwhQeBWT67DXOY'
url_aemet = f"https://opendata.aemet.es/opendata/api/maestro/municipios?api_key={api_aemet}"

json_municipios = call_api(url_aemet)

# Municipios

df_municipios = pd.DataFrame(json_municipios)

df_municipios.drop(labels=["url", "latitud", "longitud", "num_hab", "zona_comarcal", "destacada", "id_old", 'altitud'], axis = 1, inplace=True)
df_municipios.rename(columns={'latitud_dec':'latitud', 'longitud_dec':'longitud', "nombre":"municipio", "capital": "cap_muni"}, inplace = True)
df_municipios['id'] = [id[2:4] for id in df_municipios['id']]
df_municipios = df_municipios.sort_values(by="id")

# Provincias

df_provs = pd.read_csv('../src/provincias', index_col=0)
df_provs.drop(labels=["CODAUTON"], axis = 1, inplace=True)
df_provs.rename(columns={"CODPROV":"id", "NOMBRE_PROVINCIA":"provincia", "COMUNIDAD_CIUDAD_AUTONOMA":"CCAA", "CAPITAL_PROVINCIA": "cap_prov"}, inplace=True)
df_provs["id"] = df_provs["id"].astype(str).str.zfill(2)
df_provs = df_provs.sort_values(by="id")

# Municipios, provincias y CCAA con CP/ID

df_completo = df_municipios.merge(df_provs, on="id_prov", how= "left")
df_completo = df_completo[["latitud", "longitud", "municipio", "cap_muni", "id", "CP", "provincia", "cap_prov", "id_prov", "CCAA",]]
df_completo.drop(labels=["id"], axis= 1, inplace=True)

#%%

muni_list= df_completo["CP"].unique().tolist()

resultados = {
            "fecha": [],
            "precipitacion": [],
            "cielo": [],
            "viento": [],
            "temp_min": [],
            "temp_max": [],
            "municipio": [],
            "provincia": [],
        }

def clean_prediction(resultados, prediction):    
    prediccion = prediction[0]

    dia = prediccion['prediccion']['dia'][0]
    resultados["fecha"].append(dia["fecha"])
    resultados["precipitacion"].append(dia["probPrecipitacion"][0]["value"])
    resultados["cielo"].append(dia["estadoCielo"][0]["descripcion"])
    resultados["viento"].append(dia["viento"][0]["velocidad"])
    resultados["temp_min"].append(dia["temperatura"]["minima"])
    resultados["temp_max"].append(dia["temperatura"]["maxima"])
    resultados['municipio'].append(prediccion['nombre'])
    resultados['provincia'].append(prediccion['provincia'])


    return resultados

for muni in muni_list[170::]:
    url_pred = f'https://opendata.aemet.es/opendata/api/prediccion/especifica/municipio/diaria/{muni}?api_key={api_aemet}'
    json_pred = call_api(url_pred) # primero call_api para sacar la info gral de todos los municipìos

    prediction = call_api(json_pred['datos']) # saca todos los datos de un municipio

    df_prediccion = clean_prediction(resultados, prediction) # diccionario con los resultados por día de def clean_prediction

    sleep(1)

    df_clean = pd.DataFrame(resultados)

    df_clean.to_csv('predicciones')