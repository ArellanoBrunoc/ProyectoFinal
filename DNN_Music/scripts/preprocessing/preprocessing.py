import pandas as pd
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split as skms
from sklearn.preprocessing import StandardScaler as skp

def clean_df(df, seed=42):
    # Eliminamos las columnas innecesarias
    df_clean = df.drop(['filename', 'length'], axis=1, errors='ignore')
    
    # Convertimos las etiquetas en valores numéricos
    label_encoder = LabelEncoder()
    df_clean['label_encoded'] = label_encoder.fit_transform(df['label'])
    
    # Realizamos mezcla aleatoria
    df_clean['index_original'] = df_clean.index
    df_shuffle = df_clean.sample(frac=1, random_state=seed).reset_index(drop=True)

    # Creamos las particiones de entrenamiento, validación y prueba
    df_X = df_shuffle
    df_y = df_shuffle.pop('label_encoded')
    df_z = df_shuffle.pop('label')
    df_i = df_shuffle.pop('index_original')

    # Dividimos en entrenamiento, validación y prueba
    X_train, df_test_valid_X, y_train, df_test_valid_y = skms(df_X, df_y, train_size=0.7, random_state=seed, stratify=df_y)
    X_dev, X_test, y_dev, y_test = skms(df_test_valid_X, df_test_valid_y, train_size=0.66, random_state=seed, stratify=df_test_valid_y)

    print(f"El conjunto de entrenamiento tiene {X_train.shape[0]} registros de un total de {len(df)}, lo cual representa el {round(X_train.shape[0] / len(df) * 100)}%")
    print(f"El conjunto de validación tiene {X_dev.shape[0]} registros de un total de {len(df)}, lo cual representa el {round(X_dev.shape[0] / len(df) * 100)}%")
    print(f"El conjunto de prueba tiene {X_test.shape[0]} registros de un total de {len(df)}, lo cual representa el {round(X_test.shape[0] / len(df) * 100)}%")

    # **Escalamos las particiones**
    scaler = skp()
    X_train = pd.DataFrame(scaler.fit_transform(X_train), columns=X_train.columns)
    X_dev = pd.DataFrame(scaler.transform(X_dev), columns=X_train.columns)
    X_test = pd.DataFrame(scaler.transform(X_test), columns=X_train.columns)
    
    return X_train, X_dev, X_test, y_train, y_dev, y_test, df_clean
