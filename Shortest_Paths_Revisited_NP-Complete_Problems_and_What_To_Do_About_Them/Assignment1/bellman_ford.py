def read_graph(filename):
    """ read the graph structure from txt file """
    graph = {}
    with open(filename) as f:
        lines = f.readlines()
        n, m = int(lines[0].split()[0]), int(lines[0].split()[1])
        for line in lines[1:]:
            graph[int(line.split()[0]), int(line.split()[1])] = int(line.split()[2])

    return graph, n


def bellman_ford(graph, s, n):
    """ compute the single-source shortest distance using bellman-ford algorithm
        TODO: running super slow, need to be optimized
    """
    A = {}
    for v in range(1, n + 1):
        if v == s:
            A[0, v] = 0
        else:
            A[0, v] = float('inf')

    for i in range(1, n):
        for v in range(1, n + 1):
            A_temp = [A[i - 1, w] + graph[w, v] for w in range(1, n + 1) if (w, v) in graph]
            A[i, v] = min(A[i - 1, v], min(A_temp))

    # run BF algorithm one more time to detect negative cycles
    for v in range(1, n + 1):
        A_temp = [A[n - 1, w] + graph[w, v] for w in range(1, n + 1) if (w, v) in graph]
        A[n, v] = min(A[n - 1, v], min(A_temp))

    for v in range(1, n + 1):
        if A[n, v] != A[n - 1, v]:
            return

    return min([A[n - 1, v] for v in range(1, n + 1)])


def all_pairs(graph, n):
    """ find the min all-pair shortest distance """
    As = []
    for s in range(1, n + 1):
        dst = bellman_ford(graph, s, n)
        if dst is None:
            return 'NULL'
        else:
            As.append(dst)
    return min(As)


def main():
    # test case
    g1, n1 = read_graph('g_test.txt')
    assert all_pairs(g1, n1) == -2
    g2, n2 = read_graph('g2_test.txt')
    assert all_pairs(g2, n2) == 'NULL'

    g1, n1 = read_graph('g1.txt')
    print(all_pairs(g1, n1))
    g2, n2 = read_graph('g2.txt')
    print(all_pairs(g2, n2))
    g3, n3 = read_graph('g3.txt')
    print(all_pairs(g3, n3))


if __name__ == '__main__':
    main()
