class Solution:
    def specialArray(self, nums: List[int]) -> int:
        for i in range(1,len(nums)+1):
            x = i
            newarr = []
            for j in range(0,len(nums)):
                if x <= nums[j]:
                    newarr.append(nums[j])
            if x == len(newarr):
                return x
        return -1