# graficas_datos_morfometricos
Se tiene una serie de datos morfométricos previamente estandarizados y procesados en una rutina de python anterior. 
En la rutina actual se siguen los siguientes pasos: 
Es necesario reunir los datos en los grupos previamente mencionados con el fin de graficar con base en esta separación  
Se generan los diferentes gráficos: 
* Boxplot: En este caso se genera un boxplot por cada variable medida, en este caso se generarán aproximadamente 30 gráficas, ya que de esta forma es posible evidenciar si hay diferencias significativas entre los grupos, si hay outliers y de primera mano, en caso de que el rango de algún boxplot difiera del otro (es decir, que no lo contenga) se podría pensar que es una especie diferente. 
### * PCA: El análisis de componentes principales permite identificar patrones y así diferenciar entre especies en caso de que difieran. 
### * Density plots: Permite ver la concentración de los datos y evidenciar la distribución de probabilidad, permitiendo identificar patrones. En este caso, al igual que el Boxplot, se genera un gráfico por variable.
### * Heat map: El mapa de calor de correlación permite identificar el nivel de relación que existe entre las variables, si es inversamente proporcional o directamente proporcional. 
### * Gráfica de barras: Funciona para comparar la magnitud de las variables, en este caso, también se puede ver si hay diferencias entre grupos. 

El código funciona solamente para archivos excel y fue especificamente creado para los datos propios por lo tanto, si requiere usarlo en otro tipo de datos, se sugiere probarlo y modificarlo ya que es posible que no funcione. 

Se sugiere probar el código con el archivo: 07_archivo_logaritmo_aplicado.xlsx  (el cual es el último archivo o el archi final que genera el código presente en mi anterior repositorio) 
