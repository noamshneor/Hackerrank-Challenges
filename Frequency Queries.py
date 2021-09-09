# https://www.hackerrank.com/challenges/frequency-queries/problem

from collections import Counter


def freqQuery(queries):
    fre = Counter()
    ans = []
    for i in range(len(queries)):
        if queries[i][0] == 1:
            fre[queries[i][1]] += 1
        elif queries[i][0] == 2:
            if queries[i][1] in fre and fre[queries[i][1]] > 0:
                fre[queries[i][1]] -= 1
        else:
            if queries[i][1] in set(fre.values()):
                ans.append(1)
            else:
                ans.append(0)
    return ans


if __name__ == '__main__':
    print(freqQuery([(1, 1), (2, 2), (3, 2), (1, 1), (1, 1), (2, 1), (3, 2)]))
