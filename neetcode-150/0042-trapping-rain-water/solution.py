class Solution:
    def trap(self, height: List[int]) -> int:
        l, r = 0, len(height) - 1
        max_left, max_right = height[0], height[-1]
        water = 0
        
        while l < r:
            if max_left <= max_right:
                height_diff = max_left - height[l]
                water += height_diff
                    
                l += 1
                if height[l] > max_left:
                    max_left = height[l]
                    
            else:
                height_diff = max_right - height[r]
                water += height_diff
                    
                r -= 1 
                if height[r] > max_right:
                    max_right = height[r]
        
        return water