import pandas as pd 
import plotly.express as px
import streamlit as st 

#Cargar el DF
car_data = pd.read_csv('C:\\Users\\Sandra Serrano\\car_analysis\\vehicles_us.csv')

#Encabezado
st.header('Analisis de Datos de Anuncios de Venta de Coches')

#Boton para el histograma
hist_button = st.button('Construir Histograma')

if hist_button:
    st.write('Creando un hsitograma para la columna odmometro...')
    fig = px.histogram(car_data, x='odometer')
    st.plotly_chart(fig,use_container_width=True)

#Boton para grafico de dispercion
scatter_button = st.button('Construir grafico de dispersion')

if scatter_button:
    st.write('Creando un grafico de dispersion...')
    fig = px.scatter(car_data, x='price', y='odometer')
    st.plotly_chart(fig, use_container_width=True)