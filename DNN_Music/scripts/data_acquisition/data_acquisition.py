import pandas as pd
import os
import pathlib
import requests
from io import StringIO



# URL de descarga directa
file_id = "1tX-fyFqHZ_28zdGB0Inx4VtZFyjup_1Y" 
download_url = f"https://drive.google.com/uc?id={file_id}"


def load_data_set():
    response = requests.get(download_url)
    if  response.status_code == 200:
        # Lee el contenido del CSV en memoria
        csv_content = StringIO(response.text)

        df = pd.read_csv(csv_content)


        df_dict = df.drop(columns=['filename', 'length'], errors='ignore')
        columns = df_dict.columns
        descriptions = {col: "Descripción no disponible aún" for col in columns}
        print("Data set cargado con exito  y diccionario de descripciones creado")
        descriptions.update({
                    'chroma_stft_mean': 'Promedio de la transformada de Fourier del cromatograma, relacionado con la tonalidad.',
                    'chroma_stft_var': 'Varianza de la transformada de Fourier del cromatograma, mide la dispersión tonal.',
                    'rms_mean': 'Promedio de la raíz cuadrada media del espectro de la señal, refleja su intensidad promedio.',
                    'rms_var': 'Varianza de la raíz cuadrada media, indica variabilidad en la intensidad.',
                    'spectral_centroid_mean': 'Promedio del centroide espectral, indica el "brillo" promedio del sonido.',
                    'spectral_centroid_var': 'Varianza del centroide espectral, mide la dispersión en el brillo del sonido.',
                    'spectral_bandwidth_mean': 'Promedio del ancho de banda espectral, mide la amplitud del rango de frecuencias.',
                    'spectral_bandwidth_var': 'Varianza del ancho de banda espectral, indica fluctuaciones en el rango de frecuencias.',
                    'rolloff_mean': 'Promedio de la frecuencia de rolloff, donde se concentra el 85% de la energía espectral.',
                    'rolloff_var': 'Varianza de la frecuencia de rolloff, refleja cambios en la distribución de energía espectral.',
                    'zero_crossing_rate_mean': 'Promedio de la tasa de cruces por cero, indica la frecuencia de cambios de signo en la señal.',
                    'zero_crossing_rate_var': 'Varianza de la tasa de cruces por cero, mide la variabilidad en los cambios de signo.',
                    'harmony_mean': 'Promedio de la armonía en la señal, refleja la tonalidad general.',
                    'harmony_var': 'Varianza de la armonía, mide la dispersión tonal.',
                    'perceptr_mean': 'Promedio de la perceptualidad, describe aspectos perceptivos del sonido.',
                    'perceptr_var': 'Varianza de la perceptualidad, mide la variabilidad en aspectos perceptivos.',
                    'tempo': 'Tempo estimado de la señal, en beats por minuto (bpm).',
                    'label': 'Etiqueta de clasificación del género musical.',
                    })


        for i in range(1, 21):
            descriptions[f'mfcc{i}_mean'] = f'Promedio del coeficiente cepstral en la frecuencia {i}, relacionado con la textura del sonido.'
            descriptions[f'mfcc{i}_var'] = f'Varianza del coeficiente cepstral en la frecuencia {i}, mide la variabilidad en la textura del sonido.'


        return df, descriptions
    else:
        print("Archivo no encontrado:")




if __name__ == "__main__":
    df, descriptions = load_data_set()
