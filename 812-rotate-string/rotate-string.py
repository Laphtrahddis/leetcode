class Solution(object):
    def rotateString(self, s, goal):
        """
        :type s: str
        :type goal: str
        :rtype: bool
        """
        s=list(s)
        goal=list(goal)
        if len(s)!=len(goal):
            return False
        offset=0
        count=0
        while offset<len(s):
            count=0
            for i in range(len(s)):
                if (s[i]==goal[(i+offset)%len(goal)]):
                    count+=1
                    if count==len(s):
                        return True
            if offset==len(s):
                return False
            offset+=1
        return False
                
