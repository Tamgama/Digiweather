
import pandas as pd
import numpy as np 
import requests as rq 
import re
import folium
from folium import plugins


pd.set_option('display.max_columns', None)


class selection:
    def __init__(self, municipio, provincia, ccaa):
        self.municipio = municipio
        self.provincia = provincia
        self.ccaa = ccaa
        pass

# Murcia = selection('Murcia', 'Murcia', 'Región de Murcia')
    # Murcia.municipio
    # Murcia.provincia
    # Murcia.ccaa

    def call_api(url):
        response = rq.get(url)
        if response.status_code == 200: 
            print(f"API call failed: {response.reason}")
        else:
            return response.json()

    def provincias(self, provincia):
        self.provincia = prov
        
        provincias = {'01': 'Álava', '02': 'Albacete', '03': 'Alicante', '04': 'Almería', '33': 'Asturias', '05': 'Ávila', '06': 'Badajoz',
            '08': 'Barcelona', '48': 'Bizkaia','09': 'Burgos', '10': 'Cáceres', '11': 'Cádiz',  '39': 'Cantabria', '12': 'Castelló/Castellón',
            '51': 'Ceuta', '13': 'Ciudad Real','14': 'Córdoba', '15': 'A Coruña', '16': 'Cuenca', '17': 'Girona', '18': 'Granada', '19': 'Guadalajara',
            '20': 'Gipuzkoa', '21': 'Huelva', '22': 'Huesca', '071': 'Isla de Menorca', '072': 'Isla de Mallorca', '073': 'Islas de Ibiza y Formentera',
            '351': 'Isla de Lanzarote', '352': 'Isla de Fuerteventura', '353': 'Isla de Gran Canaria',  '381': 'Isla de Tenerife', '382': 'Isla de La Gomera',
            '383': 'Isla de La Palma', '384': 'Isla de El Hierro', '23': 'Jaén','24': 'León','25': 'Lleida','27': 'Lugo', '28': 'Madrid', '29': 'Málaga',
            '52': 'Melilla','30': 'Murcia', '31': 'Navarra','32': 'Ourense', '34': 'Palencia','36': 'Pontevedra','26': 'La Rioja', '37': 'Salamanca','40': 'Segovia',
            '41': 'Sevilla','42': 'Soria','43': 'Tarragona','44': 'Teruel','45': 'Toledo','46': 'Valencia','47': 'Valladolid','49': 'Zamora', '50': 'Zaragoza'}
        
        prov = input(f"Selecciona el número de la provincia de la que quieras ver el tiempo")

        for provincia in provincias:
            if prov == provincias['']:
                url_aemet = f"https://opendata.aemet.es/opendata/api/prediccion/provincia/hoy/{prov}?api_key={api_aemet}"

    
#        json_provincias = call_api(url_aemet)
                
    
