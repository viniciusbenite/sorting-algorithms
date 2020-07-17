# Divide and conquer algorithm
import copy
from .visualizer import Visualizer


# O(n)
def merge(array, left, right, frames):
    middle = (left + right) // 2

    if right - left > 2:
        merge(array, left, middle, frames)
        merge(array, middle, right, frames)

    arrayColor = copy.deepcopy(array)

    for i in range(left, middle):
        arrayColor[i].set_color('y')
    for i in range(middle, right):
        arrayColor[i].set_color('b')

    l = left
    r = middle
    tempArray = []

    for i in range(left, right):
        frames.append(copy.deepcopy(arrayColor))
        if r == right or (l < middle and array[l].value <= array[r].value):
            tempArray.append(array[l])
            frames[-1][l].set_color('r')
            l = l + 1
        else:
            tempArray.append(array[r])
            frames[-1][r].set_color('r')
            r = r + 1
    for i in range(left, right):
        array[i] = tempArray[i - left]
    frames.append(copy.deepcopy(array))


#  O(nlog2n)
def mergeSort(data):
    frames = [data]
    array = copy.deepcopy(data)
    merge(array, 0, Visualizer.sizeArrays, frames)
    frames.append(array)
    return frames
