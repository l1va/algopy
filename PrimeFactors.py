import math


# O(sqrt(n))
def prime_factors(n):
    res = []
    if n % 2 == 0:
        res.append(2)
    while n % 2 == 0:
        n //= 2
    for i in range(3, int(math.sqrt(n) + 1), 2):
        if n % i == 0:
            res.append(i)
        while n % i == 0:
            n //= i
    if n > 2:
        res.append(n)
    return res


def main():
    assert prime_factors(10 ** 12) == [2, 5]
    assert prime_factors(3) == [3]
    assert prime_factors(12345678912) == [2, 3, 7, 9185773]
    assert prime_factors(200560490130) == [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31]


main()
