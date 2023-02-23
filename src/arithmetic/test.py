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


def demo2(obstacleGrid):
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
    dp[0][0] = [] if [0, 0] in snake else [(0, 0)]

    for i in range(1, m):
        dp[i][0] = [(i, 0)] if [i, 0] not in snake and dp[i - 1][0] != 0 else []
    for j in range(1, n):
        dp[0][j] = [(0, j)] if [0, j] not in snake and dp[0][j - 1] != 0 else []
    for i in range(1, m):
        for j in range(1, n):
            if [i, j] in snake:
                dp[i][j] = []
            else:
                # dp[i][j] = dp[i - 1][j] + dp[i][j - 1]
                temp = []
                temp.extend(dp[i - 1][j])
                temp.extend(dp[i][j - 1])
                temp.append((i, j))
                dp[i][j] = temp
                # dp[i][j] = [path + (i, j) for path in temp]

    return dp[m - 1][n - 1]


if __name__ == '__main__':
    # obstacleGrid = [[0, 0, 0], [0, 1, 0], [0, 0, 0]]
    # # print(unique_paths_with_obstacles(obstacleGrid))
    # print(demo2(obstacleGrid))

    t = [(0, 2)]

    t.append((3,3))
    print(t)