class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        r=0
        l=0
        min_len = float('inf')
        sub = 0
        while r < len(nums):
            sub+=nums[r]
            if sub >= target:
                while sub >= target:
                    min_len = min(min_len,r-l+1)
                    sub-=nums[l]
                    l+=1
            r+=1
        if min_len == float('inf'):
            return 0
        return min_len