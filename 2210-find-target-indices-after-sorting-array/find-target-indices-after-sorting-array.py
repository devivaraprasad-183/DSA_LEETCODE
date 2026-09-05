class Solution:
    def targetIndices(self, nums: List[int], target: int) -> List[int]:
        nums.sort()
        ans = []
        for i in  range(0,len(nums)):
            if nums[i] == target:
                ans.append(i)
        return ans