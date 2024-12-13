# Importamos librerias
import pandas as pd
import numpy as np 
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
import tensorflow as tf
from sklearn.neighbors import KNeighborsClassifier
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import classification_report, confusion_matrix
import matplotlib.pyplot as plt
import seaborn as sns


def KNN_model(df):
    # Codificamos las etiquetas
    class_encod = df.iloc[:,-1]
    converter = LabelEncoder()
    y = converter.fit_transform(class_encod)

    # Eliminamos columnas no relevantes
    df = df.drop(['filename', 'length'], axis=1)

    # Ajustamos y transformamos los datos
    fit = StandardScaler()
    X = fit.fit_transform(np.array(df.iloc[:,:-1], dtype=float))
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3)

    # Entrenamos el modelo
    clf1 = KNeighborsClassifier(n_neighbors=3)
    clf1.fit(X_train, y_train)
    y_pred = clf1.predict(X_test)

    # Visualizamos resultados y evaluamos el modelo
    print("Training set score: {:.3f}".format(clf1.score(X_train, y_train)))
    print("Test set score: {:.3f}".format(clf1.score(X_test, y_test)))

    # Imprimir el mejor resultado de precisión
    best_accuracy = clf1.score(X_test, y_test) * 100  # Se convierte a porcentaje
    print(f"Mejor precisión en la prueba: {best_accuracy:.2f}%")

    # Confusión y reporte de clasificación
    cf_matrix = confusion_matrix(y_test, y_pred)
    sns.set(rc={'figure.figsize':(8,3)})
    sns.heatmap(cf_matrix, annot=True)
    print(classification_report(y_test, y_pred))

