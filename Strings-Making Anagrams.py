# https://www.hackerrank.com/challenges/ctci-making-anagrams/problem

from collections import Counter


def makeAnagram(a, b):
    fre_a = Counter(a)
    fre_b = Counter(b)
    ans = 0
    sy = set(fre_a.keys()).symmetric_difference(set(fre_b.keys()))
    un = set(fre_a.keys()).intersection(set(fre_b.keys()))
    for i in sy:
        if i in fre_a.keys():
            ans += fre_a[i]
        if i in fre_b.keys():
            ans += fre_b[i]
    for i in un:
        ans += abs(fre_a[i] - fre_b[i])
    return ans


if __name__ == '__main__':
    print(makeAnagram('cde', 'dcf'))
    print(makeAnagram('abc', 'cde'))
