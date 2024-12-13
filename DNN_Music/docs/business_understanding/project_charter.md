# Project Charter - Entendimiento del Negocio

## Nombre del Proyecto

Redes neuronales en la clasificación de géneros musicales.

## Objetivo del Proyecto

Desde tiempos inmemoriales, la música ha sido un elemento central en las culturas humanas, actuando como un medio de comunicación, expresión emocional y cohesión social. Compuesta por sonidos organizados en patrones de ritmo, melodía y armonía, la música se ha consolidado como un pilar fundamental en la expresión artística.

El objetivo de este proyecto es desarrollar y optimizar un modelo basado en redes neuronales capaz de aprender patrones y características acústicas inherentes a cada género musical. Esta iniciativa tiene aplicaciones directas en la industria del entretenimiento y la música, ofreciendo utilidad para plataformas de streaming en la curaduría de listas de reproducción y recomendaciones personalizadas, así como para individuos que deseen gestionar amplias bibliotecas de audio de manera más eficiente.

## Alcance del Proyecto

El desarrollo de este proyecto comenzará con la recopilación y análisis de metadatos musicales clave, como el corte espectral, el centroide espectral, la armonía y la tasa de cruce por cero, entre otros. Estas características permitirán identificar aspectos cruciales como la presencia de ruido o sonidos agudos, la disonancia, la tonalidad y la profundidad de los sonidos.

Posteriormente, se emplearán técnicas avanzadas de preprocesamiento de audio y aprendizaje profundo para construir un modelo capaz de clasificar géneros musicales de manera automatizada a partir de las características acústicas de las canciones. Finalmente, el modelo será evaluado y optimizado para garantizar una alta calidad en sus predicciones.

El éxito del proyecto se medirá por la confiabilidad del modelo al categorizar correctamente fragmentos de audio dentro de sus respectivos géneros musicales.


## Metodología
Para llevar a cabo este proyecto, se utilizará un conjunto de datos extraído de la plataforma Kaggle, que contiene fragmentos de audio pertenecientes a diversos géneros musicales. En primer lugar, se realizará una limpieza y preprocesamiento de los datos, seguido de un análisis exploratorio para identificar patrones relevantes.

El entrenamiento del modelo se llevará a cabo utilizando redes neuronales densas, empleando herramientas como TensorFlow, Keras y Scikit-learn para el desarrollo, ajuste y evaluación del modelo. La metodología asegurará la implementación de mejores prácticas en aprendizaje profundo y procesamiento de audio, garantizando la solidez y confiabilidad de los resultados.

Para este proyecto, no se considerará necesario el uso de versionamiento de datos (DVC), dado que los datos no cambian a lo largo del desarrollo y no requieren un control de versiones detallado.

## Contexto Adicional
En 2002, G. Tzanetakis y P. Cook presentaron su conocido artículo sobre clasificación de géneros musicales, titulado "Musical genre classification of audio signals", publicado en IEEE Transactions on Audio and Speech Processing.

Para la clasificación de géneros musicales en este proyecto, se utilizará el GTZAN Genre Dataset, que representa un total de 1000 pistas de audio con una duración de 30 segundos. Este conjunto de datos está dividido en 10 géneros, cada uno con 100 pistas. Todas las pistas están en formato de archivo .wav, con una frecuencia de muestreo de 22050Hz, en mono y 16 bits. Este dataset es ampliamente utilizado en investigaciones de clasificación de géneros musicales y sirve como base para entrenar y evaluar el modelo de redes neuronales en este proyecto.

## Cronograma

| Etapa | Duración Estimada | Fechas |
|------|---------|-------|
| Entendimiento del negocio y carga de datos | 1 semana | del 21 de noviembre al 28 de noviembre |
| Preprocesamiento, análisis exploratorio | 1 semana |  del 28 de noviembre al 4 de diciembre |
| Modelamiento y extracción de características | 1 semana | del 4 de diciembre al 11 de diciembre |
| Despliegue | 1 semana | del 11 de diciembre al 18 de diciembre |
| Evaluación y entrega final | 1 semana | del 18 de diciembre al 25 de diciembre |


## Equipo del Proyecto

- Bruno Cataño Arellano
- Andrey Camilo Ruiz Perez
- Lucia Castellanos Castillo
