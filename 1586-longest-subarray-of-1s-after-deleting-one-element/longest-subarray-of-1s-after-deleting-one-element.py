class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        r=0
        l=0
        zero = 0
        long_len = 0
        while r < len(nums):
            if nums[r]==0:
                zero+=1
            while zero > 1:
                if nums[l]== 0:
                    zero-=1
                l+=1
            long_len = max(long_len,r-l+1)
            r+=1
        return long_len-1