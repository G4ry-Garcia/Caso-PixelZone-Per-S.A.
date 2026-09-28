import pandas as pd

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

