class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        r = 0
        l =  0
        length = 0
        nums1 = []
        zero_count = 0
        while r < len(nums):
            nums1.append(nums[r])
            if nums[r] == 0:
                zero_count +=1
            while zero_count > k: 
                nums1.remove(nums[l])
                if nums[l]==0:
                    zero_count-=1
                l+=1

            length = max(length,r-l+1)
            r+=1
        return length