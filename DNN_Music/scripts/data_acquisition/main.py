import pandas as pd
import os
import pathlib

# Verificar ruta actual
print(f"Ruta actual: {os.getcwd()}")

csv_path = pathlib.Path(__file__).resolve().parents[3] / 'DNN_Music' / 'docs' / 'data' / 'musicdataset.csv'

def load_data_set(path) -> pd.DataFrame:
    if csv_path.exists():
        df = pd.read_csv(filepath_or_buffer=csv_path)
        print("Data set cargado con exito")
        
        return df
    else:
        print("Archivo no encontrado:", csv_path)


df = load_data_set(csv_path)