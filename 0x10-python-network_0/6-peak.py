#!/usr/bin/python3
"""Find peak module"""


def find_peak(list_of_integers):
    """Find peak in list"""
    if not list_of_integers:
        return None
    n = len(list_of_integers)
    if n == 1:
        return list_of_integers[0]
    if list_of_integers[0] >= list_of_integers[1]:
        return list_of_integers[0]
    if list_of_integers[n - 1] >= list_of_integers[n - 2]:
        return list_of_integers[n - 1]
    for i in range(1, n - 1):
        if list_of_integers[i] >= list_of_integers[i - 1] and \
           list_of_integers[i] >= list_of_integers[i + 1]:
            return list_of_integers[i]

if __name__ == "__main__":
    list_of_integers = [1, 2, 4, 6, 3]
    print(find_peak(list_of_integers))  # 6
    list_of_integers = [4, 2, 1, 2, 3, 1]
    print(find_peak(list_of_integers))  # 4
    list_of_integers = [2, 2, 2]
    print(find_peak(list_of_integers))  # 2
    list_of_integers = []
    print(find_peak(list_of_integers))  # None
    list_of_integers = [-2, -4, 2, 1]
    print(find_peak(list_of_integers))  # 2
    list_of_integers = [4, 2, 1, 2, 2, 2, 3, 1]
    print(find_peak(list_of_integers))  # 4

"""
Complexity of find_peak function is O(n)
"""
