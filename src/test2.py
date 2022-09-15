from pathlib import Path
from fileWatch.lru_cache import LRUCache


class Person:
    def __init__(self, name):
        self.name = name

    @LRUCache.auto_cache
    def run(self, age):
        print('run', self.name, age)


p = Person('zcy')
p.run(18)

p.run(20)
