def questionA(arr, d):
    """
    找一对石头 暴力求解
    时间复杂度:O(N^2)
    空间复杂度:O(1)
    :param arr:
    :param d:
    :return:
    """
    if d < 0:
        return []
    arr_length = len(arr)
    for i in range(arr_length):
        for j in range(i + 1, arr_length):
            if abs(arr[i] - arr[j]) == d:
                return [(i, j)]
    return []


def questionB(arr, d):
    """
    找一对石头
    时间复杂度:O(N) N是入参arr中元素数量
    空间复杂度:O(N) N是入参arr中元素数量
    :param arr: 数组中的值为 石头的重量
    :param d: 重量差
    :return: 返回一对石头的下标; 返回[]表示未匹配
    """
    if d < 0:
        return []
    hashtable = {}
    for index, weight in enumerate(arr):
        if weight - d in hashtable:
            return [(hashtable[weight - d], index)]
        if weight + d in hashtable:
            return [(hashtable[weight + d], index)]
        hashtable[arr[index]] = index
    return []


def questionC(arr, d):
    """
    找多对石头,并全部输出
    时间复杂度:O(N)
    空间复杂度:O(N)
    :param arr: 数组中的值为 石头的重量
    :param d: 重量差
    :return: 返回多对石头的下标; 返回[]表示未匹配
    """
    if d < 0:
        return []
    hashtable = {}
    result = []
    for index, weight in enumerate(arr):
        if weight - d in hashtable and len(hashtable[weight - d]) > 0:
            result.append((hashtable[weight - d][0], index))
            del hashtable[weight - d][0]
        elif weight + d in hashtable and len(hashtable[weight + d]) > 0:
            result.append((hashtable[weight + d][0], index))
            del hashtable[weight + d][0]
        else:
            hashtable[arr[index]] = hashtable.get(arr[index], []) + [index]
    return result


if __name__ == "__main__":
    test_cases = [
        ([1, 2, 3, 4, 5], 1),
        ([5, 4, 3, 2, 1], 1),
        ([1, 4, 6, 10, 8, 12], 2),
        ([12, 8, 6, 10, 4, 1], 2),
        ([2, 2, 2, 4, 4, 4], 2),
        ([2, 2, 2, 4, 4, 4], 2),
        ([1], 1),
        ([], 1),
        ([1, 2, 3, 2, 1], -1),
        ([-6, -9, 12], 3)
    ]
    for test_case in test_cases:
        arr, d = test_case
        print(f'params -> arr:{arr} d:{d}')
        print(f'func -> questionA result:{questionA(arr, d)}')
        print(f'func -> questionB result:{questionB(arr, d)}')
        print(f'func -> questionC result:{questionC(arr, d)}')
        print('==============================')
