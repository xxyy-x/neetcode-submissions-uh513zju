class Solution:
    def rob(self, nums: List[int]) -> int:
        
        if len(nums) == 0:
            return None
        if len(nums) == 1:
            return nums[0]
        dp = [0] * len(nums)
        dp[0] = nums[0]
        dp[1] = max(dp[0], nums[1])
        
        for i in range(2, len(nums)):
            dp[i] = max(dp[i-1], dp[i-2]+nums[i])
        
        return dp[len(nums) - 1]


# dp[i] = max()
#    i = [0,1,2,3,4]
# nums = [5,2,3,4,4]