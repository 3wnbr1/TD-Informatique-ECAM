"""Tris par insertion, selection et bulle."""


import random


listeNonTriee = [random.randint(0, 1000) for i in range(10)]


def minimum(lst):
    """Return the index of minimum element."""
    mi = 0
    for i in range(len(lst)):
        if lst[i] < lst[mi]:
            mi = i
    return mi


def triParSelection(lst):
    """Tris par selection."""
    for i in range(len(lst)):
        m = minimum(lst[i::])
        lst[i + m], lst[i] = lst[i], lst[i + m]
    return lst


def triParInsertion(lst):
    """Tris par insertion."""
    for i in range(1, len(lst)):
        tmp = lst[i]
        n = i
        while lst[n-1] > tmp and n > 0:
            lst[n] = lst[n-1]
            n -= 1
        lst[n] = tmp
    return lst


def triBulle(lst):
    """Tris bulle."""
    for i in range(len(lst), 0, -1):
        for j in range(1, i):
            if lst[j] < lst[j-1]:
                lst[j], lst[j-1] = lst[j-1], lst[j]
    return lst
