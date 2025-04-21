from operator import itemgetter

class Solution(object):
    def frequencySort(self, s):
        """
        :type s: str
        :rtype: str
        """
        dict={}
        for i in s:
            if i not in dict:
                dict[i]=1
            else:
                dict[i]+=1
        sorted_items = sorted(dict.items(), key=itemgetter(1), reverse=True)
        l=[]
        for key,item in sorted_items:
            for i in range(item):
                l.append(key)
        return "".join(l)
            
        