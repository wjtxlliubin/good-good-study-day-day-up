class LIS():
    '''
    最长递增子序列
    '''
    def lis(self, data):
        dp = [1 for i in range(len(data))]
        for index, value in enumerate(data):
            if index > 0:
                j = index
                while j > 0:
                    if data[j - 1] < data[j]:
                        dp[index] = dp[j - 1] + 1
                        j = 0
                    else:
                        j = j - 1
        return max(dp)


if __name__ == '__main__':
    data = [10, 9, 2, 5, 3, 7, 101, 102]
    print(LIS().lis(data))
