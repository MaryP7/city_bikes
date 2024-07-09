import streamlit as st
import pandas as pd
import numpy as np
from plotly.subplots import make_subplots
import plotly.graph_objects as go
import matplotlib.pyplot as plt
from streamlit_keplergl import keplergl_static
from keplergl import KeplerGl
from datetime import datetime as dt



st.set_page_config(page_title = 'Divvy Bikes Strategy Dashboard', layout='wide')
#st.title("Divvy Bikes Strategy Dashboard")
#st.markdown("The dashboard will help with the expansion problems Divvy currently faces")
#st.markdown("Right now, Divvy bikes runs into a situation where customers complain about bikes not being avaibale at certain times. This analysis aims to look at the potential reasons behind this.")

page = st.sidebar.selectbox('Select an aspect of the analysis',
   ["Intro page",  "Weather component and bike usage",
  "Most popular stations",
     "Map", "Recommendations"])

if page == "Weather component and bike usage":

    df = pd.read_csv('data/data_subset.csv', index_col = 0)

    fig_2 = make_subplots(specs = [[{"secondary_y": True}]])

    fig_2.add_trace(
        go.Scatter(x = df['date'], y = df['bike_rides_daily'], name = 'Daily bike rides', marker={'color': df['bike_rides_daily'],'color': 'blue'}),
    secondary_y = False
    )

    fig_2.add_trace(
    go.Scatter(x=df['date'], y = df['avgTemp'], name = 'Daily temperature', marker={'color': df['avgTemp'],'color': 'red'}),
    secondary_y=True
    )

    fig_2.update_layout(
    title = 'Daily bike trips and temperatures in 2022',
    height = 600
    )

    st.plotly_chart(fig_2, use_container_width=True)

elif page == "Most popular stations":

    top20 = pd.read_csv('data/top20.csv', index_col = 0)


    fig = go.Figure(go.Bar(x = top20.index, y = top20['value'], marker={'color': top20['value'],'colorscale': 'Blues'}))
    fig.update_layout(
    title = 'Top 20 most popular bike stations in New York',
    xaxis_title = 'Start stations',
    yaxis_title ='Sum of trips',
    width = 900, height = 600
    )
    st.plotly_chart(fig, use_container_width=True)

elif page == "Map":

    path_to_html = "Divvy Bike Trips Aggregated.html" 

    with open(path_to_html,'r') as f: 
        html_data = f.read()

    st.header("Aggregated Bike Trips in New York")
    st.components.v1.html(html_data,height=1000)
    
    
    
    
elif page == "Intro page":
    
    
   
    st.title("Divvy Bikes Strategy Dashboard")
    st.markdown("The dashboard will help with the expansion problems Divvy currently faces")
    st.markdown("Right now, Divvy bikes runs into a situation where customers complain about bikes not being avaibale at certain times. This analysis aims to look at the potential reasons behind this.")
    
    
    
    
    
    
elif page == "Recommendations":
    st.title("Future recomendations")
    st.markdown("The dashboard will help with the expansion problems Divvy currently faces")