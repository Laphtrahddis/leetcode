class Solution(object):
    def largestAltitude(self, gain):
        """
        :type gain: List[int]
        :rtype: int
        """
        alt=0
        maxalt=0
        for i in gain:
            alt+=i
            maxalt=max(maxalt,alt)
        return maxalt