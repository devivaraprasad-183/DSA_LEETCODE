class Solution:
    def longestPalindrome(self, s: str) -> int:
        freq = {}
        count = 0
        con = 0
        for i in s:
            if i not in freq:
                freq[i] = 1
            else:
                freq[i]+=1
        for keys,values in freq.items():
            if values %2 ==0:
                count+=values
            else:
                count+=values - 1

                con+=1    

        if con > 0:
            count+=1
        return count