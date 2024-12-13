import keras as k
import pandas as pd
import matplotlib.pyplot as plt





def plotHistory(history):
    print("Max. Validation Accuracy", max(history.history["val_accuracy"]))
    pd.DataFrame(history.history).plot(figsize=(12,6))
    plt.show()


def create_model(X_train , y_train, X_dev, y_dev):
    print("Creando modelo con forma de X_train:", X_train.shape)
    model = k.models.Sequential([
        k.layers.Dense(1024, activation='relu', input_shape=(X_train.shape[1],)),
        k.layers.Dropout(0.3),

        k.layers.Dense(512, activation='relu'),
        k.layers.Dropout(0.3),

        k.layers.Dense(256, activation='relu'),
        k.layers.Dropout(0.3),

        k.layers.Dense(128, activation='relu'),
        k.layers.Dropout(0.3),

        k.layers.Dense(64, activation='relu'),
        k.layers.Dropout(0.3),

        k.layers.Dense(10, activation='softmax'),
    ])
    
    # Verifica si el modelo fue creado correctamente
    print("Modelo creado exitosamente.")
    model.summary()  # Esto debería mostrar la arquitectura del modelo
    # Definimos el umbral de precisión
    ACCURACY_THRESHOLD = 0.94

    class myCallback(k.callbacks.Callback):
        def on_epoch_end(self, epoch, logs={}):
            if(logs.get('val_accuracy') > ACCURACY_THRESHOLD):
                print("\n\nSe detiene el entrenamiento pues se ha alcanzado un %2.2f%% de precisión!" %(ACCURACY_THRESHOLD*100))
                self.model.stop_training = True
    
    def trainModel(model, epochs, optimizer, X_train, y_train, X_dev, y_dev):
        batch_size = 128
        callback = myCallback()
        model.compile(optimizer=optimizer,
                  loss='sparse_categorical_crossentropy',
                  metrics=['accuracy'])
        return model.fit(X_train, y_train, validation_data=(X_dev, y_dev), epochs=epochs,
                     batch_size=batch_size, callbacks=[callback])
    
    model_history = trainModel(model=model, epochs=500, optimizer='rmsprop', X_train=X_train, y_train=y_train, X_dev=X_dev, y_dev=y_dev)

    return model_history, model

