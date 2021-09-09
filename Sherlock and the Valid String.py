# https://www.hackerrank.com/challenges/sherlock-and-valid-string/problem

from collections import Counter


def isValid(s):
    fre = Counter(s)
    if len(set(fre.values())) == 1:
        return "YES"
    else:
        val_fre = Counter(fre.values())
        if len(val_fre.values()) == 2:
            lstK = list(val_fre.keys())
            if 1 in lstK:
                if val_fre[1] == 1:
                    return "YES"
            elif abs(lstK[0] - lstK[1]) == 1:
                if lstK[0] > lstK[1]:
                    if val_fre[lstK[0]] == 1:
                        return "YES"
                else:
                    if val_fre[lstK[1]] == 1:
                        return "YES"
    return "NO"


if __name__ == '__main__':
    print(isValid('aabbccddeefghi'))
    print(isValid('abcdefghhgfedecba'))
