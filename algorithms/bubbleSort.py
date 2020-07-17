# O(n²)

import copy
from .visualizer import Visualizer


def bubbleSort(data):

    frames = [data]
    data = copy.deepcopy(data)

    n = Visualizer.sizeArrays

    for i in range(n):
        # Flag to finish the algorithm and remove unnecessary iterations
        isSorted = True

        # Go through all elements of the array and compare with their
        # neighbour
        for j in range(n - i - 1):
            # if the actual value is bigger then the next ...
            if data[j].value > data[j + 1].value:
                data[j], data[j + 1] = data[j + 1], data[j]
            isSorted = False
            frames.append(copy.deepcopy(data))
            frames[-1][j + 1].set_color('r')
        if isSorted:
            break
    frames.append(data)
    # print(array)
    return frames
