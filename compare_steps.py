#!/usr/bin/env python
# coding: utf-8

# In[4]:


import random


def compute_avg2(n):
    """
    Compute and return average steos for three way merge sort with and without threshold for input size of n.
    This function will generate random arrays of size n and record the time and steps that each sorting algorithm took.
    This process will repeat 5 times to obtain the steps for average cases. 
                     
    Parameters
    ----------
    n: The size of random array

    Returns 
    -------
    mt_avgstep: average steps of merge sort with threshold for input size of n
    m_avgstep: average steps of merge sort without threshold for input size of n
    """
    global m_step
    
    #reset m_step
    m_step = 0
    
    #variabes that store average steps of each sorting algorithm
    m_avgstep, mt_avgstep = 0, 0

    #compute average steps to sort 100 random lists of length n
    for i in range(5):
        #random list to be sorted
        randomlist = []
        #generate random lists of length 10
        for j in range(0,n):
            #each item is within 0 to 100
            num = random.randint(0,100)
            randomlist.append(num)
        
        #the threshold is set to zero, which is equivelant as having all way merge sort
        merge_3_sort_threshold(randomlist,0,len(randomlist)-1,0)
        m_avgstep += m_step 
        
        #reset m_step
        m_step = 0
        
        #the threshold is set to 21
        merge_3_sort_threshold(randomlist,0,len(randomlist)-1,21)
        mt_avgstep += m_step
        
        #reset m_step
        m_step = 0
        
    m_avgstep = m_avgstep / 5
    #calculate average step by dividing the global variable m_step
    mt_avgstep = mt_avgstep / 5
    
    return m_avgstep,mt_avgstep
    
#variables to step took by each input size
m_avg, mt_avg = 0,0
#lists to store steps of different input size
m_steps = []
mt_steps = []
#lists to store input size
input_size = []

#record average steps taken for selection sort and merge sort for input size 0 to 30
for n in range(5000):
    input_size.append(n)
    m_avg, mt_avg = compute_avg2(n)
    #add to list
    m_steps.append(m_avg)
    mt_steps.append(mt_avg)
    
import numpy as np

plt.plot(input_size,m_steps,label = "Merge Sort without Threshold")
plt.plot(input_size,mt_steps,label = "Merge Sort with Threshold")
#plotting n*logn
x = np.array(input_size[1:])
nlogn = np.multiply(np.log(x)/np.log(3),x)
plt.plot(x, nlogn, "--", label = "n*log_3(n)")
plt.ylabel("Average Steps")
plt.xlabel("Input Size")
plt.title("Average Steps taken by merge sort with and without threshold")
plt.legend()
plt.show()


# In[ ]:




