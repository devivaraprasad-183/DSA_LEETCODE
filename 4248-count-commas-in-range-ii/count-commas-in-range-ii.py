class Solution:
    def countCommas(self, n: int) -> int:

        count = 0

        if n < 1000:
            return 0

        elif n < 1000000:
            count = n - 999

        elif n < 1000000000:
            count = 999000
            count += 2 * (n - 999999)

        elif n < 1000000000000:
            count = 1998999000
            count += 3 * (n - 999999999)

        elif n < 1000000000000000:
            count = 2998998999000
            count += 4 * (n - 999999999999)

        else:
            count = 3998998998999000
            count += 5 * (n - 999999999999999)

        return count