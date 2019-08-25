from collections import defaultdict
from heapq import heapify, heappop, heappush


def load_graph(filename):
    """ load the graph from the txt file """
    graph = defaultdict(list)
    with open(filename) as f:
        lines = f.readlines()
        for line in lines[1:]:
            graph[int(line.split()[0])].append([int(line.split()[1]), int(line.split()[2])])
            graph[int(line.split()[1])].append([int(line.split()[0]), int(line.split()[2])])

    return graph


def mst(graph):
    """ implement Prim's algorithm on MST """
    start = list(graph.keys())[0]
    visited, costs = {start}, []
    unvisited = []

    for v in graph[start]:
        heappush(unvisited, [v[1], v[0]])

    while visited != set(graph.keys()):
        winner = heappop(unvisited)
        visited.add(winner[1])
        costs.append(winner[0])
        for i, v in enumerate(unvisited):
            if v[1] == winner[1]:
                v[0] = float('inf')

        heapify(unvisited)

        for v in graph[winner[1]]:
            if v[0] not in visited:
                heappush(unvisited, [v[1], v[0]])

    return sum(costs)


def main():
    graph = load_graph('edges_test.txt')
    assert mst(graph) == 14

    graph = load_graph('edges.txt')
    print(mst(graph))


if __name__ == '__main__':
    main()
