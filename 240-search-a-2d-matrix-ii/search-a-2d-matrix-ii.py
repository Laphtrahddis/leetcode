class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        m,n=len(matrix),len(matrix[0])
        #n=len(matrix[0])
        for i in range(m-1,-1,-1):
            if matrix[i][0]==target:
                return True
            elif matrix[i][0]>target:
                continue
            else:
                #binary search karo
                low,high=0,n-1
                #high=n-1
                while(low<=high):
                    mid=(low+high)//2
                    if matrix[i][mid]==target:
                        return True
                    elif matrix[i][mid]<target:
                        low=mid+1
                    else:
                        high=mid-1
        return False
        