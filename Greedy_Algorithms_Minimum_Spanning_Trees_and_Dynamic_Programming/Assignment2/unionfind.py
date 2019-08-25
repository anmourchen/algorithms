""" Union Find basic structure """


class UnionFind():
    def __init__(self, nodes):
        self.root = dict(zip(nodes, nodes))
        self.subtree = dict(zip(nodes, [[node] for node in nodes]))

    def find(self, node):
        """ find the root of a node """
        return self.root[node]

    def union(self, i, j):
        """ union two nodes i and j by merging a smaller tree to the larger one """
        pi, pj = self.root[i], self.root[j]
        if pi != pj:
            if len(self.subtree[pj]) > len(self.subtree[pi]):
                pi, pj = pj, pi

            for node in self.subtree[pj]:
                self.root[node] = pi
            self.subtree[pi] += self.subtree[pj]
            del self.subtree[pj]

        else:
            return
