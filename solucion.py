import pandas as pd
from typing import Set
import requests

def ej_1_cargar_datos_demograficos() -> pd.DataFrame:
    data = pd.read_csv("us-cities-demographics.cvs", sep=";")
    return data


   

def ej_2_cargar_calidad_aire(city: Set[str]) -> None:

    api_url= f'https://api.api-ninjas.com/v1/airquality?city={city}'.format(city)
    response = requests.get(api_url, headers={'X-Api-Key': 'XnpBYxcmgiEDi3JQdo9xZg==ZCUbPr9vcQNMDT2B'})
    if response.status_code == requests.codes.ok:
        
        data = response.json()
        return data
  

def limpieza_de_datos(data):
    eliminar_filas=data.drop(['Race', 'Count', 'Number of Veterans'], axis=1, inplace=True)
    datos_limpios=eliminar_filas.drop_duplicates(inplace=True)
    return datos_limpios

