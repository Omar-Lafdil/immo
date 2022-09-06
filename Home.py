# -*- coding: utf-8 -*-
"""
Created on Mon Aug 29 16:41:35 2022

@author: Hamza
"""

import numpy as np
import pickle
import streamlit as st










def main():
    
    
    #giving a title
    #st.title('Estimation des Prix des Appartements')
    
    #sidebar    
    
    #st.set_page_config(page_title="Immobilier Dashboard", page_icon=":bar_chart:", layout="wide")


    st.header("Application Web pour Estimer les prix de l'immobilier au Maroc")
    st.text("")
    st.text("")
    st.text("")

    st.text("")

    st.text("")


    st.markdown('Nous avons construit cette application web pour : ')
    st.markdown('- Aider le citoyen Marocain à **prédire le prix** de son appartement de rêve .')
    st.markdown("- Aider les investisseurs **en leur donnant accès** aux outils d'analyse du marché .")
    st.markdown("- Trier les bonnes offres des mauvaises. Sites Web pris en charge :  **Avito**")
    st.markdown("- Plus de fonctionnalités seront ajoutées dans le future ...")


    
    
    
if __name__ == '__main__' :
    main()