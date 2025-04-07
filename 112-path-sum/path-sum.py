# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def dfs(self, node, targetSum,sum_):
        if not node:
            return 0
        if not node.left and not node.right:
            if sum_+node.val==targetSum:
                self.count+=1
        
        self.dfs(node.left,targetSum,sum_+node.val)
        self.dfs(node.right,targetSum,sum_+node.val)
        
        
    
    def hasPathSum(self, root, targetSum):
        """
        :type root: Optional[TreeNode]
        :type targetSum: int
        :rtype: int
        """
        self.count=0
        if not root:
            return False
        sum_=root.val
        if not root.left and not root.right and sum_==targetSum:
            return True
        self.dfs(root.left,targetSum,sum_)
        self.dfs(root.right,targetSum,sum_)
        return bool(self.count)
        