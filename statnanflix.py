import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import plotly.express as px
import plotly.graph_objects as go
import plotly.figure_factory as ff
import datetime
 
from plotly.subplots import make_subplots

link = "https://raw.githubusercontent.com/marcpiveteau/projet2/main/tableallege4.csv"
table = pd.read_csv(link)

link2="https://raw.githubusercontent.com/marcpiveteau/projet2/main/tableactexplode.csv"
tableact =pd.read_csv(link2)


st.title('Bienvenue sur Nanflix!')


st.markdown("![Alt Text](https://github.com/marcpiveteau/projet2/blob/main/cinemananflix.jpg?raw=true)")




listevote = [i for i in range(0,2600000,100000)]
today = datetime.date.today()
premieredate = datetime.date(1910, 1, 1)
start_date=st.date_input('date de début:', premieredate)
end_date = st.date_input('Date de fin :')
nombredevote = st.selectbox('nombre de votes mini',listevote)
st.write("vous avez selectionner de l'année:", start_date, "à l'année", end_date, " avec au minimum ", nombredevote," de votes")

tablegraph= table[[ 'année_du_film', 'durée_du_film', 'genres', 'titre', 'Réalisateur','notes_du_film', 'numVotes', 'scenariste', 'acteur_actrisse']]
tablegraph['genres'] = tablegraph['genres'].str.split(',')
tablegraph2 = tablegraph.explode('genres')
tablegraph2['année_du_film'] = pd.to_datetime(tablegraph2['année_du_film'],format='%Y')
jaugegenreannée =tablegraph2[tablegraph2['année_du_film'].isin(pd.date_range(start_date, end_date))]
jaugegenreannée = jaugegenreannée[jaugegenreannée['numVotes'] > nombredevote]
tablegenre = jaugegenreannée.groupby(by='genres').count().reset_index()

fig1 = px.bar(tablegenre,x='genres', y="titre",color='genres',labels={"titre" : "nombre de film"})
fig1.update_layout(
     title={'text': "films par genres sur la periode",'x':0.5,'xanchor': 'center','yanchor': 'top'},
    title_font_family="Times New Roman",
    title_font_color="#FA0087")
st.plotly_chart(fig1)

fig12 = px.pie(tablegenre, values= 'titre', names='genres')
fig12.update_layout(
     title={'text': "pourcentage par genres sur la periode",'x':0.5,'xanchor': 'center','yanchor': 'top'},
    title_font_family="Times New Roman",
    title_font_color="#FA0087")
st.plotly_chart(fig12)

tablegenre2 =jaugegenreannée.groupby(by='genres').mean().reset_index()
choixstatgenr = st.selectbox('que voulez vous voir ?',['moyenne des notes','durée moyenne des films','nombres de vote en moyenne'])
if choixstatgenr=='moyenne des notes':
	fig4 = px.bar(tablegenre2, x='genres', y="notes_du_film",color='genres',labels={"notes_du_film" : "moyenne des notes"})
	fig4.update_layout(
     title={'text': "moyenne des notes par genres",'x':0.5,'xanchor': 'center','yanchor': 'top'},
    title_font_family="Times New Roman",
    title_font_color="#FA0087")
if choixstatgenr=='durée moyenne des films':
	fig4 = px.bar(tablegenre2, x='genres', y="durée_du_film",color='genres',labels={"durée_du_film" : "moyenne des durées"})
	fig4.update_layout(
     title={'text': "moyenne des durées par genres",'x':0.5,'xanchor': 'center','yanchor': 'top'},
    title_font_family="Times New Roman",
    title_font_color="#FA0087")
if choixstatgenr=='nombres de vote en moyenne':
	fig4 = px.bar(tablegenre2, x='genres', y="numVotes",color='genres',labels={"numVotes" : "moyenne de nombres de votes"})
	fig4.update_layout(
     title={'text': "moyenne du nombres de votes par genres( attention celle-ci est faussé suivant la selection)",'x':0.5,'xanchor': 'center','yanchor': 'top'},
    title_font_family="Times New Roman",
    title_font_color="#FA0087")

st.plotly_chart(fig4)



