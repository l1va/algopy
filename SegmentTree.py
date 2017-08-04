class SegmentTree:
    def __init__(self, a):
        self.n = len(a)
        self.src = a
        self.arr = [0] * 4 * self.n
        self._build(1, 0, self.n - 1)

    # O(n)
    def _build(self, cur, l, r):
        if l == r:
            self.arr[cur] = self.src[l]
        else:
            m = (l + r) // 2
            self._build(cur * 2, l, m)
            self._build(cur * 2 + 1, m + 1, r)
            self.arr[cur] = self.arr[cur * 2] + self.arr[cur * 2 + 1]

    # O(log(n))
    def sum(self, l, r):  # sum for [l..r]
        return self._sum(1, 0, self.n - 1, l, r)

    def _sum(self, cur, tl, tr, l, r):
        if l > r:
            return 0
        if l == tl and r == tr:
            return self.arr[cur]
        tm = (tl + tr) // 2
        return self._sum(cur * 2, tl, tm, l, min(r, tm)) + \
               self._sum(cur * 2 + 1, tm + 1, tr, max(l, tm + 1), r)

    # O(log(n))
    def update(self, pos, val):
        self._update(1, 0, self.n - 1, pos, val)

    def _update(self, cur, tl, tr, pos, val):
        if tl == tr:
            self.arr[cur] = val
        else:
            tm = (tl + tr) // 2
            if pos <= tm:
                self._update(cur * 2, tl, tm, pos, val)
            else:
                self._update(cur * 2 + 1, tm + 1, tr, pos, val)
            self.arr[cur] = self.arr[cur * 2] + self.arr[cur * 2 + 1]


def main():
    a = [1, 1, 2, 1, 3]
    st = SegmentTree(a)
    assert st.sum(0, 4) == 8
    assert st.sum(1, 3) == 4
    assert st.sum(2, 4) == 6
    a = [0] * 10 ** 6
    for i in range(10 ** 6):
        a[i] = i + 1
    st = SegmentTree(a)
    assert st.sum(100, 10 ** 5 - 1) == (10 ** 5 + 1) * (10 ** 5 / 2) - (100 + 1) * 50  # 5000044950


main()
