# -*- coding: utf-8 -*-
"""
Created on Sat Apr 23 09:33:10 2022

@author: jahop_fz60h0
"""

import streamlit as st
from streamlit_option_menu import option_menu
#from streamlit_lottie import st_lottie  # pip install streamlit-lottie
import streamlit.components.v1 as components
import requests  # pip install requests
import plotly.express as px

import pandas as pd
#import numpy as np

#import plotly.graph_objects as go 


from PIL import Image

image = Image.open('pemex.png')
st.image(image)


    
st.title("Modelado de Sistemas Petroleros")
page_names = ['Abdiel Levi Aquino Ibarra', 'Horacio Alberto Contreras Navarro', 'Jorge Balcazar Balcazar', 'Juan Armando Romero Guadarrama', 'Lilian Mareni Luna de Anda', 'Marisol Polet Pinzón Sotelo', 'Monica Angelina Solís Sánchez', 'Oscar Augusto González Verde', 'Oscar Cuevas Sánchez', 'Silvia Silva Mendoza', 'Unión de los gráficos']

page = st.radio('Navegación', page_names, index = 0)
#st.write("**La variable 'page' returns:**", page)

data = pd.read_csv("NDR.csv")
data = data.set_index('PROFESIONISTAS')

#col1, col2, col3 = st.columns(3)

col1, col2 = st.columns([100, 100])

col1.subheader("DATOS")
col1.write(data)


#1                    
if page == 'Abdiel Levi Aquino Ibarra':
   #st.title(f"Has seleccionado {selected}")
   fig = px.line(x=["Calidad de roca almacén", "Estratigrafía de Secuencias de sistemas carbonatados", "Estratigrafía de Secuencias de sistemas clásticos", "Sedimentología y análisis de facies de clásticos", "Sedimentología y análisis de facies de rocas carbonatadas", "Mapeo, correlaciones estratigráficas y estructurales", "Geología estructural y restauración", "Modelo geológico y mapeo de propiedades 3D", "Tectónica salina y arcilla", "Análisis de cuencas y sistemas petroleros", "Análisis de roca generadora", "Análisis de rutas de migración", "Análisis de sellos", "Exploración y análisis de plays", "Geoquímica del petróleo", "Reconstrucción estructural, paleogeografía y tectónica", "Interpretación estructural 2D/3D", "Análisis de riesgo geológico", "Estimación de recursos y reservas", "Integración de geociencias"], y=[2,2,3,2,1,3,3,3,3,4,3,4,2,3,3,2,2,3,2,3])
   fig.update_layout(yaxis_title='Nivel de dominio', xaxis_title = 'Competencias', title='Abdiel Levi Aquino Ibarra', autosize=True, height=700, width = 1900, font=dict(family="bold, monospace", size=15, color="black"))
   fig.update_yaxes(range = [0,5])
   st.plotly_chart(fig)
   #fig.show()
else:   
   st.subheader("")
   st.write("")
   
#2                
if page == 'Horacio Alberto Contreras Navarro':
   #st.title(f"Has seleccionado {selected}")
   fig = px.line(x=["Calidad de roca almacén", "Estratigrafía de Secuencias de sistemas carbonatados", "Estratigrafía de Secuencias de sistemas clásticos", "Sedimentología y análisis de facies de clásticos", "Sedimentología y análisis de facies de rocas carbonatadas", "Mapeo, correlaciones estratigráficas y estructurales", "Geología estructural y restauración", "Modelo geológico y mapeo de propiedades 3D", "Tectónica salina y arcilla", "Análisis de cuencas y sistemas petroleros", "Análisis de roca generadora", "Análisis de rutas de migración", "Análisis de sellos", "Exploración y análisis de plays", "Geoquímica del petróleo", "Reconstrucción estructural, paleogeografía y tectónica", "Interpretación estructural 2D/3D", "Análisis de riesgo geológico", "Estimación de recursos y reservas", "Integración de geociencias"], y=[2,2,2,2,2,2,2,1,1,3,2,2,2,2,1,2,1,2,1,2])
   fig.update_layout(yaxis_title='Nivel de dominio', xaxis_title = 'Competencias', title='Horacio Alberto Contreras Navarro', autosize=True, height=700, width = 1900, font=dict(family="bold, monospace", size=15, color="black"))
   fig.update_yaxes(range = [0,5])
   st.plotly_chart(fig)
   #fig.show()
