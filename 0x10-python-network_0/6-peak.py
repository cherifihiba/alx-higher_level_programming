#!/usr/bin/python3
"""Find peak module"""


def find_peak(list_of_integers):
    """Find peak in list"""
    if not list_of_integers:
        return None
    n = len(list_of_integers)
    mid = n // 2
    if (mid == n - 1 or list_of_integers[mid] >= list_of_integers[mid + 1]) and \
            (mid == 0 or list_of_integers[mid] >= list_of_integers[mid - 1]):
        return list_of_integers[mid]
    if mid != n - 1 and list_of_integers[mid + 1] > list_of_integers[mid]:
        return find_peak(list_of_integers[mid + 1:])
    return find_peak(list_of_integers[:mid])


if __name__ == "__main__":
    list_of_integers = [1, 2, 4, 6, 3]
    print(find_peak(list_of_integers))  # 6
    list_of_integers = [4, 2, 1, 2, 3, 1]
    print(find_peak(list_of_integers))  # 3
    list_of_integers = [2, 2, 2]
    print(find_peak(list_of_integers))  # 2
    list_of_integers = []
    print(find_peak(list_of_integers))  # None
    list_of_integers = [-2, -4, 2, 1]
    print(find_peak(list_of_integers))  # 2
    list_of_integers = [4, 2, 1, 2, 2, 2, 3, 1]
    print(find_peak(list_of_integers))  # 4
