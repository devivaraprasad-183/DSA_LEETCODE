class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        r = 0
        l = 0
        ans = 1
        count = 0
        if k < 2:
            return 0
        while r < len(nums):
            ans *= nums[r]
            while ans >= k:
                ans = ans//nums[l]
                l+=1
            if ans < k :
                count +=r-l+1
            r+=1
        return count