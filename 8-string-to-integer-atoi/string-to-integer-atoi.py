class Solution(object):
    def myAtoi(self, s):
        """
        :type s: str
        :rtype: int
        """
        sign=1
        str=''
        i=0
        if len(s)==0:
            return 0
        while(i<len(s) and s[i]==' '):
            i+=1
        if i<len(s) and s[i]=='-':
            sign=-1
            i+=1
        elif i<len(s) and s[i]=='+':
            i+=1
        while(i<len(s) and s[i] in ['0','1','2','3','4','5','6','7','8','9']):
            str=str+s[i]
            i+=1
        if str=='':
            return 0
        result=sign*int(str)
        INT_MIN, INT_MAX = -2**31, 2**31 - 1
        return max(INT_MIN, min(INT_MAX, result))

        
        