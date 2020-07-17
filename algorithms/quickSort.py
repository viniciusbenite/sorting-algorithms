from random import randint

# Best case (pivot close to median of the array): O(n)
# Worst case (pivot is the smallest or largest value): O(n²)
# Avg case: O(log2n)

import copy
from .visualizer import Visualizer


def quickSort(data):
    frames = [data]
    array = copy.deepcopy(data)
    qSort(data, 0, Visualizer.sizeArrays, frames)
    frames.append(array)
    return frames


def qSort(data, left, right, frames):
    if right - left > 1:
        arrayColor = copy.deepcopy(data)
        for i in range(left, right):
            arrayColor[i].set_color('y')
        l = left
        r = right - 1
        pivot = data[r].value
        while l < r:
            frames.append(copy.deepcopy(arrayColor))
            frames[-1][l if data[l].value == pivot else r].set_color('r')
            frames[-1][r if data[l].value == pivot else l].set_color('k')
            if data[l].value > pivot or data[r].value < pivot:
                data[l], data[r] = data[r], data[l]
                arrayColor[l], arrayColor[r] = arrayColor[r], arrayColor[l]
                frames.append(copy.deepcopy(arrayColor))
                frames[-1][l if data[l].value == pivot else r].set_color('r')
                frames[-1][r if data[l].value == pivot else l].set_color('k')
            if data[l].value == pivot:
                r = r - 1
            else:
                l = l + 1

        qSort(data, left, l, frames)
        qSort(data, l + 1, right, frames)


