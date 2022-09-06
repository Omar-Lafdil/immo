# -*- coding: utf-8 -*-
"""
Created on Tue Aug 30 08:16:42 2022

@author: Hamza
"""

import numpy as np
import pickle
import streamlit as st
import pandas as pd
#import plotly.figure_factory as ff
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px  # pip install plotly-express
import math

def main():
    
    
    #giving a title
    #st.title('Estimation des Prix des Appartements')
    st.set_page_config(page_title="Immobilier Dashboard", page_icon=":bar_chart:", layout="wide")

    #sidebar    
    st.set_option('deprecation.showPyplotGlobalUse', False)

    
    #st.header("Dashboard")
    st.text("")
    

    with st.sidebar:
        st.text("")
        st.text("")
        st.text("")

        st.subheader("Analyse :")
        rad = st.radio('', ['Temporelle', 'Selon le secteur', 'Etude des caractéristiques'])
    if rad == 'Selon le secteur':
        st.markdown("<h1 style='text-align: center; color: #FFFFFF;'> Secteurs </h1>", unsafe_allow_html=True)
        #st.header("Dashboard")
        st.text("")
        
        col1, col3 = st.columns(2, gap="small")

        st.markdown('- **Map**.')
        df = pd.read_csv('pages/données.csv')
        df['latitude'] = df['Latitude']
        df['longitude'] = df['Longitude']
        df_geo = df[['Prix','latitude','longitude']]
        df_seulement_geo = df_geo.drop(columns="Prix")
        st.map(df_seulement_geo)
        dfs = pd.read_csv('pages/secteurs.csv').head(6)
        #fig = ff.create_distplot(dfs, bin_size=[.1, .25, .5])
        #st.plotly_chart(fig, use_container_width=True)
        nouv_df = (dfs.groupby(by=["Villes"]).mean()[["Counts"]].sort_values(by="Counts", ascending = False).head(6))

        #sns.barplot(x=dfs['Counts'], y=dfs['Villes'])
        fig_sales = px.bar(nouv_df,x=nouv_df.index,y="Counts",title="<b>Les Secteurs Contenant le plus grand nombre d'offres</b>",color_discrete_sequence=["#0083B8"] * len(nouv_df),template="plotly_white")
        fig_sales.update_layout(
        xaxis=dict(tickmode="linear"),
        plot_bgcolor="rgba(0,0,0,0)",
        yaxis=(dict(showgrid=False)),
    )
        
        #plt.xticks(rotation="vertical")
        
        #fig = plt.show()
        col1.plotly_chart(fig_sales, use_container_width=True)
        
        df_secteur = pd.read_csv('pages/Dataset.csv')
        nouv_df = (df_secteur.groupby(by=["Secteur"]).mean()[["Prix"]].sort_values(by="Prix", ascending = False).head(6))
        st.text("")
        
        fig_hourly_sales = px.bar(nouv_df,x=nouv_df.index,y="Prix",title="<b>Les Secteurs les plus chers</b>",color_discrete_sequence=["#0083B8"] * len(nouv_df),template="plotly_white")
        fig_hourly_sales.update_layout(
        xaxis=dict(tickmode="linear"),
        plot_bgcolor="rgba(0,0,0,0)",
        yaxis=(dict(showgrid=False)),
    )
        
        
        nouv_df.plot.barh(stacked=True)
        col3.plotly_chart(fig_hourly_sales, use_container_width=True)
        st.text("")
        #fig.update_layout(plot_bgcolor="rgba(0,0,0,0)")
        #col3.pyplot(fig)

        #st.bar_chart(dfs, use_container_width=True)
        
    if rad == 'Temporelle' :
        df_tempo = pd.read_csv('pages/Months_dat.csv')
        this_m_avg = math.trunc(df_tempo['Avg'][0]/1000)*1000
        last_m_avg = math.trunc(df_tempo['Avg'][1]/1000)*1000
        change = this_m_avg-last_m_avg
        col1, col3 = st.columns(2, gap="small")
        col1.subheader("Résultats du mois Août :")
        col3.metric(label="Avg Price", value=(str(this_m_avg)+ " MAD"), delta=(str(change)+" MAD"))
        st.text("")
        st.text("")

        st.text("")
        
        col1, col2, col3 = st.columns([1,1,4], gap="small")

        #sns.barplot(x=df_tempo['Months'], y=df_tempo['Avg'])
        
        fig = px.line(df_tempo, x="Months", y="Avg", title='Evolution du prix selon le mois')
        fig.update_layout(
        xaxis=dict(showgrid=False),
        plot_bgcolor="rgba(0,0,0,0)",
        yaxis=(dict(showgrid=False)),
    )
    
        col2.plotly_chart(fig)

    
    if rad == 'Etude des caractéristiques':
        tab1, tab2, tab3, tab4 = st.tabs(["Surface Habitable", "Salons", "Etage","Âge de l'appartement"])
        df = pd.read_csv('pages/Données_fin.csv')
        
        with tab1:
            st.header("Surface Habitable")
            nouv_df = (df.groupby(by=["Surface habitable"]).mean()[["Prix"]].sort_values(by="Surface habitable", ascending = True))
            col1, col2 = st.columns(2, gap="small")
            fig = px.line(nouv_df, x=nouv_df.index, y="Prix",labels={'Prix':"Prix en MAD"}, title='Evolution du prix selon la surface habitable')
            fig.update_layout(
            xaxis=dict(showgrid=False),
            plot_bgcolor="rgba(0,0,0,0)",
            yaxis=(dict(showgrid=False)),
        )
        
            col1.plotly_chart(fig)
        
        with tab2:
            nouv_df = (df.groupby(by=["Salons"]).mean()[["Prix"]].sort_values(by="Prix", ascending = False))
            col1, col2 = st.columns(2, gap="small")
            figure = px.bar(nouv_df, x=nouv_df.index, y='Prix',labels={'Prix':"Prix en MAD"}, title='Evolution du prix selon le Nombre des salons',color_discrete_sequence=["#0083B8"] * len(nouv_df),template="plotly_white")
            figure.update_layout(
            xaxis=dict(showgrid=False),
            plot_bgcolor="rgba(0,0,0,0)",
            yaxis=(dict(showgrid=False)),
        )
            col1.plotly_chart(figure, use_container_width=True)
            nouv_df = (df.groupby(by=["Salons"]).count())["Titre"]
            figure = px.bar(nouv_df, x=nouv_df.index, y=nouv_df, labels={'y':"Nb d'offres"}, title="Nombre d'offres selon le nombre des salons",color_discrete_sequence=["#0083B8"] * len(nouv_df),template="plotly_white")
            figure.update_layout(
            xaxis=dict(showgrid=False),
            plot_bgcolor="rgba(0,0,0,0)",
            yaxis=(dict(showgrid=False)),
        )
            col2.plotly_chart(figure, use_container_width=True)

            
        with tab3:
            col1, col2 = st.columns(2, gap="small")

            nouv_df = (df.groupby(by=["Étage"]).count())["Titre"]
            figure = px.bar(nouv_df, x=nouv_df.index, y=nouv_df, labels={'y':"Nb d'offres"}, title="Nombre d'offres selon l'Étage",color_discrete_sequence=["#0083B8"] * len(nouv_df),template="plotly_white")
            figure.update_layout(
            xaxis=dict(showgrid=False),
            plot_bgcolor="rgba(0,0,0,0)",
            yaxis=(dict(showgrid=False)),
        )
            col1.plotly_chart(figure, use_container_width=True)
            
            nouv_df = (df.groupby(by=["Étage"]).mean()[["Prix"]].sort_values(by="Prix", ascending = False))
            figure = px.bar(nouv_df, x=nouv_df.index, y='Prix', labels = {'Prix':"Prix en MAD"}, title="Evolution du prix selon l'Étage",color_discrete_sequence=["#0083B8"] * len(nouv_df),template="plotly_white")
            figure.update_layout(
            xaxis=dict(showgrid=False),
            plot_bgcolor="rgba(0,0,0,0)",
            yaxis=(dict(showgrid=False)),
            )
            col2.plotly_chart(figure, use_container_width=True)
        
        with tab4:
            col1, col2 = st.columns(2, gap="small")

            nouv_df = (df.groupby(by=["Âge du bien"]).count())["Titre"]
            figure = px.bar(nouv_df, x=nouv_df.index, y=nouv_df, labels={'y':"Nb d'offres"}, title="Nombre d'offres selon l'Étage",color_discrete_sequence=["#0083B8"] * len(nouv_df),template="plotly_white")
            figure.update_layout(
            xaxis=dict(showgrid=False),
            plot_bgcolor="rgba(0,0,0,0)",
            yaxis=(dict(showgrid=False)),
        )
            col1.plotly_chart(figure, use_container_width=True)
            
            nouv_df = (df.groupby(by=["Âge du bien"]).mean()[["Prix"]].sort_values(by="Prix", ascending = False))
            figure = px.bar(nouv_df, x=nouv_df.index, y='Prix', labels = {'Prix':"Prix en MAD"}, title="Evolution du prix selon l'Étage",color_discrete_sequence=["#0083B8"] * len(nouv_df),template="plotly_white")
            figure.update_layout(
            xaxis=dict(showgrid=False),
            plot_bgcolor="rgba(0,0,0,0)",
            yaxis=(dict(showgrid=False)),
            )
            col2.plotly_chart(figure, use_container_width=True)

    
if __name__ == '__main__' :
    main()