class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:
        if len(nums) < 1:
            return 0
        nam = sorted(set(nums))
        count = 1
        counts = 1
        
        for i in range(0,len(nam)-1):
            if nam[i+1] == nam[i]+1:
                count+=1
                counts = max(count,counts)
            else:
                count = 1
        return counts