class Solution:
    def countBits(self, n: int) -> List[int]:
        if n == 0:
            return [0]
        
        res = [0]
        idx = 0
        target = 1
        
        for _ in range(n):
            res.append(res[idx] + 1)
            idx += 1
            if idx == target:
                idx = 0
                target *= 2
            
        return res