else:   
   st.subheader("")
   st.write("")

#3                    
if page == 'Jorge Balcazar Balcazar':
   #st.title(f"Has seleccionado {selected}")
   fig = px.line(x=["Calidad de roca almacén", "Estratigrafía de Secuencias de sistemas carbonatados", "Estratigrafía de Secuencias de sistemas clásticos", "Sedimentología y análisis de facies de clásticos", "Sedimentología y análisis de facies de rocas carbonatadas", "Mapeo, correlaciones estratigráficas y estructurales", "Geología estructural y restauración", "Modelo geológico y mapeo de propiedades 3D", "Tectónica salina y arcilla", "Análisis de cuencas y sistemas petroleros", "Análisis de roca generadora", "Análisis de rutas de migración", "Análisis de sellos", "Exploración y análisis de plays", "Geoquímica del petróleo", "Reconstrucción estructural, paleogeografía y tectónica", "Interpretación estructural 2D/3D", "Análisis de riesgo geológico", "Estimación de recursos y reservas", "Integración de geociencias"], y=[2,1,1,1,1,2,1,1,1,2,1,1,1,2,1,1,1,1,1,2])
   fig.update_layout(yaxis_title='Nivel de dominio', xaxis_title = 'Competencias', title='Jorge Balcazar Balcazar', autosize=True, height=700, width = 1900, font=dict(family="bold, monospace", size=15, color="black"))
   fig.update_yaxes(range = [0,5])
   st.plotly_chart(fig)
   #fig.show()
else:   
   st.subheader("")
   st.write("")

#4                   
if page == 'Juan Armando Romero Guadarrama':
   #st.title(f"Has seleccionado {selected}")
   fig = px.line(x=["Calidad de roca almacén", "Estratigrafía de Secuencias de sistemas carbonatados", "Estratigrafía de Secuencias de sistemas clásticos", "Sedimentología y análisis de facies de clásticos", "Sedimentología y análisis de facies de rocas carbonatadas", "Mapeo, correlaciones estratigráficas y estructurales", "Geología estructural y restauración", "Modelo geológico y mapeo de propiedades 3D", "Tectónica salina y arcilla", "Análisis de cuencas y sistemas petroleros", "Análisis de roca generadora", "Análisis de rutas de migración", "Análisis de sellos", "Exploración y análisis de plays", "Geoquímica del petróleo", "Reconstrucción estructural, paleogeografía y tectónica", "Interpretación estructural 2D/3D", "Análisis de riesgo geológico", "Estimación de recursos y reservas", "Integración de geociencias"], y=[3,2,2,2,2,2,2,1,2,3,3,2,2,3,3,2,2,1,2,2])
   fig.update_layout(yaxis_title='Nivel de dominio', xaxis_title = 'Competencias', title='Juan Armando Romero Guadarrama', autosize=True, height=700, width = 1900, font=dict(family="bold, monospace", size=15, color="black"))
   fig.update_yaxes(range = [0,5])
   st.plotly_chart(fig)
   #fig.show()
else:   
   st.subheader("")
   st.write("")

#5                   
if page == 'Lilian Mareni Luna de Anda':
   #st.title(f"Has seleccionado {selected}")
   fig = px.line(x=["Calidad de roca almacén", "Estratigrafía de Secuencias de sistemas carbonatados", "Estratigrafía de Secuencias de sistemas clásticos", "Sedimentología y análisis de facies de clásticos", "Sedimentología y análisis de facies de rocas carbonatadas", "Mapeo, correlaciones estratigráficas y estructurales", "Geología estructural y restauración", "Modelo geológico y mapeo de propiedades 3D", "Tectónica salina y arcilla", "Análisis de cuencas y sistemas petroleros", "Análisis de roca generadora", "Análisis de rutas de migración", "Análisis de sellos", "Exploración y análisis de plays", "Geoquímica del petróleo", "Reconstrucción estructural, paleogeografía y tectónica", "Interpretación estructural 2D/3D", "Análisis de riesgo geológico", "Estimación de recursos y reservas", "Integración de geociencias"], y=[2,1,1,1,2,2,2,1,1,3,3,3,2,2,3,2,1,2,1,2])
   fig.update_layout(yaxis_title='Nivel de dominio', xaxis_title = 'Competencias', title='Lilian Mareni Luna de Anda', autosize=True, height=700, width = 1900, font=dict(family="bold, monospace", size=15, color="black"))
   fig.update_yaxes(range = [0,5])
   st.plotly_chart(fig)
   #fig.show()
