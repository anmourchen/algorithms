
def merge_sort(array):
    """
    Implement merge sort
    :param array: an unsorted list of integers
    :return: a sorted list of integers
    """
    if len(array) == 1:
        return array

    n = len(array)
    a, b = merge_sort(array[:n // 2]), merge_sort(array[n // 2:])
    # merge
    out = []
    i, j = 0, 0

    while i < len(a) and j < len(b):
        if a[i] < b[j]:
            out.append(a[i])
            i += 1
        else:
            out.append(b[j])
            j += 1
    if i < len(a):
        out += a[i:]

    if j < len(b):
        out += b[j:]

    return out


def main():
    a = [4, 1]
    assert merge_sort(a) == [1, 4]

    test = [1, 531, 232, 12, 312, 321, 1, 232, 5, 3, 53, 21, 32, 55, 332, 22]
    print('after sorting:')
    print(merge_sort(test))


if __name__  == '__main__':
    main()
