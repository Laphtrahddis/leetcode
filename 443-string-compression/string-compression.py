class Solution:
    def compress(self, chars: list[str]) -> int:
        written = 0
        i = 0
        # for i, char in enumerate(chars):
        while i < len(chars):
            char = chars[i]
            length = 1
            chars[written] = char
            written += 1
            jumpTo = i+1
            for j in range(i+1,len(chars)):
                if chars[i] == chars[j]:
                    length+=1
                    if j == len(chars)-1:
                        jumpTo = j+1
                else:
                    jumpTo = j
                    break
            if length == 1:
                i = jumpTo
                continue
            else:
                for k in range(0,len(str(length))):
                    chars[written] = str(length)[k]
                    written += 1
            i = jumpTo
        return written