else:   
   st.subheader("")
   st.write("")

#6                   
if page == 'Marisol Polet Pinzón Sotelo':
   #st.title(f"Has seleccionado {selected}")
   fig = px.line(x=["Calidad de roca almacén", "Estratigrafía de Secuencias de sistemas carbonatados", "Estratigrafía de Secuencias de sistemas clásticos", "Sedimentología y análisis de facies de clásticos", "Sedimentología y análisis de facies de rocas carbonatadas", "Mapeo, correlaciones estratigráficas y estructurales", "Geología estructural y restauración", "Modelo geológico y mapeo de propiedades 3D", "Tectónica salina y arcilla", "Análisis de cuencas y sistemas petroleros", "Análisis de roca generadora", "Análisis de rutas de migración", "Análisis de sellos", "Exploración y análisis de plays", "Geoquímica del petróleo", "Reconstrucción estructural, paleogeografía y tectónica", "Interpretación estructural 2D/3D", "Análisis de riesgo geológico", "Estimación de recursos y reservas", "Integración de geociencias"], y=[2,2,3,2,2,3,2,2,3,3,3,3,3,3,3,2,3,2,2,2])
   fig.update_layout(yaxis_title='Nivel de dominio', xaxis_title = 'Competencias', title='Marisol Polet Pinzón Sotelo', autosize=True, height=700, width = 1900, font=dict(family="bold, monospace", size=15, color="black"))
   fig.update_yaxes(range = [0,5])
   st.plotly_chart(fig)
   #fig.show()
else:   
   st.subheader("")
   st.write("")

#7                   
if page == 'Monica Angelina Solís Sánchez':
   #st.title(f"Has seleccionado {selected}")
   fig = px.line(x=["Calidad de roca almacén", "Estratigrafía de Secuencias de sistemas carbonatados", "Estratigrafía de Secuencias de sistemas clásticos", "Sedimentología y análisis de facies de clásticos", "Sedimentología y análisis de facies de rocas carbonatadas", "Mapeo, correlaciones estratigráficas y estructurales", "Geología estructural y restauración", "Modelo geológico y mapeo de propiedades 3D", "Tectónica salina y arcilla", "Análisis de cuencas y sistemas petroleros", "Análisis de roca generadora", "Análisis de rutas de migración", "Análisis de sellos", "Exploración y análisis de plays", "Geoquímica del petróleo", "Reconstrucción estructural, paleogeografía y tectónica", "Interpretación estructural 2D/3D", "Análisis de riesgo geológico", "Estimación de recursos y reservas", "Integración de geociencias"], y=[2,1,1,1,2,2,2,1,1,3,3,3,2,3,3,2,1,1,1,2])
   fig.update_layout(yaxis_title='Nivel de dominio', xaxis_title = 'Competencias', title='Monica Angelina Solís Sánchez', autosize=True, height=700, width = 1900, font=dict(family="bold, monospace", size=15, color="black"))
   fig.update_yaxes(range = [0,5])
   st.plotly_chart(fig)
   #fig.show()
else:   
   st.subheader("")
   st.write("")

#8                   
if page == 'Oscar Augusto González Verde':
   #st.title(f"Has seleccionado {selected}")
   fig = px.line(x=["Calidad de roca almacén", "Estratigrafía de Secuencias de sistemas carbonatados", "Estratigrafía de Secuencias de sistemas clásticos", "Sedimentología y análisis de facies de clásticos", "Sedimentología y análisis de facies de rocas carbonatadas", "Mapeo, correlaciones estratigráficas y estructurales", "Geología estructural y restauración", "Modelo geológico y mapeo de propiedades 3D", "Tectónica salina y arcilla", "Análisis de cuencas y sistemas petroleros", "Análisis de roca generadora", "Análisis de rutas de migración", "Análisis de sellos", "Exploración y análisis de plays", "Geoquímica del petróleo", "Reconstrucción estructural, paleogeografía y tectónica", "Interpretación estructural 2D/3D", "Análisis de riesgo geológico", "Estimación de recursos y reservas", "Integración de geociencias"], y=[4,3,3,3,3,3,3,4,3,3,3,2,3,3,2,3,2,2,3,2])
   fig.update_layout(yaxis_title='Nivel de dominio', xaxis_title = 'Competencias', title='Oscar Augusto González Verde', autosize=True, height=700, width = 1900, font=dict(family="bold, monospace", size=15, color="black"))
   fig.update_yaxes(range = [0,5])
   st.plotly_chart(fig)
   #fig.show()
