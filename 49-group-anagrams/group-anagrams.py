class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        dictn = {}
        for word in strs:
            sortedword = "".join(sorted(word))
            if sortedword in dictn:
                ValueArray = dictn.get(sortedword)
                ValueArray.append(word)
                dictn[sortedword] = ValueArray
            else:
                dictn[sortedword] = [word]
        Returnarr = []
        for key in dictn:
            Returnarr.append(dictn.get(key))
        return Returnarr
