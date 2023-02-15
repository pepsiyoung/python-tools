import time
from pathlib import Path
from fileWatch.lru_cache import LRUCache


def lru_cache():
    lru_list = LRUCache(3)

    lru_list.set('xxx', 123)
    lru_list.set('yyy', 123)
    lru_list.set('zzz', 123)

    lru_list.set('AAA', 123)
    lru_list.set('AAA', 456)
    print(lru_list)


def create_delay_image():
    im_path = r"C:\Users\admin\Desktop\待检测图\43-000235-A.jpg"

    write_file = open(r"D:\Test\source1\name.jpg", "wb")
    with open(im_path, "rb") as f:
        for index, line in enumerate(f.readlines()):
            write_file.write(line)
            time.sleep(0.02)
            print(index)

    write_file.close()
    print('end')


if __name__ == '__main__':
    print(__name__)
