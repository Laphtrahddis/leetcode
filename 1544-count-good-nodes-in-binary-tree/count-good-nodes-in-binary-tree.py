# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
#
class Solution(object):
    
    def dfs(self,node,max_):
        if not node:
            return
        if node.val>=max_:
            self.count+=1
            max_=node.val
        lft=node.left
        rgt=node.right
        self.dfs(lft,max_)
        self.dfs(rgt,max_)
    def goodNodes(self, root):
        self.count=1
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        lft=root.left
        rgt=root.right
        max_=root.val
        self.dfs(lft,max_)
        self.dfs(rgt,max_)
        return self.count
        
        