def read_number(filename):
    """ Read the numbers from the txt file """
    with open(filename) as f:
        lines = f.readlines()
    nums = [int(line.split('\n')[0]) for line in lines]
    return nums


def merge_sort_count(array):
    """
    Count the number of inversions in an array
    :param array: a list of integers
    :return: a sorted list of integers, number of inversions
    """
    if len(array) == 1:
        return array, 0

    n = len(array)
    a, a_count = merge_sort_count(array[:n // 2])
    b, b_count = merge_sort_count(array[n // 2:])

    count = a_count + b_count

    # merge two sorted lists
    i, j, k = 0, 0, 0
    out = [0] * (len(a) + len(b))
    while i < len(a) and j < len(b):
        if a[i] <= b[j]:
            out[k] = a[i]
            i += 1
            k += 1
        else:
            count += len(a) - i
            out[k] = b[j]
            j += 1
            k += 1

    if i < len(a):
        out[k:] = a[i:]

    if j < len(b):
        out[k:] = b[j:]

    return out, count


def main():
    # test case
    nums = read_number('count_inversions_test.txt')
    assert merge_sort_count(nums)[1] == 28

    nums = read_number('IntegerArray.txt')
    print(merge_sort_count(nums)[1])


if __name__ == '__main__':
    main()
