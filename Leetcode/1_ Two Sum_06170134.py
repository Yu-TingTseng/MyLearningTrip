#!/usr/bin/env python
# coding: utf-8

# In[ ]:


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        a={} #先設一個字典
        for b,num in enumerate(nums): #利用enumerate列舉
            c=target-num #c是被扣除之後剩下的
            if c not in a: #如果C不能在裡面被找到
                a[num]=b # 字典裡就增加一個數，用作之後判斷
            else: #如果C能在裡面被找到
                return [a[c],b] #有找到就回傳c和b

