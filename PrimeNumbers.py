# O(n*log(log(n)))
def primes_till(n):  # Sieve of Eratosthenes
    p = [True] * n
    for i in range(2, n):
        if p[i]:
            j = i * i
            while j < n:
                p[j] = False
                j += i
    res = []
    for i in range(2, n):
        if p[i]:
            res.append(i)
    return res


def main():
    till_100 = primes_till(100)
    assert len(till_100) == 25
    assert till_100 == [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]
    till_10_5 = primes_till(100000)
    assert len(till_10_5) == 9592
    assert till_10_5[9589] == 99971


main()
