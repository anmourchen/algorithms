from itertools import combinations
import math


def distance(cities, i, j):
    """ compute the Euclidean distance between two cities, cities[i + 1] and cities[j + 1] """
    return math.sqrt((cities[i - 1][0] - cities[j - 1][0]) ** 2 + (cities[i - 1][1] - cities[j - 1][1]) ** 2)


def read_data(filename):
    """ read the cities data ffrom txt file and store them as a list of tuples of (x, y) """
    cities = []
    with open(filename) as f:
        lines = f.readlines()
        n = int(lines[0].split()[0])
        for line in lines[1:]:
            cities.append((float(line.split()[0]), float(line.split()[1])))

    return cities, n


def tsp(cities, n):
    """ find the shortest tour distance using dynamic programming
        solves in O(n^2 * 2^n) time
    """
    combos = {}
    i = 0
    for k in range(n + 1):
        for combo in combinations(range(2, n + 1), k):
            combos[(1,) + combo] = i
            i += 1
    last = i - 1
    A = {}
    for i in range(len(combos)):
        A[i, 1] = 0 if i == 0 else float('inf')
    for m in range(2, n + 1):
        for combo in combos.keys():
            if len(combo) != m:
                continue
            for j in set(combo) - {1}:
                tmp = []
                for k in set(combo) - {j}:
                    idx = combos[tuple(sorted(set(combo) - {j}))]
                    tmp.append(A[idx, k] + distance(cities, k, j))
                A[combos[combo], j] = min(tmp)
    return min([A[last, j] + distance(cities, j, 1) for j in range(2, n + 1)])


def main():
    # test case
    cities, n = read_data('tsp_test.txt')
    assert int(tsp(cities, n)) == 13
    # heuristic approach
    # https://www.coursera.org/learn/algorithms-npcomplete/discussions/weeks/2/threads/FNo8tpFPEeeH2hLapWklpg
    # divide the cities into two parts, cities[0:13] and cities[11:25]
    # compute the shortest tour distance first then subtract twice of distance of cities 12 and 13
    cities, n = read_data('tsp.txt')
    cities1, n1, cities2, n2 = cities[:13], 13, cities[11:], 14
    dst1 = tsp(cities1, n1)
    dst2 = tsp(cities2, n2)
    print(int(dst1 + dst2 - 2 * distance(cities, 12, 13)))


if __name__ == '__main__':
    main()
