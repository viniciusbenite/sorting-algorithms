# O(n²)

def bubbleSort(array):
    n = len(array)

    for i in range(n):
        # Flag to finish the algorithm and remove unecessary iterations
        isSorted = True

        # Go through all elements of the array and compare with their
        # neighbour
        for j in range(n - i - 1):
            # if the actual value is bigger then the next ...
            if array[j] > array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]
            isSorted = False

        if isSorted:
            break
    # print(array)
    return array
