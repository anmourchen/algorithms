import threading

from tqdm import tqdm

hashtable = {}


def read_numbers(filename):
    """ read the list of integers from the txt file """
    with open(filename) as f:
        lines = f.readlines()
    nums = [int(line.split()[0]) for line in lines]
    for num in nums:
        hashtable[num] = 1
    return nums


def two_sum(nums, low, high):
    """ find the counts of a target in [low, end] that satisfies sum of two distinct elements in nums equal to target
        TODO: finishing in about 3 hours, need to be optimized
    """
    count = 0
    for target in tqdm(range(low, high + 1)):
        tmp_dict = hashtable.copy()
        for num in nums:
            if num in hashtable and target - num in tmp_dict and num != target - num:
                count += 1
                break

    return count


def main():
    # test case
    nums = read_numbers('2sum_test.txt')
    count = two_sum(nums, 3, 10)
    assert count == 8

    nums = read_numbers('2sum.txt')
    count = two_sum(nums, -10000, 10000)
    print(count)


if __name__ == '__main__':
    thread = threading.Thread(target=main)
    thread.start()

