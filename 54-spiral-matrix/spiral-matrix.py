class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        left=0
        right=len(matrix[0])
        top=0
        bottom=len(matrix)
        arr=[]
        while top<bottom and left<right:
            for i in range(left,right):
                arr.append(matrix[top][i])
            top+=1
            for i in range(top,bottom):
                arr.append(matrix[i][right-1])
            right-=1
            if top >= bottom or right <= left: 
                break
            for i in range(right-1,left-1,-1):
                arr.append(matrix[bottom-1][i])
            bottom-=1
            for i in range(bottom-1,top-1,-1):
                arr.append(matrix[i][left])
            left+=1
        return arr