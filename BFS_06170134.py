#!/usr/bin/env python
# coding: utf-8

# In[9]:


from collections import defaultdict 
class Graph:

    def __init__(self): 
        self.graph = defaultdict(list) 

        
    def addEdge(self,u,v): 
        self.graph[u].append(v) 

        
    def BFS(self, s): 
        tem_list=[] #先創造一個空list，用作暫存
        tem_list.append(s)
        out_list=[] #創一個output list
        if len(out_list)==len(self.graph): #當全部走訪且存取完
            return out_list #回傳存取結果
        else:
            while len(tem_list)!=0: #這裡不能使用if，if"只"是判斷式，過了就過了，而while則是迴圈，如果沒有return或break就不會停止
                a=tem_list.pop(0) #走過之後，踢除，因為判斷式是看暫存list裡還有沒有值
                out_list.append(a) #要放進去
                for n in self.graph[a]: #進行for迴圈去把值一個一個放進list
                    if n not in out_list: #當點沒有在我要輸出的list裡
                        tem_list.append(n) #要放進去，之後再跑一次while迴圈會被剔除，不用擔心                        
                if len(out_list)==len(self.graph): #當全部走訪且存取完
                    return out_list #回傳存取結果 
     
    
    def DFS(self, s):
        tem_list=[] #先創造一個空list，用作暫存
        tem_list.append(s)
        out_list=[] #創一個output list
        if len(out_list)==len(self.graph): #當全部走訪且存取完
            return out_list #回傳存取結果
        else:
            while len(tem_list)!=0: #當tem_list裡有東西(這裡不能使用if，if"只"是判斷式，過了就過了，而while則是迴圈，如果沒有return或break就不會停止)
                a=tem_list.pop() #最後一個pop掉
                out_list.append(a) #放入out_list
                for n in self.graph[a]: #進行for迴圈去把值一個一個放進list
                    if n not in out_list: #當n還沒放入out_put裡 (當點沒有在我要輸出的list裡)                                               
                        tem_list.append(n) #要放進去，之後再跑一次while迴圈會被剔除，不用擔心
                if len(out_list)==len(self.graph): #當全部走訪且存取完
                    return out_list #回傳存取結果

