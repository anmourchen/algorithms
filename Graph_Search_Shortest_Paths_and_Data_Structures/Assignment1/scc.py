from collections import defaultdict
import sys
import threading


class Track():
    """ Use Track() class to record all the information """
    def __init__(self):
        self.visited = set()
        self.current_time = 0
        self.current_source = []
        self.leader = defaultdict(list)
        self.finishing_times = {}

    def addNode(self, node):
        """ Add node to a leader dictionary """
        self.leader[self.current_source].append(node)


def dfs(graph, start, track):
    """ DFS on the graph from start vertex"""
    track.visited.add(start)
    track.addNode(start)
    for v in graph[start]:
        if v not in track.visited:
            dfs(graph, v, track)

    track.current_time += 1
    track.finishing_times[start] = track.current_time


def dfs_loop(graph, nodes, track):
    """ Loop over the nodes on the graph using DFS """
    for node in nodes:
        if node not in track.visited:
            track.current_source = node
            dfs(graph, node, track)


def load_graph(filename):
    """ Load the graph structure from the txt file """
    edges = []
    with open(filename) as f:
        for lines in f:
            line = lines.split()
            edges.append((int(line[0]), int(line[1])))

    nodes = list(set([v for edge in edges for v in edge]))
    graph = {i: [] for i in range(1, len(nodes) + 1)}
    graph_rev = {i: [] for i in range(1, len(nodes) + 1)}
    for edge in edges:
        graph[edge[0]].append(edge[1])
        graph_rev[edge[1]].append(edge[0])

    return graph, graph_rev, nodes


def scc(graph, graph_rev, nodes):
    """ Compute the SCC components """
    track = Track()
    dfs_loop(graph_rev, nodes, track)
    sorted_nodes = sorted(track.finishing_times, key=track.finishing_times.get, reverse=True)
    track = Track()
    dfs_loop(graph, sorted_nodes, track)
    return track


def most_common(leader, x):
    """ Find the top x elements """
    results = [len(v) for k, v in leader.items()] + [0] * x
    return sorted(results, reverse=True)[: x]


def main():
    graph, graph_rev, nodes = load_graph("scc_test.txt")
    track = scc(graph, graph_rev, nodes)
    assert most_common(track.leader, 5) == [6, 3, 2, 1, 0]

    graph, graph_rev, nodes = load_graph("SCC.txt")
    track = scc(graph, graph_rev, nodes)
    print(most_common(track.leader, 5))


if __name__ == '__main__':
    threading.stack_size(67108864)  # 64MB stack
    sys.setrecursionlimit(2 ** 20)  # approx 1 million recursions
    thread = threading.Thread(target=main)  # instantiate thread object
    thread.start()  # run program at target
