# Divide and conquer algorithm


# O(n)
def merge(leftArray, rightArray):
    # Check if the one of the arrays is empty -> return the second array
    if len(leftArray) == 0:
        return rightArray

    if len(rightArray) == 0:
        return leftArray

    finalArray = []
    indexLeft = 0
    indexRight = 0

    # Iterate over the arrays until the final array is bigger
    while len(finalArray) < len(leftArray) + len(rightArray):
        # Compare the elements of both arrays and insert the
        # smaller one into the final array
        if leftArray[indexLeft] <= rightArray[indexRight]:
            finalArray.append(leftArray[indexLeft])
            indexLeft = indexLeft + 1
        else:
            finalArray.append(rightArray[indexRight])
            indexRight = indexRight + 1
        # If the one of the both array ends
        if indexRight == len(rightArray):
            # Add the remaining of the array and stop
            finalArray += leftArray[indexLeft:]
            break
        if indexLeft == len(leftArray):
            finalArray += rightArray[indexRight:]
            break
    # print(finalArray)
    return finalArray


#  O(nlog2n)
def mergeSort(array):
    if len(array) < 2:
        return array
    midPoint = len(array) // 2

    # Use of recursion to split the input into two equals halfs
    # and merge them to final result
    return merge(leftArray=mergeSort(array=array[:midPoint]),
                 rightArray=mergeSort(array=array[midPoint:]))
