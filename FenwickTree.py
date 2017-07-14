class FenwickTree:
    def __init__(self, size):
        self.arr = [0] * size
        self.n = size

    def add(self, i, val):
        while i < self.n:
            self.arr[i] += val
            i |= i + 1

    def sum(self, i):  # sum for [0..i)
        i -= 1
        res = 0
        while i >= 0:
            res += self.arr[i]
            i = (i & (i + 1)) - 1
        return res


def main():
    n = 5
    ft = FenwickTree(n)
    for i in range(n):  # 5 4 3 2 1
        ft.add(i, n - i)

    assert ft.sum(4) == 14
    ft.add(3, 2)  # 5 4 5 2 1
    assert ft.sum(4) == 16
    assert ft.sum(5) == 17


main()