nbdirector = [i for i in range(1,21)]
nbchdir = st.selectbox('combien de réalisateurs veux tu voir ? ',nbdirector)
choixstat= st.selectbox('que voulez vous voir ?',['moyenne des notes','nombres de film réalisé'])
tablegraph3= table[[ 'année_du_film', 'durée_du_film', 'genres', 'titre','Réalisateur', 'notes_du_film', 'numVotes', 'scenariste','acteur_actrisse']]
tablegraph3['année_du_film'] = pd.to_datetime(tablegraph3['année_du_film'],format='%Y')
table1quantile = tablegraph3[tablegraph3['numVotes'] > nombredevote]
if choixstat=='moyenne des notes':
	tabledirector1 = table1quantile.groupby(by='Réalisateur').mean()
	tabledirector2 = tabledirector1.sort_values(by='notes_du_film', ascending= False).reset_index()
	tabledirector3 = tabledirector2.iloc[:nbchdir,:]
if choixstat=='nombres de film réalisé':
	tabledirector1 = table1quantile.groupby(by='Réalisateur').count()
	tabledirector2 = tabledirector1.sort_values(by='notes_du_film', ascending= False).reset_index()
	tabledirector3 = tabledirector2.iloc[:nbchdir,:]

fig2 = px.bar(tabledirector3,x='Réalisateur', y='notes_du_film',color='Réalisateur',animation_group='Réalisateur',labels={"notes_du_film" : choixstat})
fig2.update_layout(
     title={'text': "classement des réalisateurs",'x':0.5,'xanchor': 'center','yanchor': 'top'},
    title_font_family="Times New Roman",
    title_font_color="#FA0087")
st.plotly_chart(fig2)

nbacteur = [i for i in range(1,21)]
nbchact = st.selectbox("combien d'acteur et actrice veux tu voir ? ",nbacteur)
choixstat1= st.selectbox('que voulez vous voir ?',['moyenne des notes','nombres de film joué'])
tablegraph4= tableact[[ 'année_du_film', 'durée_du_film', 'genres', 'titre','Réalisateur', 'notes_du_film', 'numVotes', 'scenariste','acteur_actrisse']]
tablegraph4['année_du_film'] = pd.to_datetime(tablegraph3['année_du_film'],format='%Y')
table2quantile = tablegraph4[tablegraph4['numVotes'] > nombredevote]
if choixstat1=='moyenne des notes':
	tableacteur1 = table2quantile.groupby(by='acteur_actrisse').mean()
	tableacteur2 = tableacteur1.sort_values(by='notes_du_film', ascending= False).reset_index()
	tableacteur3 = tableacteur2.iloc[:nbchact,:]
if choixstat1=='nombres de film joué':
	tableacteur1 = table2quantile.groupby(by='acteur_actrisse').count()
	tableacteur2 = tableacteur1.sort_values(by='notes_du_film', ascending= False).reset_index()
	tableacteur3 = tableacteur2.iloc[:nbchact,:]

fig3 = px.bar(tableacteur3,x='acteur_actrisse', y='notes_du_film', title="classement des acteur et actrice",color='acteur_actrisse',animation_group='acteur_actrisse',labels={"notes_du_film" : choixstat1, "acteur_actrisse": "acteur ou actrice"})
fig3.update_layout(
     title={'text': "classement des acteurs ou actrices",'x':0.5,'xanchor': 'center','yanchor': 'top'},
    title_font_family="Times New Roman",
    title_font_color="#FA0087")
st.plotly_chart(fig3)



genreselectionner=st.selectbox('selectionner un gerne pour voir la liste des films sur cette periode', ['Action','Adult','Adventure','Animation','Biography','Comedy','Crime','Documentary','Drama','Family','Fantasy','Film-Noir','History','Horror','Music','Musical','Mystery','News','Romance','Sci-Fi','Sport','Thriller','War','Western'])

film = jaugegenreannée[jaugegenreannée['genres']==genreselectionner]
film =film[['année_du_film','genres','titre','Réalisateur','notes_du_film','numVotes', 'scenariste','acteur_actrisse']]
st.dataframe(film)
