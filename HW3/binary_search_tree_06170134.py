#!/usr/bin/env python
# coding: utf-8

# In[ ]:


class TreeNode(object):
    def __init__(self,x):
        self.val = x
        self.left = None
        self.right = None
        """
        :type val: int
        :type left: TreeNode or None
        :type right: TreeNode or None
        """    
class Solution(object):
    def insert(self, root, val):
        """
        :type root: TreeNode
        :type val: int
        :rtype: TreeNode(inserted node)
        """
        if root.val == None: 
            root=TreeNode(val)
            return root 
        
        else: 
            if val > root.val:
                if root.right==None: 
                    root.right=TreeNode(val) 
                    return root.right 
                
                else:
                    return Solution().insert(root.right,val) 
 
            elif val<= root.val:
                if root.left==None: 
                    root.left=TreeNode(val) 
                    return root.left
                
                else:                    
                    return Solution().insert(root.left,val)
                
                
    def delete(self, root, target):
        """
        :type root: TreeNode
        :type target: int
        :rtype: TreeNode(the root of new completed binary search tree) (cannot search())
        """
        if Solution().search(root,target)==None:
            return None
        else:
            target =root
            if root.left==None and root.right==None:
                return root==None
            elif root.left==None and root.right:
                root.right=a
                root=b
                root.right=b
                root=a
                return root.right==None
            elif root.right==None and root.left:
                root.left=a
                root=b
                root.left=b
                root=a
                return root.left==None
            else:
                return root==None
        
        
    def search(self, root, target):
        """
        :type root: TreeNode
        :type target: int
        :rtype: TreeNode(searched node)
        """
        if root.val == None: 
            return None
        
        else: 
            if target > root.val: 
                if root.right==None:
                    return None
                
                else:
                    return Solution().search(root.right,target)
                
            elif target< root.val: 
                if root.left==None: 
                    return None
                
                else:                    
                    return Solution().search(root.left,target)
                
            else:
                return root 
            
            
    def modify(self, root, target, new_val):
        """
        :type root: TreeNode
        :type target: int
        :type new_val: int
        :rtype:TreeNode(the root of new completed binary search tree) (cannot search())
        """
        if Solution().search(root,target)==None:

            return 
        else:
            return Solution().delete(root,target)

