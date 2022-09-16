import time
from pathlib import Path
from fileWatch.lru_cache import LRUCache

lru_list = LRUCache(3)

lru_list.set('xxx', 123)
lru_list.set('yyy', 123)
lru_list.set('zzz', 123)

lru_list.set('AAA', 123)
lru_list.set('AAA', 456)

print(lru_list)
# print(lru_list.get('AAA'))
