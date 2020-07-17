# O(n²)
import copy
from .visualizer import Visualizer


def insertionSort(data):

    frames = [data]
    array = copy.deepcopy(data)
    n = Visualizer.sizeArrays

    for i in range(1, n):
        frames.append(copy.deepcopy(array))
        frames[-1][i].set_color('r')

        for j in range(i, 0, -1):
            if array[j].value < array[j - 1].value:
                array[j], array[j - 1] = array[j - 1], array[j]
                frames.append(copy.deepcopy(array))
                frames[-1][j-1].set_color('r')
            else:
                break
    frames.append(array)
    # print(array)
    return frames
