def find_pair(arr: list, d):
    cache = {}
    for index, item in enumerate(arr):
        cache[item] = index

    print(cache)
    for i in range(len(arr)):
        key = abs(d - arr[i])
        if key in cache.keys() and cache.get(key) != i:
            return i, cache.get(key)
    return None


res = find_pair([50, 100, 150], 50)
print(res)
