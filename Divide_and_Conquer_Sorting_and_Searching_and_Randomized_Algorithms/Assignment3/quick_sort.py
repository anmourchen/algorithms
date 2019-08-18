comparisons = 0


def read_number(filename):
    """ Read the numbers from the txt file """
    with open(filename) as f:
        lines = f.readlines()
    nums = [int(line.split('\n')[0]) for line in lines]
    return nums


def find_median(array, first, middle, last):
    """
    find the index of the median of three
    :param array: a list of integers
    :param first: index of first element
    :param middle: index of middle element
    :param last: index of last element
    :return: index of the median of three
    """
    if min(array[first], array[last]) < array[middle] < max(array[first], array[last]):
        return middle
    elif min(array[middle], array[last]) < array[first] < max(array[middle], array[last]):
        return first
    else:
        return last


def partition(array, low, high, mode):
    """
    partition the array so that left partition is always smaller than pivot and right partition is greater than pivot
    :param array: a list of unsorted integers
    :param low: starting index of list
    :param high: end index of list
    :param mode: string "first", "last" or "median"
    :return: the index of the pivot after partitioning
    """
    global comparisons
    # use the last element as a pivot
    if mode == 'first':
        pivot = low
    elif mode == 'last':
        pivot = high
    else:
        pivot = find_median(array, low, low + (high - low) // 2, high)
    # swap to the first
    array[pivot], array[low] = array[low], array[pivot]
    i = low + 1
    for j in range(low + 1, high + 1):
        if array[j] < array[low]:
            array[i], array[j] = array[j], array[i]
            i += 1
    array[i - 1], array[low] = array[low], array[i - 1]
    comparisons += high - low
    return i - 1


def quick_sort(array, low, high, mode):
    """
    implement quick sort function
    :param array: a list of unsorted integers
    :param low: starting index of list
    :param high: starting index of list
    :param mode: string "first", "last" or "median"
    :return: sort the integers in place in O(nlog(n)) time
    """
    if low < high:
        pi = partition(array, low, high, mode)
        quick_sort(array, low, pi - 1, mode)
        quick_sort(array, pi + 1, high, mode)


def main():
    global comparisons
    # test case
    nums = read_number('QuickSort_test.txt')
    comparisons = 0
    quick_sort(nums, 0, len(nums) - 1, 'first')
    assert comparisons == 620
    nums = read_number('QuickSort_test.txt')
    comparisons = 0
    quick_sort(nums, 0, len(nums) - 1, 'last')
    assert comparisons == 573
    nums = read_number('QuickSort_test.txt')
    comparisons = 0
    quick_sort(nums, 0, len(nums) - 1, 'median')
    assert comparisons == 502

    nums = read_number('QuickSort.txt')
    comparisons = 0
    quick_sort(nums, 0, len(nums) - 1, 'first')
    print(comparisons)
    nums = read_number('QuickSort.txt')
    comparisons = 0
    quick_sort(nums, 0, len(nums) - 1, 'last')
    print(comparisons)
    nums = read_number('QuickSort.txt')
    comparisons = 0
    quick_sort(nums, 0, len(nums) - 1, 'median')
    print(comparisons)


if __name__ == '__main__':
    main()
