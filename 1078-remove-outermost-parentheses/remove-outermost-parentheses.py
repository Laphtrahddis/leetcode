class Solution(object):
    def removeOuterParentheses(self, s):
        stack=deque()
        ans=[]
        for i in s:
            if len(stack)==0:
                stack.append(i)
                continue
            if i!=stack[-1] and len(stack)==1:
                stack.pop()
                continue
            if i!=stack[-1]:
                ans.append(i)
                stack.pop()
                continue
            stack.append(i)
            ans.append(i)
        return ''.join(ans)
        
        
        
        
        
        
        # """
        # :type s: str
        # :rtype: str
        # """
        # arr=list(s)
        # arr.pop(-1)
        # arr.pop(0)
        # index=[]
        # flag=-1
        # for i in range(len(arr)):
        #     if flag==1:
        #         flag=-1
        #         continue
        #     if i == ")":
        #         if arr[i+1]=="(":
        #             flag=1
        #             continue                    
        #         else:
        #             index.append(arr[i])
        #     else:
        #         index.append(arr[i])
        # return ''.join(index)
        
        
        
        