# O(n)
def prefix_func(s):
    n = len(s)
    pi = [0] * n
    for i in range(1, n):
        j = pi[i - 1]
        while j > 0 and s[i] != s[j]:
            j = pi[j - 1]
        if s[i] == s[j]:
            j += 1
        pi[i] = j
    return pi


# O(n)
def substrings_count(pattern, text, delim="##!##"):
    m = len(pattern)
    s = pattern + delim + text
    pi = prefix_func(s)
    ans = [0] * (m + 1)
    for i in range(m + len(delim), len(s)):
        ans[pi[i]] += 1
    for i in range(m, 0, -1):
        ans[pi[i - 1]] += ans[i]
    return ans[1:]


def main():
    text = "aaaaa"
    pattern = "aaa"
    assert prefix_func(text) == [0, 1, 2, 3, 4]
    assert substrings_count(pattern, text) == [5, 4, 3]

    text = "aaaba"
    assert prefix_func(text) == [0, 1, 2, 0, 1]
    assert substrings_count(pattern, text) == [4, 2, 1]


main()
