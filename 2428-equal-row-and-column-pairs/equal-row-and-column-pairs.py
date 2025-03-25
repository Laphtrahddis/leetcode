class Solution(object):
    def equalPairs(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        n=len(grid)
        sbray=[]
        count=0
        for i in range(n):
            for j in range(n):
                sbray.append(grid[j][i])
            for k in range(n):
                if sbray==grid[k]:
                    count+=1
            sbray=[]
        return count