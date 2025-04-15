def isPeak(i,max_,mat):
    if i-1>=0 and i+1<len(mat):
        if mat[i-1][max_]<mat[i][max_] and mat[i+1][max_]<mat[i][max_]:
            return True
        else:
            return False
    else:
        if i-1<0:
            if mat[i+1][max_]<mat[i][max_]:
                return True
            else:
                return False
        if i+1>=len(mat):
            if mat[i-1][max_]<mat[i][max_]:
                return True
            else:
                return False


class Solution(object):
    def findPeakGrid(self, mat):
        """
        :type mat: List[List[int]]
        :rtype: List[int]
        """
        if len(mat)==1 and len(mat[0])==1:
            return (0,0)
        m=len(mat)
        n=len(mat[0])
        if m==1:
            return (0,mat[0].index(max(mat[0])))
        # if n==1:
        #     return (mat.index(max(mat[0])),0)
        for i in range(m):
            max_=mat[i].index(max(mat[i]))
            if isPeak(i,max_,mat) :
                return (i,max_)

            