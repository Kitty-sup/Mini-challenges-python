#!/usr/bin/env python
# coding: utf-8

# In[4]:


"""Write a Python function that takes a string as input and returns the most frequent character (ignoring case and spaces).

The function should be case-insensitive (i.e., 'A' and 'a' are treated the same).

Spaces should be ignored when counting.

If multiple characters have the same highest frequency, return any one of them."""

def most_freq_char(s):
    s=s.lower().replace(" ","")
    freq={}

    for char in s:
        if char in freq:
            freq[char]+=1
        else:
            freq[char]=1
        max_char = max(freq,key=freq.get)
    return max_char
s=input("Enter String: ")
most_freq_char(s)


# In[ ]:




