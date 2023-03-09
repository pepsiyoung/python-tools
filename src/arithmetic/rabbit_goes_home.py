def questionA(m, n, snake):
    """
    时间复杂度 O(N^2)
    空间复杂度 O(N^2)
    :param m: 列数
    :param n: 行数
    :param snake: 蛇所在的 grid
    :return: 路径数
    """
    # dp 初始化 全部填充 0
    dp = [[0 for _ in range(n)] for _ in range(m)]
    dp[0][0] = 0 if [0, 0] in snake else 1
    # dp 初始化最左列
    for i in range(1, m):
        dp[i][0] = 1 if [i, 0] not in snake and dp[i - 1][0] == 1 else 0
    # dp 初始化最上行
    for j in range(1, n):
        dp[0][j] = 1 if [0, j] not in snake and dp[0][j - 1] == 1 else 0
    for i in range(1, m):
        for j in range(1, n):
            if [i, j] in snake:
                dp[i][j] = 0
            else:
                dp[i][j] = dp[i - 1][j] + dp[i][j - 1]

    return dp[m - 1][n - 1]


def questionB(m, n, snake):
    """
    时间复杂度 O(N^2)
    空间复杂度 O(N)
    :param m: 列数
    :param n: 行数
    :param snake: 蛇所在的 grid
    :return: 路径数
    """
    dp = [0] * n
    dp[0] = 0 if [0, 0] in snake else 1

    for i in range(m):
        for j in range(n):
            if [i, j] in snake:
                dp[j] = 0
                continue
            if j - 1 >= 0 and [i, j] not in snake:
                dp[j] += dp[j - 1]

    return dp[n - 1]


def questionD(m, n, snake):
    """
    时间复杂度 O(N^2)
    空间复杂度 O(N^2)
    :param m: 列数
    :param n: 行数
    :param snake: 蛇所在的 grid
    :return: 所有经过路径坐标
    """
    dp = [[list() for _ in range(n)] for _ in range(m)]
    if [0, 0] not in snake:
        dp[0][0].append([(0, 0)])

    for i in range(1, m):
        if [i, 0] not in snake and dp[i - 1][0] != []:
            dp[i][0] = [[(_, 0) for _ in range(i + 1)]]

    for i in range(1, n):
        if [0, i] not in snake and dp[0][i - 1] != []:
            dp[0][i] = [[(0, _) for _ in range(i + 1)]]

    for i in range(1, m):
        for j in range(1, n):
            if [i, j] not in snake:
                temp = list()
                temp.extend(dp[i - 1][j])
                temp.extend(dp[i][j - 1])
                dp[i][j] = [_ + [(i, j)] for _ in temp]

    return dp[m - 1][n - 1]


def questionE(m, n, snake):
    def dfs(r, c, obstacle: set):
        # terminator
        if [r, c] in snake:
            return 0
        if c < 0 or c >= n or r < 0 or r >= m or (r, c) in obstacle:
            return 0
        if c == n - 1 and r == m - 1:
            return 1

        # process current
        obstacle.add((r, c))

        # drill down
        res = 0
        res += dfs(r + 1, c, obstacle)
        res += dfs(r - 1, c, obstacle)
        res += dfs(r, c + 1, obstacle)
        res += dfs(r, c - 1, obstacle)

        # reset status
        obstacle.remove((r, c))
        return res

    return dfs(0, 0, set())


if __name__ == '__main__':
    # 测试用例
    # test_cases = [
    #     (3, 3, [[1, 1]]),
    #     (3, 3, [[0, 1]]),
    #     (3, 3, [[1, 0]]),
    #     (3, 3, [[0, 0]]),
    #     (3, 3, [[2, 2]]),
    #     (2, 2, [[0, 1]])
    # ]
    # for params in test_cases:
    #     m, n, snake_date = params
    #     print(f'params -> m:{m} n:{n} snake_data:{snake_date}')
    #     print(f'func -> questionA result:{questionA(m, n, snake_date)}')
    #     print(f'func -> questionB result:{questionB(m, n, snake_date)}')
    #     print(f'func -> questionD result:{questionD(m, n, snake_date)}')
    #     print('==============================')

    # test_cases = [[0, 1], [1, 3]]
    test_cases = []
    print(questionA(2, 3, test_cases))
    print(questionE(2, 3, test_cases))
