#!/usr/bin/env python
# coding: utf-8

# In[ ]:


class Solution:
    def isPalindrome(self, x: int) -> bool:
        if str(x)==str(x)[::-1]: #字串等於反著數過去
            return True #回傳True
        else: #不等於反著數
            return False #回傳False

