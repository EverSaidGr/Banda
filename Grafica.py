#----------------------------------------Importacion de librerias-----------------------------------
import pandas as pd#Libreria para analisis de datos
import matplotlib.pyplot as plt#Libreria para graficacion 

#------------------------------------------------Enlace con documento--------------------------------------
workbook1="Ejercicio01.xlsx"#Nombre del documento
df=pd.read_excel(workbook1)#Leer datos del documento
df.columns=['Frecuencia', 'Amplitud']#Cambio de nombre a las columnas


ampmax=df['Amplitud'].max()
idamMax=df['Amplitud'].idxmax()
f0=df.loc[df['Amplitud'].idxmax(),'Frecuencia']
print ('Amplitud maxima= ', ampmax)
print ('F0= ', f0)

b=ampmax-3
print(b)



#---------------------------------------Graficacion---------------------------------------
valores=df[['Frecuencia','Amplitud']]#Nombre de las columnas a utilizar en la grafica
ax=valores.plot(x='Frecuencia',y='Amplitud',rot=0)#Asignacion de las columnas a los ejes
plt.show()#Mostrar interfaz
