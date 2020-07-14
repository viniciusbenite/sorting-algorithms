# O(n²)

import copy
from .visualizer import Visualizer

def bubbleSort(ds):

    frames = [ds]
    ds = copy.deepcopy(ds)

    n = Visualizer.totalArrays

    for i in range(n):
        # Flag to finish the algorithm and remove unnecessary iterations
        isSorted = True

        # Go through all elements of the array and compare with their
        # neighbour
        for j in range(n - i - 1):
            # if the actual value is bigger then the next ...
            if ds[j].value > ds[j + 1].value:
                ds[j], ds[j + 1] = ds[j + 1], ds[j]
            isSorted = False
            frames.append(copy.deepcopy(ds))
            frames[-1][j + 1].set_color('r')
        if isSorted:
            break
    frames.append(ds)
    # print(array)
    return frames
