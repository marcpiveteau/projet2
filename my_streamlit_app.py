import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np



st.title('Hello Wilders, welcome to my Marc application!')

query = st.text_input("entre ton film preferé")
st.write(query)



st.button("test bouton") 
  
if(st.button("terminator")): 
    st.markdown(link, unsafe_allow_html=True) 


film = st.selectbox("best film: ", 
                     ['terminator', 'predator', 'titanic']) 
  
st.write("Your movie preferé: ", film) 

link = "https://raw.githubusercontent.com/murpi/wilddata/master/quests/weather2019.csv"
df_weather = pd.read_csv(link)

st.line_chart(df_weather['MAX_TEMPERATURE_C'])

import seaborn as sns
viz_correlation = sns.heatmap(df_weather.corr(), 
                                center=0,
                                cmap = sns.color_palette("vlag", as_cmap=True)
                                )

st.pyplot(viz_correlation.figure)
	

if(st.button("coup de pied")): 
    st.text("coup de pied 22") 
if(st.button("coup de poing")): 
    st.text("coup de poing 22")
if(st.button("recharge vie")): 
    st.text("recharge 22")