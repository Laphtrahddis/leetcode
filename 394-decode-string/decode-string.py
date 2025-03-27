class Solution(object):
    def decodeString(self, s):
        """
        :type s: str
        :rtype: str
        """
        stack=[]
        slen=len(s)
        for i in range(slen):
            if s[i]!="]":
                stack.append(s[i])

            else:
                substr=""
                k=""
                while stack[-1]!="[":
                    substr=stack.pop()+substr
                stack.pop()
                while stack and stack[-1].isdigit():
                    k=stack.pop()+k
                stack.append(substr*int(k))
        return "".join(stack)