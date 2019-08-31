import math


def distance(cities, i, j):
    """ compute the distance between cities i and j """
    return math.sqrt((cities[i][0] - cities[j][0]) ** 2 + (cities[i][1] - cities[j][1]) ** 2)


def read_data(filename):
    """ read the cities data from the txt file """
    cities = {}
    with open(filename) as f:
        lines = f.readlines()
        n = int(lines[0])
        for line in lines[1:]:
            cities[int(line.split()[0])] = [float(line.split()[1]), float(line.split()[2])]

    return cities, n


def tsp_nn(cities, n):
    """ compute the shortest distance using nearest neighbor heuristic approach"""
    visited = [1]
    dst = 0
    while len(visited) < n:
        unvisited = set(range(1, n + 1)) - set(visited)
        min_dst, j = min([(distance(cities, visited[-1], j), j) for j in unvisited])
        dst += min_dst
        visited.append(j)
    return int(dst + distance(cities, visited[-1], 1))


def main():
    # test case
    cities, n = read_data('nn_test.txt')
    assert tsp_nn(cities, n) == 623487

    cities, n = read_data('nn.txt')
    print(tsp_nn(cities, n))


if __name__ == '__main__':
    main()
