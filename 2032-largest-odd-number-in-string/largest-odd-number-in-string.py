class Solution(object):
    def largestOddNumber(self, num):
        """
        :type num: str
        :rtype: str
        """
        arr=str(num)
        for i in range(len(num)-1,-1,-1):
            if int(arr[i])%2==1:
                return num[0:i+1]
        return ""
        
        
        
        # max=-99999
        # arr=list(num)
        # for digit in arr:
        #     if digit>max and digit%2==1:
        #         max=digit
        # return digit
        