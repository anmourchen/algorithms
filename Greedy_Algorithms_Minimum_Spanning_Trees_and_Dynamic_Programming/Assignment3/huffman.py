from heapq import heapify, heappop, heappush


def read_code(filepath):
    """ read the weights for each symbol from txt file
        return: a python dictionary (key: symbol id, value: (weight, min coding length, max coding length)
    """
    code = {}
    with open(filepath) as f:
        lines = f.readlines()
        for i, line in enumerate(lines[1:]):
            code[i] = [int(line.split()[0]), 0, 0]
    return code


def huffman_coding(code):
    """ compute the min and max coding length from a given list of symbols
        using heap to find the two symbols with minimal weights
    """
    weight = [[w[0], w[1], w[2]] for node, w in code.items()]
    heapify(weight)
    while len(weight) > 1:
        i, j = heappop(weight), heappop(weight)
        heappush(weight, [i[0] + j[0], 1 + min(i[1], j[1]), 1 + max(i[2], j[2])])
    return weight[0][1], weight[0][2]


def main():
    # test case
    code = read_code('huffman_small.txt')
    min_length, max_length = huffman_coding(code)
    assert min_length, max_length == (3, 6)

    code = read_code('huffman.txt')
    print(huffman_coding(code))


if __name__ == '__main__':
    main()
