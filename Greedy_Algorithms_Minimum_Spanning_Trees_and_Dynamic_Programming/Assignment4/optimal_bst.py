def read_data(filepath):
    """ read the weights from txt file """
    with open(filepath) as f:
        lines = f.readlines()
        nums = lines[1].split(',')
        p = [int(num) for num in nums]

    return p


def optimal_bst(p):
    """ compute the optimal BST using dynamic programming """
    n = len(p)
    A = {}
    for s in range(n):
        for i in range(0, n - s):
            p_sum = sum([p[t] for t in range(i, i + s + 1)])
            A[i, i - 1] = A[i + s + 1, i + s] = 0
            A[i, i + s] = p_sum + min([A[i, r - 1] + A[r + 1, i + s] for r in range(i, i + s + 1)])

    return A[0, n - 1]


def main():
    p = read_data('optimal_bst.txt')
    assert optimal_bst(p) == 2780


if __name__ == '__main__':
    main()
