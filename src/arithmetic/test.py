def unique_paths_with_obstacles1(obstacleGrid) -> int:
    m, n = len(obstacleGrid), len(obstacleGrid[0])
    dp = [[0 for _ in range(n)] for _ in range(m)]

    dp[0][0] = 0 if obstacleGrid[0][0] == 1 else 1
    for i in range(1, m):
        dp[i][0] = 1 if obstacleGrid[i][0] == 0 and dp[i - 1][0] == 1 else 0
    for j in range(1, n):
        dp[0][j] = 1 if obstacleGrid[0][j] == 0 and dp[0][j - 1] == 1 else 0

    for i in range(1, m):
        for j in range(1, n):
            if obstacleGrid[i][j] == 0:
                dp[i][j] = dp[i - 1][j] + dp[i][j - 1]
            else:
                dp[i][j] = 0

    return dp[m - 1][n - 1]


def unique_paths_with_obstacles2(obstacleGrid):
    m, n = len(obstacleGrid), len(obstacleGrid[0])
    dp = [0] * n

    dp[0] = 1 if obstacleGrid[0][0] == 0 else 0
    for i in range(m):
        for j in range(n):
            if obstacleGrid[i][j] == 1:
                dp[j] = 0
                continue
            if j - 1 >= 0 and obstacleGrid[i][j] == 0:
                dp[j] += dp[j - 1]

    return dp[n - 1]


def questionD(m, n, snake):
    dp = [[[] for _ in range(n)] for _ in range(m)]
    dp[0][0] = [] if [0, 0] in snake else [[(0, 0)]]

    for i in range(1, m):
        dp[i][0] = [[(_, 0) for _ in range(i + 1)]] if [i, 0] not in snake and dp[i - 1][0] != 0 else []

    for j in range(1, n):
        dp[0][j] = [[(0, _) for _ in range(j + 1)]] if [0, j] not in snake and dp[0][j - 1] != 0 else []

    for i in range(1, m):
        for j in range(1, n):
            if [i, j] in snake:
                dp[i][j] = []
            else:
                temp_arr = list()
                temp_arr.extend(dp[i - 1][j])
                temp_arr.extend(dp[i][j - 1])
                dp[i][j] = [item + [(i, j)] for item in temp_arr]

    return dp[m - 1][n - 1]


if __name__ == '__main__':
    # nums = [40, 36, 40, 2, 36, 100, 7]
    # for i in range(2):
    #     r = nums.remove(40)
    #     print(nums, r)

    print(len([]))
