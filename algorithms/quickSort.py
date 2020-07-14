from random import randint

# Best case (pivot close to median of the array): O(n)
# Worst case (pivot is the smallest or largest value): O(n²)
# Avg case: O(log2n)


def quickSort(array):
    # Check if the array length is smaller than 2
    if len(array) < 2:
        return array

    lowArray = []
    highArray = []
    finalArray = []

    # Select a pivot in the middle of the array
    # pivot = array[len(array) // 2]
    pivot = array[randint(0, len(array) - 1)]
    # Elements bigger than pivot go to highArray. Smaller ones go to
    # lowArray.
    for element in array:
        if element < pivot:
            lowArray.append(element)
        elif element > pivot:
            highArray.append(element)
        elif element == pivot:
            finalArray.append(element)
    # arr = quickSort(lowArray) + finalArray + quickSort(highArray)
    # print(pivot)
    # print(arr)
    # Use of recursion to combine the 3 arrays
    return quickSort(lowArray) + finalArray + quickSort(highArray)
