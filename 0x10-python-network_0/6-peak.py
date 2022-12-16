#!/usr/bin/python3
"""Find Peek Module."""

def find_peak(arr):
    """finds a peak in a list of unsorted integer."""
    l = 0
    r = len(arr)

    if not arr:
        return
    while l < r:
        m = l + (r - l) // 2

        if arr[m] == arr[m - 1]:
            l += 1
            continue
        if m + 1 < len(arr) - 1 and arr[m] < arr[m + 1]:
            l = m + 1
        else:
            r = m
    return arr[l] if l < len(arr) else arr[l - 1]