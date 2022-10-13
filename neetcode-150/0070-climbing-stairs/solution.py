class Solution:
    def climbStairs(self, n: int) -> int:
        if n < 3:
            return n
        
        x = 1
        y = 2
        for i in range(2, n):
            y += x
            x = y - x
            
        return y