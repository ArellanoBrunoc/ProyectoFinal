# Imprimir los resultados y compararlos
def print_comparison(dnn_test_loss, dnn_test_acc, knn_test_loss, knn_test_acc):
    print("Resultados del DNN:")
    print(f"Pérdida en prueba: {dnn_test_loss}, Precisión en prueba: {dnn_test_acc * 100}%")
    print("\nResultados del KNN:")
    print(f"Pérdida en prueba: {knn_test_loss}, Precisión en prueba: {knn_test_acc * 100}%")
    
    print("\nComparativa:")
    if dnn_test_acc > knn_test_acc:
        print("El DNN tiene mejor precisión en la prueba.")
    elif dnn_test_acc < knn_test_acc:
        print("El KNN tiene mejor precisión en la prueba.")
    else:
        print("Ambos modelos tienen la misma precisión en la prueba.")
