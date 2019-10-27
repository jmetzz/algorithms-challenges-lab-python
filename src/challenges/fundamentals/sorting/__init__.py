def swap(a, i, j):
    """Swap two elements in a given array.

    The operation is performed in place,
    exchanging the elements in position i and j.

    Args:
        i: the index of the first element
        j: the index of the second element
    """
    temp = a[j]
    a[j] = a[i]
    a[i] = temp