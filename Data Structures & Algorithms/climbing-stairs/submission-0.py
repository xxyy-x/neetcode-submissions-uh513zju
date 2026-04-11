class Solution:
    def climbStairs(self, n: int) -> int:
        count = 0

        # 2:x, 1: n-2x
        # total: n-x

        one, two = 1, 1
        for i in range(n-1):
            temp = one
            one = one + two
            two = temp

        return one
