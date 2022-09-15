from collections import OrderedDict


class LRUCache(OrderedDict):
    """不能存储可变类型对象，不能并发访问set()"""

    def __init__(self, capacity):
        super().__init__()
        self.capacity = capacity
        self.cache = OrderedDict()

    def get(self, key):
        if key in self.cache:
            value = self.cache.pop(key)
            self.cache[key] = value
        else:
            value = None

        return value

    def set(self, key, value):
        if key in self.cache:
            value = self.cache.pop(key)
            self.cache[key] = value
        else:
            if len(self.cache) == self.capacity:
                self.cache.popitem(last=False)  # pop出第一个item
                self.cache[key] = value
            else:
                self.cache[key] = value

    def __str__(self):
        return str(self.cache)
