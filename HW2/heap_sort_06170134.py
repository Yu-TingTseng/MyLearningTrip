#!/usr/bin/env python
# coding: utf-8

# In[ ]:


class Solution(object):
    def heap_sort(self,nums):
        while len(nums)<=1:
            return nums
        for n in range (0,len(nums),1):
            l=n*2
            r=n*2+1
            if 

