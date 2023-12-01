import pandas as pd
import matplotlib.pyplot as plt


# Lee el archivo CSV y establece la columna "City" como el índice del DataFrame.
df = pd.read_csv("cities.csv")

print(df.to_string())

print("..............................................\n")

# Imprime el numero de columnas dadas como parametro
print(df.loc[[1,4]])
print("..............................................\n")

# da  las primeras 10 lineas
print(df.head(20))
print("..............................................\n")
# da las ultimas 10 lineas
print(df.tail(10))
print("..............................................\n")

# da la informacion 

print(df.info())

print("..............................................\n")

print("....................Limpieza de Datos..........................\n")

#Elimina los datos que tengan valor nulo
new_df = df.dropna()
print("Limpiando Datos Nulos")
print(new_df.to_string())

print("..............................................\n")
#Elimana los rows que contengan un valor nulo 

df.dropna(inplace =True)
print(df.to_string())

print("..............................................\n")

#Remplacar los valores nulos con otro valor 

df.fillna(0, inplace = True)

#Remplazar los valores nulos de una cierta columna

#df[nombre columna].fillna(0, inplace = True)

print("..............................................\n")

# Sacar la media
print("Media")

x = df["LatD"].median()
print(x)

# Sacar la moda
print("Moda")
y = df["LatD"].mode()
print(y)
# Sacar el promedio
print("Promedio") 
z = df["LatD"].mean()
print(z)
print("..............................................\n")

#Remover columnas

# df.dropna(subet=["nombre columna"], inplace = True)

print(".....................Remover duplicados.........................\n")

# Verifica si hay datos duplicados 
print(df.duplicated())

# Remueve los datos duplicados 
df.drop_duplicates(inplace = True)

print(".....................Plot.........................\n")

df["LatD"].plot()

plt.show()


