"""Tris Shell."""


import random


listeNonTriee = [random.randint(0, 1000) for i in range(10000)]


gaps = [1, 2, 4, 7, 10, 23, 57, 132, 301, 701]


def triParInsertion(lst):
    """Tris par insertion."""
    for i in range(1, len(lst)):
        tmp = lst[i]
        n = i
        while lst[n - 1] > tmp and n > 0:
            lst[n] = lst[n - 1]
            n -= 1
        lst[n] = tmp
    return lst


def gapSelection(n):
    """Return gap size."""
    if n >= 2100:
        j = 1
        while (2.3*701*j) < (n / 3 + 2):
            j += 1
        return int((j - 1)*2.3*701)
    else:
        for gap in gaps[::-1]:
            if gap < n / 3 + 2:
                return gap


def shell(lst):
    """Shell."""
    n = len(lst)
    gap = gapSelection(n)
    while gap != 0:
        for i in range(gap):
            lst[i::gap] = triParInsertion(lst[i::gap])
        n -= gap
        if n < 0:
            break
        gap = gapSelection(n)
    return lst
