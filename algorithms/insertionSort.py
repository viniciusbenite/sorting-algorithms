# O(n²)


def insertionSort(array, left=0, right=None):
    if right is None:
        right = len(array) - 1

    # Loop from array[left] to array right[right]
    for i in range(left + 1, right + 1):
        # Select the element we want to shift
        element = array[i]
        j = i - 1

        # Run through the array from right to left
        # If element is smaller than its neighbour, shift
        while j >= left and array[j] > element:
            # j will point to the next element
            array[j + 1] = array[j]
            j = j - 1
        array[j + 1] = element
    # print(array)
    return array
