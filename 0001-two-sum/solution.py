class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num_idx = {nums[i] : i for i in range(len(nums))}
            
        for i in range(len(nums) - 1):
            x = target - nums[i]
            if x in num_idx:
                j = num_idx[x]
                if i != j:
                    return [i, j]