def unique_paths_with_obstacles(obstacleGrid) -> int:
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


def question1(m, n, snake):
    dp = [[0 for _ in range(n)] for _ in range(m)]
    dp[0][0] = 0 if [0, 0] in snake else 1
    for i in range(1, m):
        dp[i][0] = 1 if [i, 0] not in snake and dp[i - 1][0] == 1 else 0
    for j in range(1, n):
        dp[0][j] = 1 if [0, j] not in snake and dp[0][j - 1] == 1 else 0

    for i in range(1, m):
        for j in range(1, n):
            if [i, j] in snake:
                dp[i][j] = 0
            else:
                dp[i][j] = dp[i - 1][j] + dp[i][j - 1]

    return dp[m - 1][n - 1]


if __name__ == '__main__':
    # obstacleGrid = [[0, 0, 0], [0, 1, 0], [0, 0, 0]]
    # print(unique_paths_with_obstacles(obstacleGrid))

    # m, n = 2, 2
    # snake_date = [[0, 1]]
    # print(question1(m, n, snake_date))
    # snake 可以改成dict
    pass
