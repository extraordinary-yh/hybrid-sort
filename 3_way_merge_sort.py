#!/usr/bin/env python
# coding: utf-8


def merge_3_sort(array, p, q):
    """
    Sorts array[p] to array[q] in place.
    E.g., to sort an array A, we will run 
    `merge_3_sort(A, 0, len(A)-1)`.


    Parameters
    ----------
    array : Python list or numpy array
    p : int
        index of array element to start sorting from
    q : int
        index of last array element to be sorted

    Returns
    -------
    array: a sorted Python list

    """
    #end indexes of first and second array
    r = 0
    s = 0
    #check for base case (p == q)
    if p < q :
        #divide the array into three parts
        r = p + (q-p)//3
        s = p + 2 * (q-p)//3
        #start recursion (divide the list)
        merge_3_sort(array,p,r)
        merge_3_sort(array,r+1,s)
        merge_3_sort(array,s+1,q)
        #start merge
        merge_3(array,p,r,s,q)
    return array
    
def merge_3(array, p, q, r, s):
    """
    Merges 3 sorted sublists 
    (array[p] to array[q], array[q+1] to array[r] and array[r+1] to array[s]) 
    in place.
    
    Parameters
    ----------
    array : Python list or numpy array
    p : int
        index of first element of first sublist
    q : int
        index of last element of first sublist
    r : int
        index of last element of second sublist
    s : int
        index of last element of third sublist

    """
    #sentinal value
    big = float('inf')
    #create three seperate list L, R and S
    L = array[p:q+1]
    R = array[q+1:r+1]
    S = array[r+1:s+1]
    #put sentinal value at the end of list
    L.append(big)
    R.append(big)
    S.append(big)
    #initialize counters
    i = 0 
    j = 0
    z = 0
    #copy elements back to A
    for k in range(p, s+1):
        if L[i] == min(L[i], R[j], S[z]):
            array[k] = L[i]
            i += 1
        elif R[j] == min(L[i], R[j], S[z]):
            array[k] = R[j]
            j += 1
        else:
            array[k] = S[z]
            z += 1
 
