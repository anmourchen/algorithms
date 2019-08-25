import sys
sys.setrecursionlimit(2 ** 20)


def read_data(filepath):
    """ read the knapsack problem from txt file
            returns capacity, number of items, values and weights of each item
    """
    with open(filepath) as f:
        lines = f.readlines()
        w, n = int(lines[0].split()[0]), int(lines[0].split()[1])
        values = [int(line.split()[0]) for line in lines[1:]]
        weights = [int(line.split()[1]) for line in lines[1:]]

    return w, n, values, weights


def knapsack(values, weights, w, v):
    """ solving the knapsack problem using recursion
        TODO: still runs about 30 minutes
    """
    if w <= 0:
        return 0
    if len(values) == 1:
        if weights[0] <= w:
            return values[0]
        else:
            return 0
    v1 = v.get((len(values[:-1]), w))
    if not v1:
        v1 = knapsack(values[:-1], weights[:-1], w, v)
        v[(len(values[:-1]), w)] = v1
    v2 = v.get((len(values[:-1]), w - weights[-1]))
    if not v2:
        v2 = knapsack(values[:-1], weights[:-1], w - weights[-1], v)
        v[(len(values[:-1]), w - weights[-1])] = v2
    if weights[-1] <= w:
        v2 = v2 + values[-1]
    else:
        v2 = 0
    return max(v1, v2)


def main():
    w, n, values, weights = read_data('knapsack_big.txt')
    v = {}
    print(knapsack(values, weights, w, v))


if __name__ == '__main__':
    main()
