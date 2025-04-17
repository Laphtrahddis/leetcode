class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        prefix=0
        index=0
        while index<len(strs[0]):
            temp=strs[0][index]
            for i in strs:
                if index>=len(i) or i[index]!=temp:
                    return strs[0][:prefix]
            prefix+=1
            index+=1    
        return strs[0][:prefix]
        
        