import random


def load_graph():
    """
    load the graph from the txt file
    :return: python dictionary representing the graph structure
    """
    graph = {}
    with open('kargerMinCut.txt') as f:
        for ln in f:
            line = ln.split()
            if line:
                vertices = [int(x) for x in line[1:]]
                graph[int(line[0])] = vertices
    return graph


def choose_random_edge(graph):
    """
    choose a random edge in the graph
    :param graph: a python dictionary representing the graph
    :return: two vertices representing an edge
    """
    v1 = list(graph.keys())[random.randint(0, len(graph) - 1)]
    v2 = list(graph[v1])[random.randint(0, len(graph[v1]) - 1)]
    return v1, v2


def contract_edge(graph, edge):
    """
    contract the edge in a given graph
    :param graph: a python dictionary representing the graph
    :param edge: a tuple of two vertices
    """
    v1 = graph[edge[0]]
    v1.extend(graph[edge[1]])
    del graph[edge[1]]

    for k in graph.keys():
        graph[k] = [edge[0] if x == edge[1] else x for x in graph[k]]

    graph[edge[0]] = [x for x in graph[edge[0]] if x != edge[0]]


def main():
    """
    Find the min cut of a given graph using randomized contraction
    """
    min_cut = []
    for _ in range(100):
        graph = load_graph()
        while len(graph) > 2:
            contract_edge(graph, choose_random_edge(graph))
        min_cut.append(len(graph[list(graph.keys())[0]]))

    print(min(min_cut))


if __name__ == '__main__':
    main()
