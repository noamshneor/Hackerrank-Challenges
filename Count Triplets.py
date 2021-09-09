# https://www.hackerrank.com/challenges/count-triplets-1/problem

from collections import Counter


def countTriplets(arr, r):
    a = Counter(arr)
    b = Counter()
    s = 0
    for i in arr:
        j = i // r
        k = i * r
        a[i] -= 1  # decrement of the counter of the element
        if b[j] and a[k] and i % r == 0:
            s += b[j] * a[k]
        b[i] += 1
    return s


if __name__ == '__main__':
    print(countTriplets([1, 4, 16, 64], 4))
