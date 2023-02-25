def questionA(m, n, snake):
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
    pass



if __name__ == '__main__':
    # test_cases = [
    #     (3, 3, [[1, 1]]),
    #     (2, 2, [[0, 1]]),
    #     (3, 3, [0, 1]),
    #     (3, 3, [1, 0]),
    #     (3, 3, [0, 0]),
    #     (3, 3, [2, 2])
    # ]
    # for params in test_cases:
    #     print(f'params -> m:{params[0]} m:{params[1]} snake_data:{params[2]}')
    #     m, n, snake_date = params[0], params[1], params[2]
    #     res = questionA(m, n, snake_date)
    #     # res = questionB(m, n, snake_date)
    #     print(f'result:{res}')
    #     print('==============================')
    res = questionA(2, 6, [[0, 1], [0, 5], [1, 3]])
    print(res)
