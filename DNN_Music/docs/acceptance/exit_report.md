# Informe de salida

## Resultados del proyecto

El objetivo principal del proyecto fue desarrollar un modelo capaz de clasificar géneros musicales a partir de diferentes características extraídas de archivos de audio, utilizando redes neuronales. A lo largo del proceso, se aplicaron diversas técnicas de procesamiento de datos, selección de características y optimización de modelos.

El modelo final alcanzó una precisión del 93%, lo que indica un desempeño muy bueno y una alta capacidad para generalizar a nuevos datos. Este resultado sugiere que el modelo ha aprendido las características relevantes de los géneros musicales de manera efectiva. Por otro lado, el 7% de los casos que fueron clasificados incorrectamente podría atribuirse a factores como la similitud entre algunos géneros o posibles limitaciones en la calidad de los datos de entrada.

## Lecciones aprendidas

A lo largo del desarrollo del proyecto, se aprendieron varias lecciones importantes:

1. Importancia del preprocesamiento: La normalización de las características y la adecuada limpieza de los datos fueron pasos cruciales para asegurar que el modelo pudiera aprender de manera efectiva.
2. Optimización de hiperparámetros: Ajustar los hiperparámetros, como el número de capas y las unidades en cada capa, tuvo un impacto significativo en el rendimiento del modelo.
3. Importancia del balanceo de los datos: Gracias a que no tuvimos desbalanceo de datos, cada uno de lo géneros pudo representarse de manera variada en el conjunto de entrenamiento y prueba, permitiendo así al modelo aprender de los diferentes ritmos musicales.

Asimismo, aunque el desempeño del modelo es alto, existen varias formas de mejorar el modelo:

1. Ajuste de la arquitectura: Experimentar con arquitecturas más complejas, como redes neuronales convolucionales (CNN), podría mejorar la capacidad del modelo para captar características espaciales en los datos de audio.
2. Aumento de datos: Implementar nuevas muestras de audio podría ayudar a mejorar la robustez del modelo.


## Impacto del proyecto

Este proyecto tiene un impacto significativo en diversas áreas de la industria musical, tanto en areas de innovación como de organización, pues este modelo puede integrarse en plataformas de streaming de música (como Spotify, Apple Music, Tidal etc.) para ofrecer recomendaciones más precisas y personalizadas a los usuarios. Del mismo modo, juega un rol fundamental parar curar listas de reproducción, ya que al identificar de manera efectiva el género de una canción, el sistema puede sugerir otras canciones dentro del mismo género o incluso explorar géneros similares que el usuario podría disfrutar. Por otro lado, nuestro modelo también puede usarse como una herramienta para la organización de bibliotecas musicales, ya que se podría etiquetar y organizar grandes colecciones de audio de manera automatizada.

Finalmente, para mejorar el desempeño del modelo y su aplicación en la industria se podría incrementar las muestras de audio para la clasificación de subgéneros, pues el modelo clasifica bien los géneros principales (Rock, Rap, Pop), pero los mismos géneros pueden dividirse en subgéneros con características aún más específicas (rock alternativo vs. rock clásico, o pop punk vs pop latino). Ampliar el modelo para detectar subgéneros permitiría una mayor precisión en la categorización y enriquecería la experiencia del usuario.

## Conclusiones

Este proyecto ha sido un éxito en términos de la implementación de un modelo de clasificación de géneros musicales con una precisión del 93%. A través de un proceso iterativo de preprocesamiento, entrenamiento y evaluación, se logró desarrollar un modelo robusto que puede ser utilizado en aplicaciones prácticas en el ámbito de la música digital. Sin embargo, aún existen áreas de mejora que podrían incrementar aún más el rendimiento del modelo, como la exploración de arquitecturas más avanzadas y la ampliación de los datos.

## Agradecimientos

- Agradecimientos a todo el equipo de trabajo y profesores que permitieron la realización correcta de este proyecto.
