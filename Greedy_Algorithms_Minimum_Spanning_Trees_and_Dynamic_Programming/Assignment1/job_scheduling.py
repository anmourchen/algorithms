def read_jobs(filename):
    """ load the weight and length from txt file """
    with open(filename) as f:
        lines = f.readlines()
        n = int(lines[0].split('\n')[0])
        w = [int(line.split()[0]) for line in lines[1:]]
        c = [int(line.split()[1]) for line in lines[1:]]
        return n, w, c


def compute_cost(n, w, l):
    """ compute the weighted completed time given weights and lengths """
    cost = 0
    for i in range(n):
        cost += w[i] * sum(l[:i + 1])
    return cost


def greedydiff(n, w, l):
    """ sort the weights and lengths using difference """
    diff = [wi - li for wi, li in zip(w, l)]
    diff_tuple = [(di, wi) for di, wi in zip(diff, w)]
    index = sorted(range(n), key=lambda k: diff_tuple[k], reverse=True)
    return [w[i] for i in index], [l[i] for i in index]


def greedyratio(n, w, l):
    """ sort the weights and lengths using ratio """
    ratio = [wi / li for wi, li in zip(w, l)]
    index = sorted(range(n), key=lambda k: ratio[k], reverse=True)
    return [w[i] for i in index], [l[i] for i in index]


def main():
    n, w, l = read_jobs('jobs_test.txt')
    greedy_w, greed_l = greedydiff(n, w, l)
    assert compute_cost(n, greedy_w, greed_l) == 68615
    greedy_w, greed_l = greedyratio(n, w, l)
    assert compute_cost(n, greedy_w, greed_l) == 67247

    n, w, l = read_jobs('jobs.txt')
    greedy_w, greed_l = greedydiff(n, w, l)
    print(compute_cost(n, greedy_w, greed_l))
    greedy_w, greed_l = greedyratio(n, w, l)
    print(compute_cost(n, greedy_w, greed_l))


if __name__ == '__main__':
    main()
