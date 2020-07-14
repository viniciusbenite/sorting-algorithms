from random import randint
from timeit import repeat


def runAlgorithm(algorithm, array_to_sort):
    # Set up the context and prepare the call to the specified
    # algorithm using the supplied array. Only import the
    # algorithm function if it's not the built-in `sorted()`.

    # Magic of Python's f-strings
    setup = f"from algorithms.{algorithm} import {algorithm}" \
        if algorithm != "sorted" else ""

    # Calls the algorithm with the array to sort
    stmt = f"{algorithm}({array_to_sort})"

    # Execute the code ten different times and return the time
    # in seconds that each execution took
    times = repeat(setup=setup, stmt=stmt, repeat=3, number=10)

    # Finally, display the name of the algorithm and the
    # minimum time it to
    print(f"Algorithm: {algorithm}. Minimum execution time: {min(times)}.")


ARRAY_LENGTH = 10000


if __name__ == "__main__":
    # Generate an array of `ARRAY_LENGTH` items consisting
    # of random integer values between 0 and 999
    array = [randint(0, 1000) for i in range(ARRAY_LENGTH)]
    # Call the function using the name of the sorting algorithm
    # and the array you just created
    runAlgorithm(algorithm="sorted", array_to_sort=array)
    # runAlgorithm(algorithm="bubbleSort", array_to_sort=array)
    # runAlgorithm(algorithm="insertionSort", array_to_sort=array)
    runAlgorithm(algorithm="mergeSort", array_to_sort=array)
    runAlgorithm(algorithm="quickSort", array_to_sort=array)

