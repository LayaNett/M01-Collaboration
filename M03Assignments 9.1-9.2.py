#!/usr/bin/env python
# coding: utf-8

# In[6]:


def good():
    char_name = ["Harry","Ron","Hermione"]


# In[88]:


def get_odds():
    for count in range(1,10,2):
        yield (count)
        #Basics for a generator function
odds = get_odds()  #Makes count into a list to be counted
next(odds)
next(odds)# lets me skip to count 3, idk how to skip it without using next a bunch
print(next(odds))

