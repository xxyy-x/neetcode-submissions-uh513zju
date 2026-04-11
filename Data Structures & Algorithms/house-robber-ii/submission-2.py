class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]

        if len(nums) == 2:
            return max(nums[1], nums[0])

        df = [0] * len(nums)
        df[0] = nums[0]
        df[1] = max(nums[1], df[0])
        for i in range(2,len(nums) - 1):
            df[i] = max(df[i-1], df[i-2] + nums[i])
        
        dp = [0] * len(nums)
        dp[1] = nums[1]
        dp[2] = max(nums[2], dp[1])
        for j in range(3, len(nums)):
            dp[j] = max(dp[j-1], dp[j-2] + nums[j])

        return max(df[len(nums)-2], dp[len(nums) - 1])







# either choose first or last