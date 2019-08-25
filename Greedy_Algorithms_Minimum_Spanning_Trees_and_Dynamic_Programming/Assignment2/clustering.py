from unionfind import UnionFind


def read_cluster(filename):
    """ read the graph structure from the txt file
        return: a list of tuples (node1, node2, cost)
    """
    with open(filename) as f:
        lines = f.readlines()
        graph = [(int(line.split()[0]), int(line.split()[1]), int(line.split()[2])) for line in lines[1:]]
    return graph


def kclustering(graph, k):
    """ compute the maximum spacing of a k-cluster """
    nodes = set()
    for u, v, d in graph:
        nodes.add(u)
        nodes.add(v)

    group = UnionFind(nodes)
    # sort the graph by costs
    graph = sorted(graph, key=lambda x: x[2])

    while len(group.subtree.keys()) > k:
        u, v, d = graph.pop(0)
        group.union(u, v)

    # do not output the cost between two nodes that are both in the same cluster
    while True:
        u, v, min_cost = graph.pop(0)
        if group.find(u) != group.find(v):
            break

    return min_cost


def main():
    graph = read_cluster('cluster.txt')
    print(kclustering(graph, 4))


if __name__ == '__main__':
    main()
