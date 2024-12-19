# Despliegue de modelos

## Infraestructura

- **Nombre del modelo:** DNN_Music
- **Plataforma de despliegue:** Hugging Face Spaces
- **Requisitos técnicos:**:
    * Python 3.8+
    Bibliotecas de terceros:
    - gradio (para la interfaz de usuario)
    - keras (para cargar el modelo DNN)
    - numpy (para manejar datos de entrada)
    - joblib
    Hardware:
    Proporcionado por la nube
    Dependencias adicionales:
    - tensorflow.
- **Requisitos de seguridad:** 
    * Autenticación: La plataforma de Hugging Face requiere autenticación para crear espacios. Se debe generar un token de autenticación desde Hugging Face.
    * Encriptación de datos: La encriptación se maneja automáticamente durante el transporte en Hugging Face.
- **Diagrama de arquitectura:**:




## Código de despliegue

- **Archivo principal:** App_deploy/app.py
- **Rutas de acceso a los archivos:**:
    *App_deploy/app.py
    *App_deploy/DNN_v1.h5
    *App_deploy/scaler.pkl
- **Variables de entorno:** Ninguna

## Documentación del despliegue

- **Instrucciones de instalación:** 
    * Crear cuenta en HugginFace [text](https://huggingface.co)
    * Crear un espacio nuevo en Gradio como inmterfaz
    * crear una carpeta local con los archivos necesarios y generar un clon:
    ```bash
    git clone https://huggingface.co/spaces/GithubUser/SpaceName
    ```
    * Commit y pushear todos los archivos (esto pedira un Token de autenticacion de HugginFace con permisos de escritura)
    ```bash
    git add .
    git commit -m "Add application file"
    git push
    ```
- **Instrucciones de configuración:** No requiere mayores configuraciones
- **Instrucciones de uso:** 
    * Copiar los datos de entrada deseados en el orden establecido y pegarlos en la interfaz y usar "submit" para obtener una prediccion.
    * Importar Client de Gradio, para hacer llamadas por API
- **Instrucciones de mantenimiento:** No requiere mantenimiento
