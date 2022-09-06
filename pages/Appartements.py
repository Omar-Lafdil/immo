# -*- coding: utf-8 -*-
"""
Created on Mon Aug 29 18:22:07 2022

@author: Hamza
"""

import numpy as np
import pickle
import streamlit as st
import pandas as pd
import requests
import urllib.parse
import math 

import sys
import time
from bs4 import BeautifulSoup
import requests
import pandas as pd
from time import sleep
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import csv
import seaborn as sns
from datetime import date, timedelta

loaded_model = pickle.load(open('pages/RF_67.6.sav', 'rb'))




def main():
    
    
    #giving a title
    #st.title('Estimation des Prix des Appartements')
    
    #sidebar    
    
    

    st.header("Prédiction du prix d'une appartement à partir de ces caractéristiques")
    st.text("")
    
    st.subheader('Veuillez Remplire ce formulaire suivant :')
    secteur,etage = st.columns([3,1])
    sect = secteur.text_input('Secteur')
    etag = etage.number_input('Etage', min_value=1, max_value=8,format = '%i' )
    salons,surface = st.columns([1,3])
    surf = surface.slider('Surface habitable', min_value=40, max_value=260,step=1,format = '%i')
    salon = salons.number_input('Salons', min_value=1, max_value=7,format = '%i' )
    age = st.radio("Age de l'appartement",options = ['Neuf','de 1 à 5 ans','de 6 à 10 ans', 'de 11 à 20 ans','21+ ans'])
    
    pred = st.button('Prédire')
    if pred :
        #Création de la donnée
        df = pd.DataFrame(columns = [ "Étage", "Surface habitable", "Salons"])
        

        df.loc[len(df)] = [etag,surf,salon]

        #df.loc[1] = [etage,surface,salons]
        print(df)
        #Ajout lat et lon
        url = 'https://nominatim.openstreetmap.org/search/' + urllib.parse.quote(sect) +'?format=json'
        response = requests.get(url).json()
        df['Latitude'] = response[0]["lat"]
        df['Longitude'] = response[0]["lon"]
        if age == 'Neuf' :    
            df['Âge du bien_1-5 ans']=0
            df['Âge du bien_11-20 ans']=0
            df['Âge du bien_21+ ans']=0
            df['Âge du bien_6-10 ans']=0
            df['Âge du bien_Neuf']=1
            
            
        if age == 'de 1 à 5 ans' :    
            df['Âge du bien_1-5 ans']=1
            df['Âge du bien_11-20 ans']=0
            df['Âge du bien_21+ ans']=0
            df['Âge du bien_6-10 ans']=0
            df['Âge du bien_Neuf']=0
            
            
        if age == 'de 6 à 10 ans' :    
            df['Âge du bien_1-5 ans']=0
            df['Âge du bien_11-20 ans']=0
            df['Âge du bien_21+ ans']=0
            df['Âge du bien_6-10 ans']=1
            df['Âge du bien_Neuf']=0
            
            
        if age == 'de 11 à 20 ans' :    
            df['Âge du bien_1-5 ans']=0
            df['Âge du bien_11-20 ans']=1
            df['Âge du bien_21+ ans']=0
            df['Âge du bien_6-10 ans']=0
            df['Âge du bien_Neuf']=0
            
            
        if age == '21+ ans' :    
            df['Âge du bien_1-5 ans']=0
            df['Âge du bien_11-20 ans']=0
            df['Âge du bien_21+ ans']=1
            df['Âge du bien_6-10 ans']=0
            df['Âge du bien_Neuf']=0
        
        df['month'] = 8
            
        prix = math.exp(loaded_model.predict(df))
        prix_min = math.trunc((prix-(prix/10))/1000) * 1000
        prix_max = math.trunc((prix+(prix/10))/1000) * 1000
        message = 'Le prix de cet appartement doit être entre : '+ str(prix_min) +' MAD et '+ str(prix_max)+' MAD'
        st.success(message)
        st.text(prix_max)


    st.markdown("Notre Model n'est pas parfait !  ")


    
    
    
if __name__ == '__main__' :
    main()

