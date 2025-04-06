class Solution(object):
    def findMissingAndRepeatedValues(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: List[int]
        """
        n=len(grid)
        repeat=-1
        dics={}
        for i in range(n):
            for j in range(n):
                if grid[i][j] not in dics:
                    dics[grid[i][j]]=1
                else:
                    repeat=grid[i][j]
        for i in range(1,n**2+1):
            if i not in dics:
                missing=i
                break
        return [repeat,missing]
        