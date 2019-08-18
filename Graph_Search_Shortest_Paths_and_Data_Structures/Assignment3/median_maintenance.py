from heapq import heappop, heappush


def read_data(filename):
    """ load the numbers from txt file """
    with open(filename) as f:
        nums = [int(line.split()[0]) for line in f]
    return nums


def find_medians(x, heap_low, heap_high):
    """
    find the medians using two heaps
    :param x: integer to insert
    :param heap_low: a max heap representing the smallest half of the array
    :param heap_high: a min heap represneting the largest half of the array
    :return: median
    """
    if len(heap_low) == 0:
        heappush(heap_low, -x)
    else:
        m = -heap_low[0]
        if x > m:
            heappush(heap_high, x)
            if len(heap_high) > len(heap_low):
                y = heappop(heap_high)
                heappush(heap_low, -y)
        else:
            heappush(heap_low, -x)
            if len(heap_low) > len(heap_high) + 1:
                y = -heappop(heap_low)
                heappush(heap_high, y)

    return -heap_low[0]


def main():
    # test case
    nums = read_data('median_test.txt')
    heap_low, heap_high = [], []
    median_sum = sum([find_medians(num, heap_low, heap_high) for num in nums]) % 10000
    assert median_sum == 9335

    nums = read_data('median.txt')
    heap_low, heap_high = [], []
    median_sum = sum([find_medians(num, heap_low, heap_high) for num in nums]) % 10000
    print(median_sum)


if __name__ == '__main__':
    main()
