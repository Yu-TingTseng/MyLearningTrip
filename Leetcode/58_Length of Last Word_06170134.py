#!/usr/bin/env python
# coding: utf-8

# In[ ]:


class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        s = s.strip() #刪除最後的空白值
        a = s.split(" ") #從空白分開
        if len(a)==0: #沒有第二個字
            return 0 #就沒有東西
        else: 
            b = a[-1] #從最後一個字 
            return len(b) #最後回傳長度

