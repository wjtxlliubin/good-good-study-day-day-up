class Solution:
    def change(self, amount: int, coins: list) -> int:
        dp = [[ 1 if j==0 else 0 for j in range(amount+1)] for i in range(len(coins)+1)]
        print(dp)
        for i in range(1,len(coins)+1):
            for j in range(1,amount+1):
                if j - coins[i-1]>=0:
                    dp[i][j] = dp[i-1][j]+dp[i][j - coins[i-1]]
                else:
                    dp[i][j] = dp[i - 1][j]
        return dp[len(coins)][amount]

if __name__ == '__main__':
    amount = 5
    coins = [1, 2, 5]
    print(Solution().change(amount, coins))
