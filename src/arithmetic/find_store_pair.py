def find_one_pair(arr, d):
    """
    找一对石头
    时间复杂度:O(N) N是入参arr中元素数量
    空间复杂度:O(N) N是入参arr中元素数量
    :param arr: 数组中的值为 石头的重量
    :param d:
    :return: 返回石头的下标; 返回[]表示未匹配
    """
    if d < 0:
        return []
    hashtable = {}
    for index, weight in enumerate(arr):
        if weight - d in hashtable:
            return [hashtable[weight - d], index]
        if weight + d in hashtable:
            return [hashtable[weight + d], index]
        hashtable[arr[index]] = index
    return []


def find_multi_pair(arr, d):
    """
    找多对石头
    :param arr:
    :param d:
    :return:
    """
    if d < 0:
        return []
    hashtable = {}
    result = []
    for index, weight in enumerate(arr):
        if weight - d in hashtable:
            result.append((hashtable[weight - d], index))
            del hashtable[weight - d]
        elif weight + d in hashtable:
            result.append((hashtable[weight + d], index))
            del hashtable[weight + d]
        else:
            hashtable[arr[index]] = index
    return result


if __name__ == "__main__":
    test_cases = [
        ([1, 2, 3, 4, 5], 1),
        ([5, 4, 3, 2, 1], 1),
        ([1, 4, 6, 10, 8, 12], 2),
        ([12, 8, 6, 10, 4, 1], 2),
        ([1], 1),
        ([], 1),
        ([1, 2], -1),
        ([-6, -9, 12], 3)
    ]


    def test_cases_func(func):
        print(f'=====function: {func.__name__}=====')
        for test_case in test_cases:
            arr, d = test_case
            print(f'params -> arr:{arr} d:{d}')
            res = func(arr, d)
            print(f'result:{res}')
            print("---------------------")


    test_cases_func(find_one_pair)
    test_cases_func(find_multi_pair)
