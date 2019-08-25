def read_data(filepath):
    """ read the strings, gap cost and mismatch cost from txt file """
    with open(filepath) as f:
        lines = f.readlines()
        gap, mismatch = int(lines[1].split()[0]), int(lines[1].split()[1])
        x = lines[2].split()[0]
        y = lines[3].split()[0]

    return x, y, gap, mismatch


def alignment(x, y, gap, mismatch):
    """ compute minimal alignment cost using dynamic programming """
    p = [[0 for i in range(len(y) + 1)] for j in range(len(x) + 1)]
    for i in range(1, len(x)):
        p[i][0] = i * gap
    for j in range(1, len(y)):
        p[0][j] = j * gap

    for i in range(1, len(x) + 1):
        for j in range(1, len(y) + 1):
            p[i][j] = min(p[i - 1][j - 1] + mismatch * (x[i - 1] != y[j - 1]),
                          p[i - 1][j] + gap,
                          p[i][j - 1] + gap)
    return p[len(x)][len(y)]


def main():
    x, y, gap, mismatch = read_data('sequence_alignment.txt')
    assert alignment(x, y, gap, mismatch) == 224


if __name__ == '__main__':
    main()
