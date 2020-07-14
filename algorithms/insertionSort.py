# O(n²)

def insertionSort(array):
    for i in range(1, len(array)):
        # Select the element we want to shift. Starts on the
        # second element of the array.
        element = array[i]
        j = i - 1

        # Run through the array from right to left
        # If element is smaller than its neighbour, shift
        while j >= 0 and array[j] > element:
            # j will point to the next element
            array[j + 1] = array[j]
            j = j - 1
        array[j + 1] = element
    # print(array)
    return array
