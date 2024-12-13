"""
# Diccionario de datos

## Base de datos musicdataset.csv

**Datos de musicdataset.csv que contienen información espectral de cada fragmento de pista de audio.**

| Variable               | Descripción                                                                                           | Tipo de dato | Rango/Valores posibles          | Fuente de datos    | Rango estimado                              |
|------------------------|-------------------------------------------------------------------------------------------------------|--------------|----------------------------------|--------------------|---------------------------------------------|
| chroma_stft_mean       | Promedio de la transformada de Fourier del cromatograma, relacionado con la tonalidad.               | Numérico     | Valores reales.                 | musicdataset.csv   | [0.0, 1.0]                                 |
| chroma_stft_var        | Varianza de la transformada de Fourier del cromatograma, mide la dispersión tonal.                   | Numérico     | Valores reales.                 | musicdataset.csv   | [0.0, 0.1]                                 |
| rms_mean               | Promedio de la raíz cuadrada media del espectro de la señal, refleja su intensidad promedio.         | Numérico     | Valores reales.                 | musicdataset.csv   | [0.0, 1.0]                                 |
| rms_var                | Varianza de la raíz cuadrada media, indica variabilidad en la intensidad.                            | Numérico     | Valores reales.                 | musicdataset.csv   | [0.0, 0.1]                                 |
| spectral_centroid_mean | Promedio del centroide espectral, indica el "brillo" promedio del sonido.                            | Numérico     | Valores reales.                 | musicdataset.csv   | [0.0, 8000.0]                              |
| spectral_centroid_var  | Varianza del centroide espectral, mide la dispersión en el brillo del sonido.                        | Numérico     | Valores reales.                 | musicdataset.csv   | [0.0, 1000000.0]                           |
| spectral_bandwidth_mean| Promedio del ancho de banda espectral, mide la amplitud del rango de frecuencias.                    | Numérico     | Valores reales.                 | musicdataset.csv   | [0.0, 4000.0]                              |
| spectral_bandwidth_var | Varianza del ancho de banda espectral, indica fluctuaciones en el rango de frecuencias.              | Numérico     | Valores reales.                 | musicdataset.csv   | [0.0, 1000000.0]                           |
| rolloff_mean           | Promedio de la frecuencia de rolloff, donde se concentra el 85% de la energía espectral.            | Numérico     | Valores reales.                 | musicdataset.csv   | [0.0, 8000.0]                              |
| rolloff_var            | Varianza de la frecuencia de rolloff, refleja cambios en la distribución de energía espectral.       | Numérico     | Valores reales.                 | musicdataset.csv   | [0.0, 1000000.0]                           |
| zero_crossing_rate_mean| Promedio de la tasa de cruces por cero, indica la frecuencia de cambios de signo en la señal.        | Numérico     | Valores reales.                 | musicdataset.csv   | [0.0, 1.0]                                 |
| zero_crossing_rate_var | Varianza de la tasa de cruces por cero, mide la variabilidad en los cambios de signo.                | Numérico     | Valores reales.                 | musicdataset.csv   | [0.0, 0.1]                                 |
| harmony_mean           | Promedio de la armonía en la señal, refleja la tonalidad general.                                    | Numérico     | Valores reales.                 | musicdataset.csv   | [0.0, 1.0]                                 |
| harmony_var            | Varianza de la armonía, mide la dispersión tonal.                                                   | Numérico     | Valores reales.                 | musicdataset.csv   | [0.0, 0.1]                                 |
| perceptr_mean          | Promedio de la perceptualidad, describe aspectos perceptivos del sonido.                            | Numérico     | Valores reales.                 | musicdataset.csv   | [0.0, 1.0]                                 |
| perceptr_var           | Varianza de la perceptualidad, mide la variabilidad en aspectos perceptivos.                        | Numérico     | Valores reales.                 | musicdataset.csv   | [0.0, 0.1]                                 |
| tempo                  | Tempo estimado de la señal, en beats por minuto (bpm).                                              | Numérico     | Valores reales (típico: 0-300). | musicdataset.csv   | [0.0, 300.0]                               |
| mfccX_mean             | Promedio del coeficiente cepstral en la frecuencia X, relacionado con la textura del sonido.        | Numérico     | Valores reales.                 | musicdataset.csv   | [-50.0, 50.0]                              |
| mfccX_var              | Varianza del coeficiente cepstral en la frecuencia X, mide la variabilidad en la textura del sonido. | Numérico     | Valores reales.                 | musicdataset.csv   | [0.0, 100.0]                              |
| label                  | Etiqueta de clasificación del género musical.                                                      | Categórico   | Nombres de géneros musicales.   | musicdataset.csv   | Nombres de géneros musicales específicos. |
"""
