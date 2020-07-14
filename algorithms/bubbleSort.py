def bubbleSort(array):
    n = len(array)

    for i in range(n):
        # Flag para terminar o programa: remove passos desnecessários
        isSorted = True

        # Percorrer os elementos do array um a um e comparar
        # com os vizinho
        for j in range(n - i - 1):
            # Se o valor atual for maior ...
            if array[j] > array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]

            isSorted = False

        if isSorted:
            break

    return array
