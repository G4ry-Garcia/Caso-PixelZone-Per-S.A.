import pandas as pd
from pathlib import Path
import numpy as np


data = pd.read_csv("../DATA/dataset.txt")

#Creamos un array con los valores de la cabecera
Datos =["ID","Store ID","Total Price","Base Price","Units Sold"]

#Remplazamos el valor vacio por "Desconocido"
data[Datos]=data[Datos].fillna("Desconocido")
print(data)

# Corroboramos que filas han sido modificadas
filas_modificadas = data[data[Datos].isin(["Desconocido"]).any(axis=1)]
print("-" * 200)

print(filas_modificadas)

#Convertimos en 0 el valor Desconocido
data["Total Price"] = pd.to_numeric(data["Total Price"], errors="coerce")

# 1. Buscamos la fila donde estaba el valor desconocido
id_buscado = 193915
resultado = data[data["ID"] == id_buscado]

print(resultado)
#-------------Calculando medidas de tendencia central----------

#"Calcularemos la media y mediana por Store ID con las unidades vendidas"

#1er paso, quitamos los limites para la visualización

#pd.set_option("display.max_rows", None)
#pd.set_option("display.max_columns", None)
#pd.set_option("display.width", None)

#2do paso, agrupamos las columnas que necesitamos y calculamos la media, mediana y moda

agrupado = data.groupby("Store ID")["Units Sold"].agg(["mean","median"]).round(2)

#print("-" * 200)
#print(agrupado)

# Creamos las nuevas columnas

resultado = (data.groupby('Store ID') ['Units Sold']
          .agg(Media_de_unidades_vendidas="mean",Mediana_de_unidades_vendidas="median")
          .round(2)
          .reset_index())
print("-" * 200)
print(resultado)

#"Calcularemos la media y mediana por Store ID con el precio total y precio base"

#"Calcularemos los descuentos aplicados"

data["Descuento"] = data["Base Price"] - data["Total Price"]

data["Descuento_%"] = data["Descuento"]/data["Base Price"] *100

agrupados = (data.groupby(["ID","Store ID"])
             .agg(
                Descuento_Total=('Descuento', 'sum'),
                Porcentaje_de_descuento=('Descuento_%', 'mean')
            )
             .round(2)
             .reset_index())
print(agrupados)
