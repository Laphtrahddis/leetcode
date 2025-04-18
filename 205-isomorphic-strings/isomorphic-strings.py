class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        # """
        # s=list(s)
        # t=list(t)
        # if len(s)!=len(t): return False
        # prevs=s[0]
        # prevt=t[0]
        dict={}
        for i in range(len(s)):
            if s[i] not in dict:
                if t[i] not in dict.values():
                    dict[s[i]]=t[i]
                else:
                    return False
            else:
                if dict[s[i]]!=t[i]:
                    return False
        return True
        