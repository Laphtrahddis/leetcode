class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        dict={}
        if len(s)!=len(t):
            return False
        for i in s:
            if i not in dict:
                dict[i]=1
            else:
                dict[i]+=1
        for i in t:
            if i not in dict:
                return False
            else:
                dict[i]-=1
                if dict[i]<0:
                    return False
        for i in dict.values():
            if i!=0:
                return False
        return True
        