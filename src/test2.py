import time
import numpy as np
from src.PyQT.fileWatch.lru_cache import LRUCache
from pathlib import Path


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

    write_file = open(r"D:\Test\source1\name-A.jpg", "wb")
    with open(im_path, "rb") as f:
        for index, line in enumerate(f.readlines()):
            write_file.write(line)
            time.sleep(0.02)
            print(index)

    write_file.close()
    print('end')


def create_delay_image(im_path, interval_second):
    file_name = Path(im_path).stem
    write_file = open(rf"D:\Test\source1\{file_name}.jpg", "wb")
    with open(im_path, "rb") as f:
        for index, line in enumerate(f.readlines()):
            write_file.write(line)
            time.sleep(interval_second)
            print(index)

    write_file.close()
    print('end')


def use_np_c():
    x1 = np.array([1, 2, 3])
    x2 = np.array([4, 5, 6])
    res = np.c_[x1, x2]
    print(res)


if __name__ == '__main__':
    # source = r'D:\Datasets\DataSample\层后0411\images'
    # target = r'D:\Datasets\DataSample\层后0411\images1'
    # txt_paths = list(Path(source).glob('*.jpg'))
    # for txt_path in tqdm(list(txt_paths)):
    #     im = Image.open(txt_path)
    #     w, h = im.size
    #     if w == 3800 and h == 2200:
    #         shutil.copy(Path(txt_path), Path(target))
    create_delay_image(r"D:\Test\14-000014-B.jpg", 0.1)
