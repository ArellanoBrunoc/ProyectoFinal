import matplotlib.pyplot as plt
import seaborn as sns

def df_shape(df):
    snippets = df.shape
    print(f"\nEl dataset que vamos a utilizar tiene las dimensiones {snippets}.")
    df.info()

def memory_usage(df):
    # ¿Qué tamaño en MB tiene el conjunto de datos?
    megabytes_music = df.memory_usage(deep = True).sum() / (1024**2)
    print(f"Este dataset tiene un tamaño de {megabytes_music} MB.")

def data_type(df):
    # ¿En qué formato están guardados los datos?
    tipos_datos = df.dtypes.value_counts()
    print(f"Los tipos de datos en el dataframe son:\n\n{tipos_datos}.")

def missing_data(df):
    # ¿Hay datos faltantes?
    faltantes = df.isnull().sum()
    print(faltantes.sort_values(ascending=False))

def label_visualizer(df):
    etiquetas = df['label'].value_counts()
    plt.figure(figsize=(10,6))
    sns.barplot(x=etiquetas.index, y=etiquetas.values, palette='viridis', hue=etiquetas.index)
    plt.title('Distribución de géneros musicales')
    plt.xlabel('Género')
    plt.ylabel('Fragmentos')
    plt.xticks(rotation=45)
    plt.show()