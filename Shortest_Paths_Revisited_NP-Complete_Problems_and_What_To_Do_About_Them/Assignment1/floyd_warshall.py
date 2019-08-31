def read_graph(filename):
    """ read the graph structure from txt file """
    graph = {}
    with open(filename) as f:
        lines = f.readlines()
        n, m = int(lines[0].split()[0]), int(lines[0].split()[1])
        for line in lines[1:]:
            graph[int(line.split()[0]), int(line.split()[1])] = int(line.split()[2])

    return graph, n


def floyd_warshall(graph, n):
    """ compute the min all-pair shortest distance using floyd warshall algorithm
        O(n^2) using space optimization
        TODO: finishing in around 1 hour, still need to be optimized
    """
    A = {}
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            if i == j:
                A[i, j] = 0
            elif (i, j) in graph:
                A[i, j] = graph[i, j]
            else:
                A[i, j] = float('inf')

    for k in range(1, n + 1):
        A_next = {}
        for i in range(1, n + 1):
            for j in range(1, n + 1):
                A_next[i, j] = min(A.get((i, j)), A.get((i, k)) + A.get((k, j)))
        A = A_next.copy()

    if check_negative_cycle(A, n):
        return 'NULL'
    else:
        return min(A.values())


def check_negative_cycle(A, n):
    """ check if it has a negative cycle """
    for i in range(1, n + 1):
        if A.get((i, i)) < 0:
            return True
    return False


def main():
    # test case
    g1, n1 = read_graph('g_test.txt')
    assert floyd_warshall(g1, n1) == -2
    g2, n2 = read_graph('g2_test.txt')
    assert floyd_warshall(g2, n2) == 'NULL'

    g1, n1 = read_graph('g1.txt')
    print(floyd_warshall(g1, n1))
    g2, n2 = read_graph('g2.txt')
    print(floyd_warshall(g2, n2))
    g3, n3 = read_graph('g3.txt')
    print(floyd_warshall(g3, n3))


if __name__ == '__main__':
    main()
