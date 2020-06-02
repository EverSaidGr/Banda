#----------------------------------------Importacion de librerias-----------------------------------
import pandas as pd # Librería para análisis de datos
import matplotlib.pyplot as plt #Librería para graficación

#------------------------------------------------Enlace con documento--------------------------------------
workbook1 = "Ejercicio01.xlsx" # Nombre del documento
df = pd.read_excel(workbook1) # Leer datos del documento

#---------------------------------------------Formato--------------------------------
df.columns = ['Frecuencia', 'Amplitud'] # Cambio de nombre a las columnas

#-----------------------------------------Variables de entrada-----------------
amp_max = df['Amplitud'].max()
f0 = df.loc[df['Amplitud'].idxmax(), 'Frecuencia']
print('Amplitud máxima =', amp_max)
print('F0 =', f0)
b = amp_max - 3
print('B', b)

# ---------------------------------Calculemos f2------------------------------
m1=df[(df.index<=df['Amplitud'].idxmax())]
print(m1)
nearest_values = df.iloc[(m1['Amplitud'] - b).abs().argsort()[:2]]
print(nearest_values)
y2 = nearest_values.iloc[1,1]
y1 = nearest_values.iloc[0,1]
x2 = nearest_values.iloc[1,0]
x1 = nearest_values.iloc[0,0]
print ( 'y2', y2)
print ('y1',y1)
print ('x2',x2)
print ('x1',x1)
m = (y2 - y1) / (x2 - x1)
print ('m',m)
f1 = (b - y1 + (m * x1)) / m
print('f1', f1)

# ---------------------------------Calculemos f2------------------------------
m2=df[(df.index>=df['Amplitud'].idxmax())]
print(m2)
nearest_values_two = df.iloc[(m2['Amplitud'] - b).abs().argsort()[:2]]
print(nearest_values_two)
print(b)
y4 = nearest_values_two.iloc[1,1]
y3 = nearest_values_two.iloc[0,1]
x4 = nearest_values_two.iloc[1,0]
x3 = nearest_values_two.iloc[0,0]
print ( 'y4', y4)
print ('y3',y3)
print ('x4',x4)
print ('x3',x3)
m = (y4 - y3) / (x4 - x3)
print ('m',m)
f2 = (b - y3 + (m * x3)) / m
print('f2', f2)


#------------------------------Calcular ancho de banda
print('Ancho de banda: ', abs(f1 - f2))

#---------------------------------------Graficacion---------------------------------------
valores=df[['Frecuencia','Amplitud']] # Nombre de las columnas a utilizar en la gráfica
ax=valores.plot(x='Frecuencia',y='Amplitud',rot=0) # Asignación de las columnas a los ejes
plt.show() # Mostrar interfaz