def read_graph(filepath):
    with open(filepath) as f:
        lines = f.readlines()
        num = [int(line.split()[0]) for line in lines[1:]]
    return num


def mwis(num):
    W = [0] * (len(num) + 1)
    W[1] = num[0]
    for i in range(2, len(num) + 1):
        W[i] = max(W[i - 1], W[i - 2] + num[i - 1])

    S = []
    i = len(num)
    while i > 0:
        if W[i] > W[i - 2] + num[i - 1]:
            i -= 1
        else:
            S.append(i)
            i -= 2
    return W[len(num)], S


def main():
    # test case
    num = read_graph('mwis_small.txt')
    weight, vertices = mwis(num)
    assert weight == 2617
    assert vertices == [10, 7, 4, 2]

    num = read_graph('mwis.txt')
    _, vertices = mwis(num)
    candidates = [1, 2, 3, 4, 17, 117, 517, 997]
    s = ['1' if i in vertices else '0' for i in candidates]
    print(''.join(s))


if __name__ == '__main__':
    main()
