def maxsubarray(array):  # Поменяли nums на array
    maxsum = array[0]
    currentsum = array[0]

    for num in array[1:]:
        currentsum = max(num, currentsum + num)
        maxsum = max(maxsum, currentsum)

    return maxsum


array = [-5, 2, -3, 6, -2, 3, 1, -7, 3]
print(maxsubarray(array))
