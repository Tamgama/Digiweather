# Phase 1 #

import pandas as pd
import numpy as np 
import requests as rq 
import re

pd.set_option('display.max_columns', None)

#%%
# Function 
def get_municipios(url):
    request = rq.get(url)

    print(f"Request code: {request.status_code}")

    if request.status_code != 200: 
        print(f"El motivo por el que la llamada falló es {request.reason}")
    else:
        return request.json()  # Si la llamada fue exitosa, devuelve los datos de respuesta en formato JSON.
    
api_key_aemet = 'eyJhbGciOiJIUzI1NiJ9.eyJzdWIiOiJ0YW1hcmEuZ2FybWFydEBnbWFpbC5jb20iLCJqdGkiOiJmYWI5ZTZiNS1jNmExLTQ1ZDktYTBjMy0yOWZjZWI5OGNjZjAiLCJpc3MiOiJBRU1FVCIsImlhdCI6MTcwMzc2MjU5NCwidXNlcklkIjoiZmFiOWU2YjUtYzZhMS00NWQ5LWEwYzMtMjlmY2ViOThjY2YwIiwicm9sZSI6IiJ9.wQjTcA3P9QntIk7bf14ARySyGL-elGxhQPlSaR-oyGM'

url_aemet = f"https://opendata.aemet.es/opendata/api/maestro/municipios?api_key={api_key_aemet}"

json_municipios = get_municipios(url_aemet)

#%%