#!/usr/bin/env python
# coding: utf-8

import time

def compute_avg3(n):
    """
    Compute and return average runtime for three way merge sort with and without threshold for input size of n.
    This function will generate random arrays of size n and record the time and steps that each sorting algorithm took.
    This process will repeat 5 times and average run time and steps of 5 attempts will be computed.
                     
    Parameters
    ----------
    n: The size of random array

    Returns 
    -------
    mt_avgstep: average runtime of merge sort with threshold for input size of n
    m_avgstep: average runtime of merge sort without threshold for input size of n
    """

    #variabes that store average time of each sorting algorithm
    m_avgtime = 0
    mt_avgtime = 0

    #compute average runtimes to sort 5 random lists of length n
    for i in range(5):
        #random list to be sorted
        randomlist = []
        #generate random lists of length 10
        for j in range(0,n):
            #each item is within 0 to 100
            num = random.randint(0,100)
            randomlist.append(num)
        
        #start timing
        start1 = time.time()
        #the threshold is set to zero, which is equivelant as having all way merge sort
        merge_3_sort_threshold(randomlist,0,len(randomlist)-1,0)
        end1 = time.time()
        m_avgtime += end1 - start1
        
        #the threshold is set to 21
        start2 = time.time()
        merge_3_sort_threshold(randomlist,0,len(randomlist)-1,21)
        end2 = time.time()
        mt_avgtime += end2 - start2

    #calculate average step by dividing the sum of runtime
    m_avgtime= m_avgtime / 5
    mt_avgtime= mt_avgtime / 5
    
    return m_avgtime,mt_avgtime
    
#variables to step took by each input size
m_avgtime, mt_avgtime = 0,0
#lists to store steps of different input size
m_time = []
mt_time = []

#record average steps taken for selection sort and merge sort for input size 0 to 30
for n in range(5000):
    m_avgtime, mt_avgtime = compute_avg3(n)
    #add to list
    m_time.append(m_avgtime)
    mt_time.append(mt_avgtime)

