### LeetCode
##### 1_ Two Sum
class  Solution :
    def  twoSum ( self , nums : List[ int ], target : int ) -> List[ int ]:
        a = {} #先設一個字典
        for b,num in  enumerate (nums): #利用enumerate列舉
            c = target - num # c是被扣除之後剩下的
            if c not  in a: #如果C不能在裡面被找到
                a[num] = b #字典裡就增加一個數，用作之後判斷
            else : #如果C能在裡面被找到
                return [a[c],b] #有找到就回傳c和b
                
##### 7_ Reverse Integer
class  Solution :
    def  reverse ( self , x : int ) -> int :
        a = str (x)[:: - 1 ] #設一個a存放字串反過來
        if x < - 0 : #字串小於0
            a = a.strip( " - " ) #要將減號去除
            if  int (a) > 2 ** 31 - 1 : #限制範圍
                return   0  #超出回傳0
            else :
                return  - int (a) #沒超出就把減號加回去然後回傳           
        else : #字串大於0
            if  int (a) > 2 ** 31 - 1 : #限制範圍
                return  0  #超出回傳0
            else :
                return  int (a) #沒超出就直接回傳
##### 9_ Palindrome Number
class  Solution :
    def  isPalindrome ( self , x : int ) -> bool :
        if  str (x) == str (x)[:: - 1 ]: #字串等於反著數過去
            return  True  #回傳True
        else : #不等於反著數
            return  False  #回傳False
##### 14_ Longest Common Prefix
class  Solution :
    def  longestCommonPrefix ( self , strs : List[ str ]) -> str :
        a =  " "  #先設定一個空的字串，用來放相同的字
        for i in [ * zip ( * strs)]: # 米字號是用來解壓縮，並不是一般常見的乘的用法
            if  len ( set (i)) ==  1 : #集合不含相同的值
                a += i[ 0 ] #重複
            else : #有相同的值
                break  #跳離
        return a #回傳已修改字串
##### 58_Length of Last Word
class  Solution :
    def  lengthOfLastWord ( self , s : str ) -> int :
        s = s.strip() #刪除最後的空白值
        a = s.split( "  " ) #從空白分開
        if  len (a) == 0 : #沒有第二個字
            return  0  #就沒有東西
        else :
            b = a[ - 1 ] #從最後一個字
            return  len (b) #最後回傳長度
