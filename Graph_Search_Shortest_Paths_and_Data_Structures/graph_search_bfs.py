def bfs(graph, start, order=[]):
    visited, queue = set(), [start]
    while queue:
        vertex = queue.pop(0)
        if vertex not in visited:
            visited.add(vertex)
            order.append(vertex)
            queue.extend(set(graph[vertex]) - visited)

    return order


def main():
    graph = {'A': ['B', 'C'],
             'B': ['A', 'D', 'E'],
             'C': ['A', 'F'],
             'D': ['B'],
             'E': ['B', 'F'],
             'F': ['C', 'E']
             }
    order = bfs(graph, 'A')
    print(order)


if __name__ == '__main__':
    main()
