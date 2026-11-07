class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = list(s)
        cleaned_s =[]
        for index,char in enumerate(s):
            if char.lower() in list("qwertyuiopasdfghjklzxcvbnm1234567890"):
                # s.pop(index)
                cleaned_s.append(char)
        s_rev = cleaned_s[::-1]
        for index,char in enumerate(cleaned_s):
            cleaned_s[index] = char.lower()
        for index,char in enumerate(s_rev):
            s_rev[index] = char.lower()
        if s_rev == cleaned_s:
            return True
        else:
            return False
