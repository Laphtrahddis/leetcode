class Solution(object):
    def maxDepth(self, s):
        """
        :type s: str
        :rtype: int
        """
        queue=deque()
        len_=0
        maxlen=0
        for i in s:
            if i=='(':
                queue.append(i)
                len_+=1
            elif i==')':
                queue.pop()
                len_-=1
            else:
                continue
            maxlen=max(maxlen,len_)
        return maxlen

        
        