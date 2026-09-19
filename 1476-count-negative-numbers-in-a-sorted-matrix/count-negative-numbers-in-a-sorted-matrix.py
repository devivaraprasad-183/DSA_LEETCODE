class Solution:
    def countNegatives(self, grid: list[list[int]]) -> int:
        count = 0
        for i in grid:
            left = 0
            right = len(i) - 1
            ans = len(i)
            while left <= right:
                mid = (left+right)//2
                if i[mid] < 0:
                    ans= mid
                    right = mid - 1
                elif i[mid] >= 0:
                    left = mid + 1
            final = len(i) - ans
            count += final
        return count 