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

from sklearn.neighbors import KNeighborsClassifier
from sklearn.preprocessing import StandardScaler, LabelEncoder
from sklearn.metrics import classification_report, confusion_matrix, accuracy_score, log_loss
from sklearn.model_selection import train_test_split
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt


def KNN_model(df):
    # Codificamos las etiquetas
    class_encod = df.iloc[:, -1]
    converter = LabelEncoder()
    y = converter.fit_transform(class_encod)

    # Eliminamos columnas no relevantes
    df = df.drop(['filename', 'length'], axis=1)

    # Ajustamos y transformamos los datos
    fit = StandardScaler()
    X = fit.fit_transform(np.array(df.iloc[:, :-1], dtype=float))
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

    # Entrenamos el modelo
    clf1 = KNeighborsClassifier(n_neighbors=3)
    clf1.fit(X_train, y_train)
    y_pred = clf1.predict(X_test)
    y_proba = clf1.predict_proba(X_test)  # Probabilidades necesarias para log_loss

    # Calcular accuracy
    accuracy = accuracy_score(y_test, y_pred)

    # Calcular log-loss
    loss = log_loss(y_test, y_proba)

    # Visualizamos resultados y evaluamos el modelo
    print("Training set score: {:.3f}".format(clf1.score(X_train, y_train)))
    print("Test set score: {:.3f}".format(accuracy))
    print(f"Log-loss en el conjunto de prueba: {loss:.3f}")
    print(f"Mejor precisión en la prueba: {accuracy * 100:.2f}%")

    # Confusión y reporte de clasificación
    cf_matrix = confusion_matrix(y_test, y_pred)
    sns.set(rc={'figure.figsize': (8, 3)})
    sns.heatmap(cf_matrix, annot=True, cmap='Blues', fmt='g')
    plt.show()
    print(classification_report(y_test, y_pred))

    return clf1, accuracy, loss


