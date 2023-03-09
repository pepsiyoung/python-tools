class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        def dfs(x, y, m, n, mem):
            # terminal
            if x > m - 1 or y > n - 1:
                return 0
            if x == m - 1 or y == n - 1:
                return 1
            # process + drill down
            if mem[x][y] != -1:
                return mem[x][y]

            mem[x][y] = dfs(x + 1, y, m, n, mem) + dfs(x, y + 1, m, n, mem)
            return mem[x][y]

        mem = [[-1] * n for _ in range(m)]
        return dfs(0, 0, m, n, mem)

    def uniquePathsWithObstacles(self, obstacleGrid) -> int:

        def dfs(x, y):
            # terminal
            if (x, y) in mem:
                return mem[x, y]
            if x >= m or y >= n or obstacleGrid[x][y] == 1:
                return 0
            if x == m - 1 and y == n - 1:
                return 1
            mem[x, y] = dfs(x + 1, y) + dfs(x, y + 1)
            return mem[x, y]

        m = len(obstacleGrid)
        n = len(obstacleGrid[0])
        mem = {}
        return dfs(0, 0)

    def subsets(self, nums):
        ans = [[]]
        for num in nums:
            sub_list = [_ + [num] for _ in ans]
            ans.extend(sub_list)
        return ans

        # res = [[]]
        # for i in nums:
        #     sub_list = [[i] + num for num in res]
        #     res.extend(sub_list)
        # print(res)


if __name__ == '__main__':
    arr1 = [[0, 0], [0, 1]]
    # arr2 = [[0, 0, 0], [0, 1, 0], [0, 0, 0]]
    # result = Solution().uniquePathsWithObstacles(arr1)
    # print(result)
    # arr.append([1, 2, 3])
    # arr.append([4, 5, 6])

    # Solution().subsets([1, 2, 3])