else:   
   st.subheader("")
   st.write("")

#9             
if page == 'Oscar Cuevas Sánchez':
   #st.title(f"Has seleccionado {selected}")
   fig = px.line(x=["Calidad de roca almacén", "Estratigrafía de Secuencias de sistemas carbonatados", "Estratigrafía de Secuencias de sistemas clásticos", "Sedimentología y análisis de facies de clásticos", "Sedimentología y análisis de facies de rocas carbonatadas", "Mapeo, correlaciones estratigráficas y estructurales", "Geología estructural y restauración", "Modelo geológico y mapeo de propiedades 3D", "Tectónica salina y arcilla", "Análisis de cuencas y sistemas petroleros", "Análisis de roca generadora", "Análisis de rutas de migración", "Análisis de sellos", "Exploración y análisis de plays", "Geoquímica del petróleo", "Reconstrucción estructural, paleogeografía y tectónica", "Interpretación estructural 2D/3D", "Análisis de riesgo geológico", "Estimación de recursos y reservas", "Integración de geociencias"], y=[2,3,3,3,3,3,2,2,1,3,3,2,1,2,1,2,2,1,1,2])
   fig.update_layout(yaxis_title='Nivel de dominio', xaxis_title = 'Competencias', title='Oscar Cuevas Sánchez', autosize=True, height=700, width = 1900, font=dict(family="bold, monospace", size=15, color="black"))
   fig.update_yaxes(range = [0,5])
   st.plotly_chart(fig)
   #fig.show()
else:   
   st.subheader("")
   st.write("")

#10                    
if page == 'Silvia Silva Mendoza':
   #st.title(f"Has seleccionado {selected}")
   fig = px.line(x=["Calidad de roca almacén", "Estratigrafía de Secuencias de sistemas carbonatados", "Estratigrafía de Secuencias de sistemas clásticos", "Sedimentología y análisis de facies de clásticos", "Sedimentología y análisis de facies de rocas carbonatadas", "Mapeo, correlaciones estratigráficas y estructurales", "Geología estructural y restauración", "Modelo geológico y mapeo de propiedades 3D", "Tectónica salina y arcilla", "Análisis de cuencas y sistemas petroleros", "Análisis de roca generadora", "Análisis de rutas de migración", "Análisis de sellos", "Exploración y análisis de plays", "Geoquímica del petróleo", "Reconstrucción estructural, paleogeografía y tectónica", "Interpretación estructural 2D/3D", "Análisis de riesgo geológico", "Estimación de recursos y reservas", "Integración de geociencias"], y=[2,2,3,2,3,3,2,2,2,3,3,4,2,3,3,2,2,2,2,2])
   fig.update_layout(yaxis_title='Nivel de dominio', xaxis_title = 'Competencias', title='Silvia Silva Mendoza', autosize=True, height=700, width = 1900, font=dict(family="bold, monospace", size=15, color="black"))
   fig.update_yaxes(range = [0,5])
   st.plotly_chart(fig)
   #fig.show()
else:   
   st.subheader("")
   st.write("")

