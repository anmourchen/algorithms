from collections import defaultdict
from heapq import heappop, heappush


def load_graph(filename):
    """
    load the graph structure from the txt file
    :param filename: txt file path
    :return: graph structure
    """
    graph = defaultdict(list)
    with open(filename) as f:
        for lines in f:
            line = lines.split()
            if line:
                node = int(line[0])
                heads = [int(ln.split(',')[0]) for ln in line[1:]]
                costs = [int(ln.split(',')[1]) for ln in line[1:]]
                graph[node] = [(head, cost) for head, cost in zip(heads, costs)]
    return graph


def dijkstra(graph, source, sink):
    """
    implement Dijkstra algorithm on the graph to find the shortest path
    :param graph: a python dictionary representing the graph structure
    :param source: starting vertex
    :param sink: end vertex
    :return: shortest length, path from source to sink
    """
    queue, visited, mins = [(0, source, ())], set(), {source: 0}
    while queue:
        (cost, vertex, path) = heappop(queue)
        if vertex not in visited:
            visited.add(vertex)
            path = path + (vertex,)
            if vertex == sink:
                return cost, path

            for head, c in graph.get(vertex, ()):
                curr_cost = mins.get(head, None)
                new_cost = cost + c
                if curr_cost is None or new_cost < curr_cost:
                    mins[head] = new_cost
                    heappush(queue, (new_cost, head, path))

    return 1000000, None


def main():
    # simple test case
    graph = load_graph('dijkstraTest.txt')
    costs = [dijkstra(graph, 1, v)[0] for v in range(1, 9)]
    assert costs == [0, 1, 2, 3, 4, 4, 3, 2]

    graph = load_graph('dijkstraData.txt')
    nodes = [7, 37, 59, 82, 99, 115, 133, 165, 188, 197]
    costs = [dijkstra(graph, 1, node)[0] for node in nodes]
    print(costs)


if __name__ == '__main__':
    main()
