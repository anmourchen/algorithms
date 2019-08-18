def dfs(graph, start, visited=None):
    if not visited:
        visited = set()
    visited.add(start)
    print(start)
    for vertex in graph[start]:
        if vertex in visited:
            continue
        dfs(graph, vertex, visited)


def main():
    graph = {'A': ['B', 'C'],
             'B': ['A', 'D', 'E'],
             'C': ['A', 'F'],
             'D': ['B'],
             'E': ['B', 'F'],
             'F': ['C', 'E']
             }
    dfs(graph, 'A')


if __name__ == '__main__':
    main()