#############################################################################################################################################################




    
if page == 'Unión de los gráficos':
     fig = px.line(x=["Calidad de roca almacén", "Estratigrafía de Secuencias de sistemas carbonatados", "Estratigrafía de Secuencias de sistemas clásticos", "Sedimentología y análisis de facies de clásticos", "Sedimentología y análisis de facies de rocas carbonatadas", "Mapeo, correlaciones estratigráficas y estructurales", "Geología estructural y restauración", "Modelo geológico y mapeo de propiedades 3D", "Tectónica salina y arcilla", "Análisis de cuencas y sistemas petroleros", "Análisis de roca generadora", "Análisis de rutas de migración", "Análisis de sellos", "Exploración y análisis de plays", "Geoquímica del petróleo", "Reconstrucción estructural, paleogeografía y tectónica", "Interpretación estructural 2D/3D", "Análisis de riesgo geológico", "Estimación de recursos y reservas", "Integración de geociencias"], y=[2,2,3,2,1,3,3,3,3,4,3,4,2,3,3,2,2,3,2,3])
     fig.update_layout(yaxis_title='Nivel de dominio', xaxis_title = 'Competencias', autosize=True, height=700, width = 1900, font=dict(family="bold, monospace", size=15, color="black"))
     fig.update_yaxes(range = [0,5])
     #fig.update_traces(name='Ariel Ramírez Díaz')

     fig.add_scatter(name = 'Abdiel Levi Aquino Ibarra', x=["Calidad de roca almacén", "Estratigrafía de Secuencias de sistemas carbonatados", "Estratigrafía de Secuencias de sistemas clásticos", "Sedimentología y análisis de facies de clásticos", "Sedimentología y análisis de facies de rocas carbonatadas", "Mapeo, correlaciones estratigráficas y estructurales", "Geología estructural y restauración", "Modelo geológico y mapeo de propiedades 3D", "Tectónica salina y arcilla", "Análisis de cuencas y sistemas petroleros", "Análisis de roca generadora", "Análisis de rutas de migración", "Análisis de sellos", "Exploración y análisis de plays", "Geoquímica del petróleo", "Reconstrucción estructural, paleogeografía y tectónica", "Interpretación estructural 2D/3D", "Análisis de riesgo geológico", "Estimación de recursos y reservas", "Integración de geociencias"], y=[2,2,3,2,1,3,3,3,3,4,3,4,2,3,3,2,2,3,2,3])
     fig.update_layout(yaxis_title='Nivel de dominio', xaxis_title = 'Competencias', autosize=True, height=700, width = 1900, font=dict(family="bold, monospace", size=15, color="black"))
     fig.update_yaxes(range = [0,5])     

     #2
     fig.add_scatter(name = 'Horacio Alberto Contreras Navarro', x=["Calidad de roca almacén", "Estratigrafía de Secuencias de sistemas carbonatados", "Estratigrafía de Secuencias de sistemas clásticos", "Sedimentología y análisis de facies de clásticos", "Sedimentología y análisis de facies de rocas carbonatadas", "Mapeo, correlaciones estratigráficas y estructurales", "Geología estructural y restauración", "Modelo geológico y mapeo de propiedades 3D", "Tectónica salina y arcilla", "Análisis de cuencas y sistemas petroleros", "Análisis de roca generadora", "Análisis de rutas de migración", "Análisis de sellos", "Exploración y análisis de plays", "Geoquímica del petróleo", "Reconstrucción estructural, paleogeografía y tectónica", "Interpretación estructural 2D/3D", "Análisis de riesgo geológico", "Estimación de recursos y reservas", "Integración de geociencias"], y=[2,2,2,2,2,2,2,1,1,3,2,2,2,2,1,2,1,2,1,2])
     fig.update_layout(yaxis_title='Nivel de dominio', xaxis_title = 'Competencias', autosize=True, height=700, width = 1900, font=dict(family="bold, monospace", size=15, color="black"))
     fig.update_yaxes(range = [0,5])
 
     #3
     fig.add_scatter(name = 'Jorge Balcazar Balcazar', x=["Calidad de roca almacén", "Estratigrafía de Secuencias de sistemas carbonatados", "Estratigrafía de Secuencias de sistemas clásticos", "Sedimentología y análisis de facies de clásticos", "Sedimentología y análisis de facies de rocas carbonatadas", "Mapeo, correlaciones estratigráficas y estructurales", "Geología estructural y restauración", "Modelo geológico y mapeo de propiedades 3D", "Tectónica salina y arcilla", "Análisis de cuencas y sistemas petroleros", "Análisis de roca generadora", "Análisis de rutas de migración", "Análisis de sellos", "Exploración y análisis de plays", "Geoquímica del petróleo", "Reconstrucción estructural, paleogeografía y tectónica", "Interpretación estructural 2D/3D", "Análisis de riesgo geológico", "Estimación de recursos y reservas", "Integración de geociencias"], y=[2,1,1,1,1,2,1,1,1,2,1,1,1,2,1,1,1,1,1,2])
     fig.update_layout(yaxis_title='Nivel de dominio', xaxis_title = 'Competencias', autosize=True, height=700, width = 1900, font=dict(family="bold, monospace", size=15, color="black"))
     fig.update_yaxes(range = [0,5])

     #4
     fig.add_scatter(name = 'Juan Armando Romero Guadarrama', x=["Calidad de roca almacén", "Estratigrafía de Secuencias de sistemas carbonatados", "Estratigrafía de Secuencias de sistemas clásticos", "Sedimentología y análisis de facies de clásticos", "Sedimentología y análisis de facies de rocas carbonatadas", "Mapeo, correlaciones estratigráficas y estructurales", "Geología estructural y restauración", "Modelo geológico y mapeo de propiedades 3D", "Tectónica salina y arcilla", "Análisis de cuencas y sistemas petroleros", "Análisis de roca generadora", "Análisis de rutas de migración", "Análisis de sellos", "Exploración y análisis de plays", "Geoquímica del petróleo", "Reconstrucción estructural, paleogeografía y tectónica", "Interpretación estructural 2D/3D", "Análisis de riesgo geológico", "Estimación de recursos y reservas", "Integración de geociencias"], y=[3,2,2,2,2,2,2,1,2,3,3,2,2,3,3,2,2,1,2,2])
     fig.update_layout(yaxis_title='Nivel de dominio', xaxis_title = 'Competencias', autosize=True, height=700, width = 1900, font=dict(family="bold, monospace", size=15, color="black"))
     fig.update_yaxes(range = [0,5])

     #5
     fig.add_scatter(name = 'Lilian Mareni Luna de Anda', x=["Calidad de roca almacén", "Estratigrafía de Secuencias de sistemas carbonatados", "Estratigrafía de Secuencias de sistemas clásticos", "Sedimentología y análisis de facies de clásticos", "Sedimentología y análisis de facies de rocas carbonatadas", "Mapeo, correlaciones estratigráficas y estructurales", "Geología estructural y restauración", "Modelo geológico y mapeo de propiedades 3D", "Tectónica salina y arcilla", "Análisis de cuencas y sistemas petroleros", "Análisis de roca generadora", "Análisis de rutas de migración", "Análisis de sellos", "Exploración y análisis de plays", "Geoquímica del petróleo", "Reconstrucción estructural, paleogeografía y tectónica", "Interpretación estructural 2D/3D", "Análisis de riesgo geológico", "Estimación de recursos y reservas", "Integración de geociencias"], y=[2,1,1,1,2,2,2,1,1,3,3,3,2,2,3,2,1,2,1,2])
     fig.update_layout(yaxis_title='Nivel de dominio', xaxis_title = 'Competencias', autosize=True, height=700, width = 1900, font=dict(family="bold, monospace", size=15, color="black"))
     fig.update_yaxes(range = [0,5])

     #6
     fig.add_scatter(name = 'Marisol Polet Pinzón Sotelo', x=["Calidad de roca almacén", "Estratigrafía de Secuencias de sistemas carbonatados", "Estratigrafía de Secuencias de sistemas clásticos", "Sedimentología y análisis de facies de clásticos", "Sedimentología y análisis de facies de rocas carbonatadas", "Mapeo, correlaciones estratigráficas y estructurales", "Geología estructural y restauración", "Modelo geológico y mapeo de propiedades 3D", "Tectónica salina y arcilla", "Análisis de cuencas y sistemas petroleros", "Análisis de roca generadora", "Análisis de rutas de migración", "Análisis de sellos", "Exploración y análisis de plays", "Geoquímica del petróleo", "Reconstrucción estructural, paleogeografía y tectónica", "Interpretación estructural 2D/3D", "Análisis de riesgo geológico", "Estimación de recursos y reservas", "Integración de geociencias"], y=[2,2,3,2,2,3,2,2,3,3,3,3,3,3,3,2,3,2,2,2])
     fig.update_layout(yaxis_title='Nivel de dominio', xaxis_title = 'Competencias', autosize=True, height=700, width = 1900, font=dict(family="bold, monospace", size=15, color="black"))
     fig.update_yaxes(range = [0,5])

     #7
     fig.add_scatter(name = 'Monica Angelina Solís Sánchez', x=["Calidad de roca almacén", "Estratigrafía de Secuencias de sistemas carbonatados", "Estratigrafía de Secuencias de sistemas clásticos", "Sedimentología y análisis de facies de clásticos", "Sedimentología y análisis de facies de rocas carbonatadas", "Mapeo, correlaciones estratigráficas y estructurales", "Geología estructural y restauración", "Modelo geológico y mapeo de propiedades 3D", "Tectónica salina y arcilla", "Análisis de cuencas y sistemas petroleros", "Análisis de roca generadora", "Análisis de rutas de migración", "Análisis de sellos", "Exploración y análisis de plays", "Geoquímica del petróleo", "Reconstrucción estructural, paleogeografía y tectónica", "Interpretación estructural 2D/3D", "Análisis de riesgo geológico", "Estimación de recursos y reservas", "Integración de geociencias"], y=[2,1,1,1,2,2,2,1,1,3,3,3,2,3,3,2,1,1,1,2])
     fig.update_layout(yaxis_title='Nivel de dominio', xaxis_title = 'Competencias', autosize=True, height=700, width = 1900, font=dict(family="bold, monospace", size=15, color="black"))
     fig.update_yaxes(range = [0,5])
     

     #8
     fig.add_scatter(name = 'Oscar Augusto González Verde', x=["Calidad de roca almacén", "Estratigrafía de Secuencias de sistemas carbonatados", "Estratigrafía de Secuencias de sistemas clásticos", "Sedimentología y análisis de facies de clásticos", "Sedimentología y análisis de facies de rocas carbonatadas", "Mapeo, correlaciones estratigráficas y estructurales", "Geología estructural y restauración", "Modelo geológico y mapeo de propiedades 3D", "Tectónica salina y arcilla", "Análisis de cuencas y sistemas petroleros", "Análisis de roca generadora", "Análisis de rutas de migración", "Análisis de sellos", "Exploración y análisis de plays", "Geoquímica del petróleo", "Reconstrucción estructural, paleogeografía y tectónica", "Interpretación estructural 2D/3D", "Análisis de riesgo geológico", "Estimación de recursos y reservas", "Integración de geociencias"], y=[4,3,3,3,3,3,3,4,3,3,3,2,3,3,2,3,2,2,3,2])
     fig.update_layout(yaxis_title='Nivel de dominio', xaxis_title = 'Competencias', autosize=True, height=700, width = 1900, font=dict(family="bold, monospace", size=15, color="black"))
     fig.update_yaxes(range = [0,5])

     #9
     fig.add_scatter(name = 'Oscar Cuevas Sánchez', x=["Calidad de roca almacén", "Estratigrafía de Secuencias de sistemas carbonatados", "Estratigrafía de Secuencias de sistemas clásticos", "Sedimentología y análisis de facies de clásticos", "Sedimentología y análisis de facies de rocas carbonatadas", "Mapeo, correlaciones estratigráficas y estructurales", "Geología estructural y restauración", "Modelo geológico y mapeo de propiedades 3D", "Tectónica salina y arcilla", "Análisis de cuencas y sistemas petroleros", "Análisis de roca generadora", "Análisis de rutas de migración", "Análisis de sellos", "Exploración y análisis de plays", "Geoquímica del petróleo", "Reconstrucción estructural, paleogeografía y tectónica", "Interpretación estructural 2D/3D", "Análisis de riesgo geológico", "Estimación de recursos y reservas", "Integración de geociencias"], y=[2,3,3,3,3,3,2,2,1,3,3,2,1,2,1,2,2,1,1,2])
     fig.update_layout(yaxis_title='Nivel de dominio', xaxis_title = 'Competencias', autosize=True, height=700, width = 1900, font=dict(family="bold, monospace", size=15, color="black"))
     fig.update_yaxes(range = [0,5])

     #10
     fig.add_scatter(name = 'Silvia Silva Mendoza', x=["Calidad de roca almacén", "Estratigrafía de Secuencias de sistemas carbonatados", "Estratigrafía de Secuencias de sistemas clásticos", "Sedimentología y análisis de facies de clásticos", "Sedimentología y análisis de facies de rocas carbonatadas", "Mapeo, correlaciones estratigráficas y estructurales", "Geología estructural y restauración", "Modelo geológico y mapeo de propiedades 3D", "Tectónica salina y arcilla", "Análisis de cuencas y sistemas petroleros", "Análisis de roca generadora", "Análisis de rutas de migración", "Análisis de sellos", "Exploración y análisis de plays", "Geoquímica del petróleo", "Reconstrucción estructural, paleogeografía y tectónica", "Interpretación estructural 2D/3D", "Análisis de riesgo geológico", "Estimación de recursos y reservas", "Integración de geociencias"], y=[2,2,3,2,3,3,2,2,2,3,3,4,2,3,3,2,2,2,2,2])
     fig.update_layout(yaxis_title='Nivel de dominio', xaxis_title = 'Competencias', autosize=True, height=700, width = 1900, font=dict(family="bold, monospace", size=15, color="black"))
     fig.update_yaxes(range = [0,5])

     st.plotly_chart(fig)
     
else:
    st.subheader("")
    
    
