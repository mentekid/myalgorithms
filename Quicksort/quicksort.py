"""Implementation of QuickSort, based on the CLRS algorithm
Author: Yannis Mentekidis
Date: August 12, 2015
"""

def Partition(A, p, r):
    """ Rearranges A into elements smaller than the pivot (left)
    and larger than the pivot (right) """
    x = A[r] #last element of array
    i = p - 1 #index before first element
    for j in range(p, r):
        if A[j] <= x:
            i += 1
            (A[i], A[j]) = (A[j], A[i]) #swap
    (A[i+1], A[r]) = (A[r], A[i+1]) #move pivot
    return i+1


def QuickSort(A, p = 0, r = None):
    """ Sorts data in-place (O(N) space) and in O(NlogN) time

    Testing:
    >>> A = [2, 8, 7, 1, 3, 5, 6, 4] #integers test
    >>> QuickSort(A)
    >>> A
    [1, 2, 3, 4, 5, 6, 7, 8]

    >>> B = ['z', 'g', 'a', 'f', 'c', ' ', 'd'] #characters test
    >>> QuickSort(B)
    >>> B
    [' ', 'a', 'c', 'd', 'f', 'g', 'z']
    """
    if r == None: #default: r is the index of last point in list
        r = len(A) - 1

    if p < r:
        q = Partition(A, p, r)
        QuickSort(A, p, q-1)
        QuickSort(A, q+1, r)

    return


def main():
    pass
if __name__ == "__main__":
    main()
