def find_a_pair(arr, d):
    """
    找一对石头
    时间复杂度:O(N) N是入参arr中元素数量
    空间复杂度:O(N) N是入参arr中元素数量
    :param arr: 数组中的值为 石头的重量
    :param d:
    :return: 返回石头的下标
    """
    hashtable = {}
    for index, weight in enumerate(arr):
        if weight - d in hashtable:
            return [hashtable[weight - d], index]
        hashtable[arr[index]] = index

    return []


def find_multi_pair(arr, d):
    """
    找多对石头
    :param arr:
    :param d:
    :return:
    """
    hashtable = {}
    result = []
    for index, weight in enumerate(arr):
        if weight - d in hashtable:
            result.append((hashtable[weight - d], index))
            del hashtable[weight - d]
        else:
            hashtable[arr[index]] = index
    return result


if __name__ == "__main__":
    test_cases = [([1, 4, 50, 9, 20, 100], 50), ([6, 2, 2, 3, 3, 4, 4], 1), ([99, 1, 2, 3], -1)]
    for params in test_cases:
        print(f'params -> arr:{params[0]} d:{params[1]}')
        # res = find_a_pair(params[0], params[1])
        res = find_multi_pair(params[0], params[1])
        print(f'result:{res}')
        print('==============================')
