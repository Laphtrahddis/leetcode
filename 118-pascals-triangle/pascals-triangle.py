class Solution(object):
    def genrow(self,n):
        arr=[]
        arr.append(1)
        ans=1
        for i in range(1,n):
            ans=ans*(n-i)
            ans=ans/i
            arr.append(ans)
        return arr
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        ansarr=[]
        for i in range(1,numRows+1):
            ansarr.append(self.genrow(i))
        return ansarr
        