class Solution:
    def minimumSumSubarray(self, nums: List[int], l: int, r: int) -> int:
        ans = float('inf')
        result = 0

        for k in range(l, r+1):
            arr = []
            for j in range(len(nums)-k+1):
                result = sum(nums[j:j+k])
                if  result > 0:
                    ans = min(ans, result)
                    result = 0
        if ans == float('inf'):
            return -1    
        return ans
