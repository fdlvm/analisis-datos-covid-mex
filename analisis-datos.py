## PASO 1:
## Importar librerías de analisis de datos, pandas
import pandas as pd

## PASO 2:
## Carga de datos a un dataframe
dataFrame = pd.read_csv("210310COVID19MEXICO.csv")

## Validar el tamaño del dataframe (filas x columnas)
print(dataFrame.shape)
## Muestra las N primeras filas del dataframe
print(dataFrame.head(10))

## Mostrar el nombre de todas las columnas en el dataframe
print(dataFrame.columns)

## PASO 3: Preparando la información del dataframe (limpieza del dataframe)
## ---------------
## Imprimir la información (nombres de columna y tipos de dato actual)
print(dataFrame.info())

## Cambiar los tipos de datos a mostrar (revisar diccionario de datos)
dataFrame=dataFrame.astype({'ID_REGISTRO': 'string', 'ENTIDAD_RES': 'string'})
## Campos identificados como fecha
dataFrame['FECHA_ACTUALIZACION'] = dataFrame['FECHA_ACTUALIZACION'].astype('datetime64[ns]')
dataFrame['FECHA_INGRESO'] = dataFrame['FECHA_INGRESO'].astype('datetime64[ns]')
dataFrame['FECHA_SINTOMAS'] = dataFrame['FECHA_SINTOMAS'].astype('datetime64[ns]')

## Eliminando columnas que no deseamos trabajar
dataFrame=dataFrame.drop(columns=['ID_REGISTRO','ORIGEN','SECTOR'])
print(dataFrame.info())

## Generando dataFrame con solo las columnas que necesitamos trabajar
dataFrame = dataFrame[['FECHA_ACTUALIZACION','EDAD', 'SEXO', 'ENTIDAD_RES', 'CLASIFICACION_FINAL']]
## Mostrar los datos del nuevo dataframe "recortado"
print(dataFrame.info())


## PASO 4: Analisis de datos en el dataframe
## Mostrar una muestra aleatoria de n registros del nuevo dataframe
sample_df = dataFrame.sample(15)
print(sample_df)

# Obteniendo la media del campo edad para todo el dataframe
print(dataFrame['EDAD'].mean())

# Obteniendo la media del campo edad para todo el dataframe agrupado por sexo
print(dataFrame.groupby('SEXO').mean())

# Obtener información de los valores únicos de una columna
print(dataFrame['CLASIFICACION_FINAL'].value_counts())


## Filtro por campo 'CLASIFICACION_FINAL'
filtros = ["CASO DE SARS-COV-2  CONFIRMADO", 
           "CASO DE COVID-19 CONFIRMADO POR ASOCIACION CLINICA EPIDEMIOLOGICA",
           "CASO DE COVID-19 CONFIRMADO POR COMITE DE  DICTAMINACION" ]
positivos_df = dataFrame[dataFrame["CLASIFICACION_FINAL"].isin(filtros)] 

# Obtener información de los valores únicos de la columna
print(dataFrame['CLASIFICACION_FINAL'].value_counts())

# Obteniendo los datos de casos positivos por entidad 
positivos_entidad_df = positivos_df['ENTIDAD_RES'].value_counts()
print(positivos_entidad_df)
positivos_entidad_df = positivos_entidad_df.rename_axis('ENTIDAD').to_frame('CASOS POSITIVOS COVID')
print(positivos_entidad_df)

## PASO 5: Analisis de datos en el dataframe
# Exportando el dataframe a un archivo CSV
positivos_entidad_df.to_csv('CASOS_CONFIRMADOS_COVID19_MEXICO.csv')

