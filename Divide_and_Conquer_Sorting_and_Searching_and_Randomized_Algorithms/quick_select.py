import random


def partition(array, low, high):
    """
    Partition the array based on pivot and return the index of the pivot
    :param array: a list of distinct integers
    :param low: starting index of the list
    :param high: end index of the list
    :return: index of the pivot
    """
    pivot = random.randint(low, high)
    # swap the pivot to the last element
    array[high], array[pivot] = array[pivot], array[high]
    i = low
    for j in range(low, high):
        if array[j] < array[high]:
            array[i], array[j] = array[j], array[i]
            i += 1
    array[i], array[high] = array[high], array[i]
    return i


def RSelect(array, low, high, i):
    """
    Quick select the (i + 1)th smallest element in the list using O(n) time on average
    :param array: a list of integers
    :param low: starting index of the list
    :param high: end index of the list
    :param i: index
    :return: (i + 1)th smallest element in the list
    """
    if low == high:
        return array[low]
    pi = partition(array, low, high)
    if pi < i:
        return RSelect(array, pi + 1, high, i - pi)
    elif pi == i:
        return array[pi]
    else:
        return RSelect(array, low, pi - 1, i)


def main():
    array = [10, 3, 23, 9, 16, 21]
    i = 3
    a = RSelect(array, 0, len(array) - 1, i - 1)
    assert a == 10


if __name__ == '__main__':
    main()
