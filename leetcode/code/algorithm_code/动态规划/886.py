class Solution(object):

    def dfs(self, graph, colors, i, color, N):
        print(colors)
        colors[i] = color
        for j in range(N):
            # dislike eachother
            if graph[i][j] == 1:
                if colors[j] == color:
                    return False
                if colors[j] == 0 and not self.dfs(graph, colors, j, -1 * color, N):
                    return False
        return True

    def possibleBipartition(self, N, dislikes):
        """
        :type N: int
        :type dislikes: List[List[int]]
        :rtype: bool
        """

        colors = [0 for i in range(N)]
        graph = [[0] * N for i in range(N)]
        for a, b in dislikes:
            graph[a - 1][b - 1] = 1
            graph[b - 1][a - 1] = 1
        for i in range(N):
            if colors[i] == 0 and not self.dfs(graph, colors, i, 1, N):
                return False
        return True






if __name__ == '__main__':
    N = 4
    dislikes = [[1,2],[1,3],[2,4]]
    print(Solution().possibleBipartition(N,dislikes))