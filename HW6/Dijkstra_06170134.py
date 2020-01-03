#!/usr/bin/env python
# coding: utf-8

# In[16]:


from collections import defaultdict 

class Graph(): 

    def __init__(self, vertices): 
        self.V = vertices 
        self.graph = [] 
        self.graph_matrix = [[0 for column in range(vertices)]  
                    for row in range(vertices)] 
        self.kg = [] #設list存變數
        
    def addEdge(self,u,v,w): 
        self.kg.append((u,v,w)) #新增變數到圖裡
        
    def Dijkstra(self, s):
        a={} #設一個字典去存放我要的
        a[str(s)]=0 #一開始先把0給丟進去
        b=[0] #設一個已經走過的
        c=0 #代表第幾個list

        for i in range(0,len(self.graph)-1): #點有幾個，迴圈走幾次
            tem=[]
            tem=tem+self.graph[c]
            while 0 in tem: #先把我要看的那一個list的0都刪除                
                tem.remove(0)     
                
            d=min(tem) #剩下最小的
            e=self.graph[c].index(d) #找到對應的點
            if e not in a:
                a[str(e)]=d
            
            while e in a: #找到還沒加進去中最小的                
                tem.remove(d) #將已經走過的路刪除(不考慮)
                d=min(tem) #在找下一個最小的
                e=self.graph[c].index(d) #再找他的位置 
            
            c=e #更新c
            b.append(e) #走過的點也加到走過的list    
            i+=1
        return a

    def Kruskal(self):
        a=set() #設一個set放所有的點
        for i in range(len(self.kg)): #用迴圈去找到所有的點
            a.add(self.kg[i][0]) #怕有什麼點找不到，要將前兩個值都要放進去
            a.add(self.kg[i][1]) #怕有什麼點找不到，要將前兩個值都要放進去
            i+=1
        b=set() #設一個set來確定已走過的
        c=[] #用來存放最後答案的
        weight=sorted(self.kg,key=lambda e:e[2],reverse=False) #用最後一個數字來排大小(小到大)
        while b != a and weight: #當點還沒全部連接到一起，且list裡有東西時
            e=weight.pop(0) #取出第一個數
            if e[0] in b and e[1] in b: #當前後兩個數字都在b裡，就表示已經連接過了
                continue #跳出這次的循環，去下一輪
            c.append(e) #如果還沒加進list，就加入
            b.update(e[:2]) #更新set，用e的前面兩個
        d={} #新增一個dict
        for i in range(len(c)): #設迴圈去跑
            x=str(c[i][0]) #前面的點
            y=str(c[i][1]) #後面的點
            z=x+"-"+y #助教要求的長像
            d[z]=c[i][2] #將點到點跟權數加到dict裡
            i+=1
        
        return d #回傳字典

