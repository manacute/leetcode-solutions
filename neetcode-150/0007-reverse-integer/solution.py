import math
class Solution:
    def reverse(self, x: int) -> int:
        s = str(x)
        s = s[::-1]
        negative = False
        while s[0] == 0:
            s = s[1:]
        
        if s[-1] == "-":
            negative = True
            s = s[:-1]
        
        i = int(s)
        if i <= -math.pow(2, 31) or i >= math.pow(2, 31) - 1:
            return 0
        
        if negative:
            i = -i
        
        return i