class Solution:
    def minimumSumSubarray(self, nums: List[int], l: int, r: int) -> int:
        ans = float('inf')
        result = 0
        for i in range(0,len(nums)):
            arr = []
            for j in range(i,len(nums)):
                arr.append(nums[j])
                if  l<=len(arr) <= r:
                    result = sum(arr)
                    if result > 0:
                        ans = min(ans,result)
        if ans == float('inf'):
            return -1    
        return ans
