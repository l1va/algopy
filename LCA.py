class LCA:
    # O(n*log(n))
    def __init__(self, g, root=0):
        n = len(g)
        self.g = g
        self.tin = [0] * n
        self.tout = [0] * n
        self.up = [0] * n
        l = 1
        while (1 << l) <= n:
            l += 1
        self.up = [[0] * (l + 1) for _ in range(n)]
        self.l = l
        self._dfs(root)

    def _upper(self, a, b):
        return self.tin[a] <= self.tin[b] and self.tout[a] >= self.tout[b]

    def _dfs(self, root):
        timer = 0
        q = [(root, 0)]
        first = [True] * len(self.g)
        while len(q) > 0:
            v, p = q[-1]
            if first[v]:
                timer += 1
                self.tin[v] = timer
                self.up[v][0] = p
                for i in range(1, self.l + 1):
                    self.up[v][i] = self.up[self.up[v][i - 1]][i - 1]
                for to in self.g[v]:
                    if to != p:
                        q.append((to, v))
                first[v] = False
            else:
                q.pop()
                timer += 1
                self.tout[v] = timer

    # O(log(n))
    def lca(self, a, b):
        if self._upper(a, b):
            return a
        if self._upper(b, a):
            return b
        for i in range(self.l, -1, -1):
            if not self._upper(self.up[a][i], b):
                a = self.up[a][i]
        return self.up[a][0]


def main():
    g = [[1, 2, 3],
         [0, 4, 5],
         [0],
         [0, 6],
         [1, 7, 8],
         [1],
         [3],
         [4],
         [4]]
    l = LCA(g)
    assert l.lca(3, 7) == 0
    assert l.lca(5, 8) == 1
    assert l.lca(1, 7) == 1
    assert l.lca(4, 1) == 1
    assert l.lca(4, 3) == 0
    assert l.lca(7, 8) == 4
    assert l.lca(5, 4) == 1
    assert l.lca(2, 6) == 0


main()
