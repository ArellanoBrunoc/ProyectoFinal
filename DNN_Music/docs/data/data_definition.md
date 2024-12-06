# Definición de los datos

## Origen de los datos

Los datos fueron obtenidos de la plataforma Kaggle:  
[GTZAN Genre Classification](https://www.kaggle.com/code/imsparsh/gtzan-genre-classification-deep-learning-val-92-4/notebook#GTZAN---Deep-Learning)

## Especificación de los scripts para la carga de datos

El script utilizado para la carga de los datos es:  
`../../scripts/data_acquisition/main.py`

Este script verifica la existencia del archivo CSV `musicdataset.csv`, ubicado en la carpeta de datos correspondiente, y lo carga utilizando la biblioteca **pandas**. Además, prepara un diccionario de descripciones para las columnas relevantes.

## Referencias a rutas o bases de datos origen y destino

### Rutas de origen de datos

1. Archivo CSV de datos de Kaggle:  
   [musicdataset.csv](https://www.kaggle.com/code/imsparsh/gtzan-genre-classification-deep-learning-val-92-4/notebook#GTZAN---Deep-Learning)

2. Ubicación local del archivo:  
   `DNN_Music/docs/data/musicdataset.csv`

#### Estructura de los archivos de origen

El archivo `musicdataset.csv` contiene las siguientes columnas:  

- **filename**: Nombre del archivo de audio.  
- **length**: Longitud del archivo de audio en segundos.  
- **chroma_stft_mean/var**: Promedio y varianza del cromatograma transformado.  
- **rms_mean/var**: Promedio y varianza de la raíz cuadrada media del espectro.  
- **spectral_centroid_mean/var**: Brillo promedio y su dispersión.  
- **spectral_bandwidth_mean/var**: Promedio y varianza del ancho de banda espectral.  
- **rolloff_mean/var**: Promedio y varianza de la frecuencia de rolloff.  
- **zero_crossing_rate_mean/var**: Promedio y varianza de cruces por cero.  
- **harmony_mean/var**: Promedio y varianza de la armonía tonal.  
- **perceptr_mean/var**: Promedio y varianza de la perceptualidad del sonido.  
- **tempo**: Tempo en beats por minuto (bpm).  
- **label**: Género musical.  

Adicionalmente, contiene 20 columnas de coeficientes cepstrales (mfcc) con sus promedios y varianzas:  
`mfcc1_mean`, `mfcc1_var`, ..., `mfcc20_mean`, `mfcc20_var`.

#### Procedimientos de transformación y limpieza de los datos

En el script `main.py`, se realiza una limpieza básica de los datos:  
- Se eliminan las columnas irrelevantes como `filename` y `length`.  
- Se genera un diccionario de descripciones para cada columna del conjunto de datos, facilitando su interpretación.  

### Base de datos de destino

#### Base de datos de destino para los datos

El conjunto de datos procesados será utilizado directamente en el modelo, sin cargarlo a una base de datos específica, pero podría integrarse en sistemas de almacenamiento más complejos según la necesidad del despliegue.

#### Estructura de la base de datos de destino

En este proyecto, los datos transformados se mantienen en un **DataFrame de pandas**, cuya estructura incluye todas las columnas relevantes descritas anteriormente, excepto las que fueron eliminadas en el preprocesamiento.  

#### Procedimientos de carga y transformación de los datos en la base de datos de destino

El procedimiento de transformación incluye:  
1. Carga del archivo CSV utilizando **pandas**.  
2. Eliminación de columnas innecesarias (`filename`, `length`).  
3. Creación de un diccionario de descripciones para cada columna.  
4. Preparación del conjunto de datos para su uso directo en el pipeline del modelo de Machine Learning.

