class Solution(object):
    def coinchange(self,coin,amount):
        def dp(n):
            if n == 0 :return 0
            if n<0 :return -1
            res = float('INF')
            for i in coin:
                sub = dp(n - i)
                if sub == -1 : continue
                res = min(res,sub+1)
            return res if res !=float('INF') else -1
        return dp(amount)
if __name__ == '__main__':
    print(Solution().coinchange(coin=[5,3,4],amount=8))
