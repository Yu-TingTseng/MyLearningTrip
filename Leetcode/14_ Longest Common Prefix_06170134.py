#!/usr/bin/env python
# coding: utf-8

# In[ ]:


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        a = "" #先設定一個空的字串，用來放相同的字
        for i in [*zip(*strs)]: # * 是用來解壓縮，並不是一般常見的乘的用法
            if len(set(i)) == 1: #集合不含相同的值
                a += i[0] #重複
            else: #有相同的值
                break #跳離
        return a #回傳已修改字串

