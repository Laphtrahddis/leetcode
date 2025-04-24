# def isPalindrome(s):
#     if s==s[::-1]:
#         return True
#     else: return False


class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        if len(s)<1:
            return ""
        elif len(s)==1:
            return s
        else:
            res=""
            reslen=0
            for i in range(len(s)):
                #ODD:
                l,r=i,i
                while (l>=0 and r<len(s)) and s[l]==s[r]:
                    if r-l+1>reslen:
                        res=s[l:r+1]
                        reslen=r-l+1
                    l-=1
                    r+=1
                #EVEN:
                l,r=i,i+1
                while l>=0 and r<len(s) and s[l]==s[r]:
                    if r-l+1>reslen:
                        res=s[l:r+1]
                        reslen=r-l+1
                    l-=1
                    r+=1
            return res

        # if len(s)==1:
        #     return s
        # maxlen=0
        # start=0
        # end=0
        # for i in range(len(s)-1):
        #     for j in range(i+1,len(s),1):
        #         val=isPalindrome(s[i:j+1])
        #         if val==True:
        #             maxlen=max(maxlen,j-i)
        #             if maxlen==j-i:
        #                 start=i
        #                 end=j
        #         else:
        #             continue
        # return s[start:end+1]

        