from collections import defaultdict
from itertools import combinations

from unionfind import UnionFind


def read_nodes(filename):
    """ read the graph structure from the txt file by converting the binary to an integer
        return: a python dictionary {integer: line id}
    """
    nodes = defaultdict(list)
    with open(filename) as f:
        lines = f.readlines()
        for i, line in enumerate(lines[1:]):
            num = int(''.join(line.split()), 2)
            nodes[num].append(i)
    return nodes


def hamming1(num):
    """ return the list of numbers with 1 bit difference from num """
    masks = [1 << i for i in range(num.bit_length())]
    code = [num ^ mask for mask in masks]
    return code


def hamming2(num):
    """ return the list of numbers with 2 bit difference from num """
    masks = [(1 << i) ^ (1 << j) for (i, j) in combinations(range(num.bit_length()), 2)]
    code = [num ^ mask for mask in masks]
    return code


def kclustering(nodes):
    """ clustering the nodes by hamming distance """
    clusters = UnionFind(nodes)
    for num in nodes:
        for code in hamming1(num):
            if code in nodes:
                clusters.union(num, code)

        for code in hamming2(num):
            if code in nodes:
                clusters.union(num, code)

    return len(clusters.subtree.keys())


def main():
    graph = read_nodes('clustering-big.txt')
    print(kclustering(graph))


if __name__ == '__main__':
    main()
