class Solution(object):
    def canPartition(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        nums_sum = sum(nums)
        if nums_sum % 2 != 0:
            return False
        n = len(nums)
        nums_sum = int(nums_sum / 2)
        dp = [[True if j == 0 else False for j in range(nums_sum + 1)] for i in range(n + 1)]
        for i in range(1, n + 1):
            for j in range(1, nums_sum + 1):
                if j - nums[i - 1] >= 0:
                    dp[i][j] = dp[i - 1][j] or dp[i - 1][j - nums[i - 1]]
                else:
                    dp[i][j] = dp[i - 1][j]
        return dp[n][nums_sum]


if __name__ == '__main__':
    print(Solution().canPartition([1, 5, 11, 5, 6, 6]))
