class Solution(object):
    def closeStrings(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: bool
        """
        # flag=0
        # if len(word1)!=len(word2):
        #     return False
        # for i in range (len(word1)):
        #     if word1[i]!=word2[i]:
        #         flag+=1
        # if flag==1:
        #     return True
        # dict1={}
        # dict2={}
        # for i in word1:
        #     if i not in dict1:
        #         dict1[i]=1
        #     else:
        #         dict1[i]+=1
        # for i in word2:
        #     if i not in dict2:
        #         dict2[i]=1
        #     else:
        #         dict2[i]+=1
        # j=0
        # while j<len(word2):
        #     for i in range(len(word1)):
        #         if word1[i]!=word2[i]:
        #             dict1[word1[i]]-=1
        #             dict2[word2[i]]-=1
        #             if dict1[word1[i]]!=dict2[word2[i]]:
        #                 return False
        #     j+=1
        # return True
        word1set=set(word1)
        word2set=set(word2)
        for i in word1set:
            if i not in word2set:
                return False
        for i in word2set:
            if i not in word1set:
                return False
        dict1={}
        dict2={}
        for i in word1:
            if i not in dict1:
                dict1[i]=1
            else:
                dict1[i]+=1
        for i in word2:
            if i not in dict2:
                dict2[i]=1
            else:
                dict2[i]+=1
            word1arr=[]
            word2arr=[]
        for key,value in dict1.items():
            word1arr.append(value)
        for key,value in dict2.items():
            word2arr.append(value)
        word1arr.sort()
        word2arr.sort()
        if word1arr==word2arr:
            return True
        else:
            return False
            
        
        