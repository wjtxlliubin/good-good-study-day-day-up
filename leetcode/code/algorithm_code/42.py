'''
给定 n 个非负整数表示每个宽度为 1 的柱子的高度图，计算按此排列的柱子，下雨之后能接多少雨水。
上面是由数组 [0,1,0,2,1,0,1,3,2,1,2,1] 表示的高度图，在这种情况下，可以接 6 个单位的雨水（蓝色部分表示雨水）
'''


class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        count = 0
        lenght = len(height)
        left_max = [0 for _ in range(lenght)]
        right_max = [0 for _ in range(lenght)]
        left_max[0] = height[0]
        right_max[-1] = height[-1]
        for i in range(1, lenght):
            left_max[i] = max(left_max[i - 1], height[i - 1])
        for j in range(lenght - 2, -1, -1):
            right_max[j] = max(height[j], right_max[j + 1])
        for i in range(1, lenght - 1):
            max_left = left_max[i]
            max_right = right_max[i]
            cur = min(max_left, max_right) - height[i]
            count += cur if cur > 0 else 0
        return count


if __name__ == '__main__':
    # [0,1,0,2,1,0,1,3,2,1,2,1]
    print(Solution().trap([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]))
    # for i in range(5, -1, -1):
    #     print(i)
