#!/usr/bin/env python
# coding: utf-8

# In[ ]:


class Solution:
    def reverse(self, x: int) -> int:
        a=str(x)[::-1] #設一個a存放字串反過來
        if x<-0: #字串小於0
            a=a.strip("-") #要將減號去除
            if int(a)>2**31-1: #限制範圍
                return  0 #超出回傳0
            else:
                return -int(a) #沒超出就把減號加回去然後回傳           
        else: #字串大於0
            if int(a)>2**31-1: #限制範圍
                return 0 #超出回傳0
            else:
                return int(a) #沒超出就直接回傳 

