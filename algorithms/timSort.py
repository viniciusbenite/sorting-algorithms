# O(n log2 n) avg and worst case
# O(n) on best cases -> almost sorted arrays
from .insertionSort import insertionSort
from .mergeSort import merge


def timSort(array):

    arraySlice = 32

    # Divide the array into small portions
    for i in range(0, len(array), arraySlice):
        insertionSort(array, i, min((i + arraySlice - 1), len(array) - 1))

    # Merge the sorted slices
    # Start from arraySlice, doubling the size on
    # each iteration until you surpass the length of
    # the array.
    size = arraySlice
    while size < len(array):
        # Determine the arrays that will

        # be merged together

        for start in range(0, len(array), size * 2):
            # Compute the `midpoint` (where the first array ends
            # and the second starts) and the `endpoint` (where
            # the second array ends)
            midpoint = start + size - 1
            end = min((start + size * 2 - 1), (len(array) - 1))
            # Merge the two sub arrays.
            # The 'left' array should go from 'start' to
            # 'midpoint + 1', while the 'right' array should
            # go from 'midpoint + 1' to 'end + 1'.
            mergedArray = merge(
                leftArray=array[start:midpoint + 1],
                rightArray=array[midpoint + 1:end + 1])
            # Finally, put the merged array back into
            # your array
            array[start:start + len(mergedArray)] = mergedArray
        # Each iteration should double the size of your arrays
        size *= 2
    # print(array)
    return array
