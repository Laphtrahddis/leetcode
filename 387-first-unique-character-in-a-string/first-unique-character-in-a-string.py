class Solution:
    def firstUniqChar(self, s: str) -> int:
        seen = []
        for index, char in enumerate(s):
            if char in seen:
                continue
            else:
                if char not in s[index+1:]:
                    return index
                else:
                    seen.append(char)
        return -1
