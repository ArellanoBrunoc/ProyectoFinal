# Reporte del Modelo Baseline  

Este documento contiene los resultados del modelo baseline y su comparativa con un modelo adicional construido.  

---

## Descripción del modelo  
El modelo baseline es un **DNN (Deep Neural Network)** diseñado para la clasificación de géneros musicales utilizando características extraídas del audio, como transformadas espectrales, coeficientes cepstrales y otras variables relacionadas con el análisis de sonido.  

Un modelo adicional **KNN (K-Nearest Neighbors)** fue implementado para comparar su rendimiento con el baseline.  

---

## Variables de entrada  

Las variables de entrada incluyen:  
- `chroma_stft_mean`, `chroma_stft_var`  
- `rms_mean`, `rms_var`  
- `spectral_centroid_mean`, `spectral_centroid_var`  
- `spectral_bandwidth_mean`, `spectral_bandwidth_var`  
- `rolloff_mean`, `rolloff_var`  
- `zero_crossing_rate_mean`, `zero_crossing_rate_var`  
- `harmony_mean`, `harmony_var`  
- `perceptr_mean`, `perceptr_var`  
- `tempo`  
- `mfcc1_mean`, ..., `mfcc20_mean`  
- `mfcc1_var`, ..., `mfcc20_var`  

---

## Variable objetivo  

La variable objetivo es `label`, que representa el género musical asociado a cada muestra de audio.  

---

## Evaluación del modelo  

### Métricas de evaluación  

Para evaluar los modelos, se utilizaron las siguientes métricas:  
1. **Precisión (Accuracy)**: Porcentaje de predicciones correctas sobre el total de ejemplos.  
2. **Pérdida (Loss)**: Medida del error del modelo en la predicción de los datos de prueba.  

---

### Resultados de evaluación  

| Modelo | Pérdida en prueba | Precisión en prueba |  
|--------|-------------------|---------------------|  
| **DNN** (baseline) | 1.0824 | 93.42% |  
| **KNN** (adicional) | 1.5180 | 89.59% |  

---

## Análisis de los resultados  

El modelo baseline (DNN) demostró un mejor rendimiento en comparación con el modelo adicional (KNN):  
- **Fortalezas del DNN**:  
  - Alta precisión en las predicciones (93.42%).  
  - Capacidad para capturar relaciones no lineales en los datos.  
- **Debilidades del KNN**:  
  - Menor precisión en comparación con el DNN (89.59%).  
  - Sensible al ruido y al tamaño de los datos, lo que puede haber afectado su desempeño.  

---

## Conclusiones  

1. El modelo baseline **DNN** es el más adecuado para este proyecto, dado que mostró una mayor precisión y menor pérdida en comparación con el modelo adicional **KNN**.  
2. Los resultados respaldan la decisión inicial de utilizar un DNN como base para futuras iteraciones y mejoras.  
3. Áreas potenciales de mejora incluyen la optimización de hiperparámetros en el DNN y la incorporación de técnicas avanzadas de regularización para mejorar aún más su rendimiento.  

---

## Referencias  

1. [GTZAN Genre Classification Dataset](https://www.kaggle.com/code/imsparsh/gtzan-genre-classification-deep-learning-val-92-4/notebook#GTZAN---Deep-Learning).  
2. Documentación interna del proyecto, incluyendo los scripts.  .  
