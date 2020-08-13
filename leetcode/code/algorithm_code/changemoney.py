class Solution(object):
    def change(self, coins,amount):
        dp = [i for i in range(amount+1)]
        for i in range(1,amount+1):
            for coin in coins:
                if i - coin < 0:continue
                dp[i] = min(dp[i],1+dp[i-coin])
        return -1 if (dp[amount] == amount + 1) else dp[amount]
if __name__ == '__main__':
    print(Solution().change([ 1,2,5],11))