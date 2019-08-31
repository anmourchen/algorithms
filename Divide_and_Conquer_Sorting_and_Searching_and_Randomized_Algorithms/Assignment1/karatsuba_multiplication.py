def karatsuba(x, y):
    """
    Implement Karatuba Multiplication of two integers
    TODO: run time is still O(n^2)
    """
    if len(str(x)) == 1 and len(str(y)) == 1:
        return x * y

    n1, n2 = len(str(x)), len(str(y))
    b, d = x % (10 ** (n1 // 2)), y % (10 ** (n2 // 2))
    a, c = x // (10 ** (n1 // 2)), y // (10 ** (n2 // 2))
    ac = karatsuba(a, c)
    bd = karatsuba(b, d)
    ad = karatsuba(a, d)
    bc = karatsuba(b, c)
    return 10 ** (n1// 2 + n2 // 2) * ac + 10 ** (n1 // 2) * ad + 10 ** (n2 // 2) * bc + bd


def main():
    a, b = 15, 23
    assert karatsuba(a, b) == a * b
    c, d = 12052, 12
    assert karatsuba(c, d) == c * d

    x = 3141592653589793238462643383279502884197169399375105820974944592
    y = 2718281828459045235360287471352662497757247093699959574966967627
    print(karatsuba(x, y))


if __name__ == '__main__':
    main()
