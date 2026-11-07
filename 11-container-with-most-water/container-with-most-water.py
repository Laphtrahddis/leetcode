class Solution:
    def maxArea(self, height: list[int]) -> int:
        maxAR = 0
        i = 0 
        j = len(height) - 1
        while i<j:
            minheight = height[i] if height[i]<height[j] else height[j]
            area = minheight * (j-i)
            if area > maxAR:
                maxAR = area
            if height[i] < height[j]:
                i+=1
            else:
                j-=1
        return maxAR
