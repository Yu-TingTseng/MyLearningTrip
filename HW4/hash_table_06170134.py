#!/usr/bin/env python
# coding: utf-8

# In[1]:


from Crypto.Hash import MD5
class ListNode:
    def __init__(self, val):
        self.val = val #建立節點
        self.next = None

class MyHashSet:
    def __init__(self, capacity=5):
        self.capacity = capacity #建立空間
        self.data = [None] * capacity

    def add(self, key):
        
        h = MD5.new() #使用MD5加密
        h.update(key.encode("utf8")) #指定編碼，使用utf8
        b=int(h.hexdigest(),16) #將16進位轉10進位
        index=b%self.capacity #取除capacity的餘數，希望index可以隨著capacity可大可小
        
        if self.data[index] == None: #如果index還未被建立
            self.data[index]=ListNode(key) #那就直接把key給放進去
            return 
        else: #如果index已被建立
            self.data[index].next=ListNode(key) #不可用append加在後面
            return 
        
    def contains(self, key):
        
        h = MD5.new()
        h.update(key.encode("utf8"))
        b=int(h.hexdigest(),16) 
        index=b%self.capacity 
        
        if self.data[index] == None: #如果index還未被建立
            return False #代表根本不會有key的存在，直接回傳False
        elif self.data[index] and key.find: #如果index已建立，且key存在(.find用法是網路上查的，已附在參考資料)
            return True #回傳True
        else: #index已建立，但key不存在
            return False #回傳False
    
    def remove(self, key):
        h = MD5.new()
        h.update(key.encode("utf8")) 
        b=int(h.hexdigest(),16) 
        index=b%self.capacity 
        
        if self.data[index] == None: #如果index還未被建立
            return #代表根本不會有key的存在，直接回傳
        elif self.data[index] and key.find: #index已建立，且key存在
            if key==self.data[index] and self.next == None: #index裡只有key一個值
                self.data[index]==None #直接將它變為無
                return
            else: #index裡有不只一個key
                self.data[index]==self.data[index].next #值變成下一個
                self.data[index].next==None #而後一個位置變None
                return
        else: #index已建立，但key不存在
            return #沒有key的存在，直接回傳

