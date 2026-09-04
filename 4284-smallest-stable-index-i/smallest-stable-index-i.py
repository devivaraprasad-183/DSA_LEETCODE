class Solution:
    def firstStableIndex(self, nums: list[int], k: int) -> int:
        for i in range(0, len(nums)):
            left  = max(nums[:i+1])
            right = min(nums[i:])
            if abs(left - right) <= k:
                return i
        return -1
