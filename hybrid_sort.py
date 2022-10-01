#!/usr/bin/env python
# coding: utf-8

#global variable m_step that counts the steps of merge sort
m_step = 0

def merge_3_sort_threshold(array, p, q, threshold = 18):
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
    threshold: int
        the threshold which subarrays with length below it will be sorted by selection_sort
        has a default value of 18 because it is experimentally found to be the optimal threshold

    Returns
    -------
    array: a sorted Python list

    """
    #declare global variable
    global m_step
    #add one step each time the function is called
    m_step += 1
    #variables that store the end of first and second subarray
    r = 0
    s = 0
    #check for whether start index is smaller than end index
    if p < q:
        #divide the array into three parts
        r = p + (q-p)//3
        s = p + 2 * (q-p)//3
        #if subarrays have length less than threshold
        if r - p < threshold:
            selection_sort(array,p,r)
            selection_sort(array,r+1,s)
            selection_sort(array,s+1,q)
        else:
            #start recursion (divide the list)
            merge_3_sort_threshold(array,p,r,threshold)
            merge_3_sort_threshold(array,r+1,s,threshold)
            merge_3_sort_threshold(array,s+1,q,threshold)
        #start merge
        merge_3_step(array,p,r,s,q)
    return array
    
    
def merge_3_step(array, p, q, r, s):
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
    #use global variable m_step
    global m_step
    #sentinal value
    big = float('inf')
    #create three seperate list L, R and S
    L = array[p:q+1]
    R = array[q+1:r+1]
    S = array[r+1:s+1]
    #count step for slicing operation
    m_step += s-p
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
        #count steps for comparison and copy operations inside for loop
        m_step += 3

def selection_sort(A,p,q):
    """
    Sorts array[p] to array[q] in place with selection sort.

    Parameters
    ----------
    array : Python list or numpy array
    p : int
        index of array element to start sorting from
    q : int
        index of last array element to be sorted
        
    """
    #used to calculate steps
    steps = 0
    #store the value of jth number in the sequence in variable key
    key = 0
    
    for i in range(p, q):
        #set min index to current number
        minidx = i
        #find the min number on the right of current item
        for j in range(i+1, q+1):
            if A[j] < A[minidx]:
                minidx = j
            #count steps for inner for loop
            steps += 1
        #if found smaller number, swap current number and min number
        if minidx != i:
            key = A[i] 
            A[i] = A[minidx]
            A[minidx] = key
            #count steps for swap
            steps += 3
        #count steps for outer for loop
        steps += 1
    return steps

