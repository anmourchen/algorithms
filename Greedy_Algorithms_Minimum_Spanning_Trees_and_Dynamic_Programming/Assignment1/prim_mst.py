def load_graph(filename):
    """ load the graph from the txt file """
    graph = {}
    nodes = set()
    with open(filename) as f:
        lines = f.readlines()
        for line in lines[1:]:
            v1 = int(line.split()[0])
            v2 = int(line.split()[1])
            c = int(line.split()[2])
            graph[(v1, v2)] = c
            nodes.add(v1)
            nodes.add(v2)

    return graph, nodes


def mst(graph, nodes):
    """ implement Prim's algorithm on MST """
    span = {list(nodes)[0]}
    cost = []
    while span != nodes:
        min_cost = float("inf")
        for v1 in span:
            for v2 in nodes - span:
                if (v1, v2) in graph and graph[(v1, v2)] < min_cost:
                    node = v2
                    min_cost = graph[(v1, v2)]

                if (v2, v1) in graph and graph[(v2, v1)] < min_cost:
                    node = v2
                    min_cost = graph[(v2, v1)]

        span.add(node)
        cost.append(min_cost)
    return sum(cost)


def main():
    graph, nodes = load_graph('edges_test.txt')
    assert mst(graph, nodes) == 14

    graph, nodes = load_graph('edges.txt')
    print(mst(graph, nodes))


if __name__ == '__main__':
    main()
