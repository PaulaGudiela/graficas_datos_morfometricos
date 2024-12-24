import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.decomposition import PCA

# Solicitar la ruta del archivo Excel al usuario
archivo = input("Ingresa la ruta del archivo Excel: ")

# Cargar el archivo Excel
df = pd.read_excel(archivo, index_col=0)

# Nombres de las muestras de cada grupo
grupo_1 = ['AOL1495', 'AOL1496', 'AOL1498', 'AOL1501', 'AOL1502', 'UN1620', 'UN1622', 'UN1624', 'AOL1497', 'AOL1494']
grupo_2 = ['AOL1492', 'AOL1493', 'UN1623', 'P7496']

# Filtrar las muestras para cada grupo
grupo_1_muestras = df[df.index.isin(grupo_1)]
grupo_2_muestras = df[df.index.isin(grupo_2)]
grupo_3_muestras = df[~df.index.isin(grupo_1 + grupo_2)]

# Unir todos los grupos para hacer las gráficas
df_completo = pd.concat([grupo_1_muestras, grupo_2_muestras, grupo_3_muestras], axis=0)
df_completo['Grupo'] = ['Grupo 1']*len(grupo_1_muestras) + ['Grupo 2']*len(grupo_2_muestras) + ['Grupo 3']*len(grupo_3_muestras)

# Restablecer el índice para evitar duplicados
df_completo_reset = df_completo.reset_index(drop=True)

# Convertir los datos a formato largo
df_long = df_completo_reset.reset_index().melt(id_vars=['Grupo', 'index'], var_name='Variable', value_name='Valor')
df_long = df_long.rename(columns={'index': 'Muestra'})

# 1. Boxplots individuales para cada variable
for variable in df_completo_reset.drop(columns='Grupo').columns:
    plt.figure(figsize=(8, 6))
    sns.boxplot(x='Grupo', y=variable, data=df_completo_reset, palette='Set2', showmeans=True)
    plt.title(f'Boxplot de {variable}')
    plt.xlabel('Grupo')
    plt.ylabel(variable)
    plt.savefig(f'boxplot_{variable}.png')  # Guardar cada boxplot con el nombre de la variable
    plt.show()  # Mostrar la gráfica

# 2. PCA (Análisis de Componentes Principales)
# Seleccionar solo las columnas numéricas
df_pca = df_completo_reset.drop(columns='Grupo')

# Aplicar PCA (sin estandarización, ya que los datos están estandarizados)
pca = PCA(n_components=2)
pca_result = pca.fit_transform(df_pca)

# Crear un DataFrame con los resultados de PCA
df_pca_result = pd.DataFrame(data=pca_result, columns=['PC1', 'PC2'])

# Agregar el grupo para colorear los puntos
df_pca_result['Grupo'] = df_completo_reset['Grupo'].values

# Graficar el PCA
plt.figure(figsize=(8, 6))
sns.scatterplot(x='PC1', y='PC2', hue='Grupo', data=df_pca_result, palette='Set2', s=100, marker='o')
plt.title('PCA: Primeras dos componentes principales')
plt.xlabel('Componente Principal 1')
plt.ylabel('Componente Principal 2')
plt.legend(title='Grupo')
plt.savefig('pca_scatterplot.png')  # Guardar la gráfica del PCA
plt.show()  # Mostrar la gráfica del PCA

# 3. Density Plots para cada variable
for variable in df_completo_reset.drop(columns='Grupo').columns:
    plt.figure(figsize=(8, 6))
    sns.kdeplot(data=df_completo_reset, x=variable, hue='Grupo', fill=True, common_norm=False, palette='Set2')
    plt.title(f'Density Plot de {variable}')
    plt.xlabel(variable)
    plt.ylabel('Densidad')
    plt.savefig(f'density_plot_{variable}.png')  # Guardar el density plot con el nombre de la variable
    plt.show()  # Mostrar el density plot

# 4. Heatmap de correlación entre variables
correlation_matrix = df_completo_reset.drop(columns='Grupo').corr()

# Graficar el heatmap
plt.figure(figsize=(10, 8))
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', fmt='.2f', linewidths=0.5, cbar_kws={"shrink": 0.75})
plt.title('Heatmap de Correlación entre Variables')
plt.savefig('heatmap_correlacion.png')  # Guardar el heatmap de correlación
plt.show()  # Mostrar el heatmap de correlación



# 5a. Gráfica de barras con todas las variables
df_long = df_completo_reset.reset_index().melt(id_vars=['Grupo'], var_name='Variable', value_name='Valor')
plt.figure(figsize=(12, 8))
sns.barplot(x='Variable', y='Valor', hue='Grupo', data=df_long, palette='Set2')
plt.title('Gráfica de Barras para todas las Variables')
plt.xlabel('Variable')
plt.ylabel('Valor')
plt.xticks(rotation=90)  # Rotar las etiquetas del eje x para mayor claridad
plt.tight_layout()  # Ajustar el layout
plt.savefig('barplot_todas_las_variables.png')  # Guardar la gráfica de barras
plt.show()  # Mostrar la gráfica de barras


# 5b. Gráfica de barras para cada variable
#for variable in df_completo_reset.drop(columns='Grupo').columns:
#    plt.figure(figsize=(8, 6))
#    sns.barplot(x='Grupo', y=variable, data=df_completo_reset, palette='Set2', ci=None)
#    plt.title(f'Gráfica de Barras de {variable}')
#    plt.xlabel('Grupo')
#    plt.ylabel(variable)
#    plt.savefig(f'barplot_{variable}.png')  # Guardar la gráfica de barras con el nombre de la variable
#    plt.show()  # Mostrar la gráfica de barras