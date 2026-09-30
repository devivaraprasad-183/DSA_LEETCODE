class Solution:
    def hammingWeight(self, n: int) -> int:
        count = 0
        while n!=0:
            ans = n&1
            if ans == 1:
                count +=1
            n = n >>1
        return count