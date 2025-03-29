class Solution(object):
    def predictPartyVictory(self, senate):
        """
        :type senate: str
        :rtype: str
        """
        senlist=list(senate)
        R,D=deque(),deque()
        for i,name in enumerate(senlist):
            if name=='R':
                R.append(i)
            else:
                D.append(i)
        while D and R:
            Rpop=R.popleft()
            Dpop=D.popleft()
            if Dpop<Rpop:
                D.append(Dpop+len(senlist))
            else:
                R.append(Rpop+len(senlist))
        
        return "Radiant" if R else "Dire"