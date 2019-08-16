def partition(array, low, high):
    """
    partition the array so that left partition is always smaller than pivot and right partition is greater than pivot
    :param array: a list of unsorted integers
    :param low: starting index of list
    :param high: end index of list
    :return: the index of the pivot after partitioning
    """
    # use the last element as a pivot
    pivot = array[high]
    i = low
    for j in range(low, high):
        if array[j] < pivot:
            array[i], array[j] = array[j], array[i]
            i += 1
    array[i], array[high] = array[high], array[i]
    return i


def quick_sort(array, low, high):
    """
    implement quick sort function
    :param array: a list of unsorted integers
    :param low: starting index of list
    :param high: starting index of list
    :return: sort the integers in place in O(nlog(n)) time
    """
    if low < high:
        pi = partition(array, low, high)
        quick_sort(array, low, pi - 1)
        quick_sort(array, pi + 1, high)


def main():
    array = [1, 8, 2, 4, 7]
    quick_sort(array, 0, len(array) - 1)
    assert array == [1, 2, 4, 7, 8]

    array = [2148, 9058, 7742, 3153, 6324, 609, 7628, 5469, 7017, 504]
    quick_sort(array, 0, len(array) - 1)
    print(array)


if __name__ == '__main__':
    main()
