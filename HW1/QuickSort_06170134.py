#!/usr/bin/env python
# coding: utf-8

# In[ ]:


def quicksort(list):
        while len(list)<=1:#當陣列裡的數值只有一個或為空陣列，則無需排列，直接回傳
            return list
    
        else:
            sm_list=[]
            pv_list=[]
            bg_list=[]
            pv=list[len(list)//2-1] #設陣列裡的中間值為pivot
            
            for a in list:
                if a < pv: #比pivot小的數
                    sm_list.append(a)
                elif a > pv: #比pivot大的數
                    bg_list.append(a)
                else:   #跟pivot一樣大的數
                    pv_list.append(a)
                    
        sm_list=quicksort(sm_list)
        bg_list=quicksort(bg_list)
        #不用加pv_list=quicksort(pv_list)?pv_list本來就是最後才比較裡面已經都排好了，但為什麼加了會有錯
        return sm_list + pv_list + bg_list

