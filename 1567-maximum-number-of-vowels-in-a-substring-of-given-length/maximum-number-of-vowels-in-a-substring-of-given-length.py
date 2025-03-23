class Solution(object):
    def maxVowels(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        # for i in range(k):
        #     if s[i] in "aeiou":
        #         count+=1
        # maxcount=0
        # n=len(s)
        # # for i in range()
        # for i in range(n-k+1):
        #     count=0
        #     for j in range(i,i+k):
        #         if s[j] in "aeiou":
        #             count+=1
        #     maxcount=max(maxcount,count)
        # return maxcount
        vowels=set("aeiou")
        count=sum(1 for i in range(k) if s[i] in vowels)
        maxcount=count
        for i in range(k,len(s)):
            if s[i-k] in vowels:
                count-=1
            if s[i] in vowels:
                count+=1
            maxcount=max(maxcount,count)
        return maxcount
        