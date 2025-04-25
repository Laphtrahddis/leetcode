class Solution(object):
    def beautySum(self, s):
        """
        :type s: str
        :rtype: int
        """
        total=0
        for i in range(len(s)):
            freq=[0]*26
            for j in range(i,len(s)):
                index=ord(s[j])-ord('a')
                freq[index]+=1
                min_freq=9999
                max_freq=0
                for k in freq:
                    if k>0:
                        max_freq=max(max_freq,k)
                        min_freq=min(min_freq,k)
                beauty=max_freq-min_freq
                total+=beauty
        return total
