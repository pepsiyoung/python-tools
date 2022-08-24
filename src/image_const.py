import shutil
import argparse
from PIL import Image
from PIL import ImageChops
from pathlib import Path
from tqdm import tqdm
import imagehash


def parse_opt(known=False):
    parser = argparse.ArgumentParser()
    parser.add_argument('--source', type=str, required=True, help='加载文件夹路径')
    parser.add_argument('--target', type=str, required=True, help='重复图片移动到此文件夹')
    return parser.parse_known_args()[0] if known else parser.parse_args()


def deep_compare(im_list):
    for index, im in enumerate(im_list[:-1]):
        for next_im in im_list[index + 1:]:
            try:
                diff = ImageChops.difference(im[1], next_im[1])
                if diff.getbbox() is None:
                    # 相同
                    repeat_list.append(im[0])
                    # print('相同', im[0], next_im[0])
                    break
            except ValueError as e:
                print(e, im[0], next_im[0])


# 图片去重
if __name__ == '__main__':
    opt = parse_opt(True)
    repeat_list = []
    my_dict = {}
    print('正在加载图像，请稍等...')
    im_paths = list(Path(opt.source).glob('**/*.jpg'))
    im_list = [(path, Image.open(path).convert('L')) for path in im_paths]

    print('正在去重...')
    for item in im_list:
        path, im = item
        key = imagehash.dhash(im)
        my_dict.setdefault(str(key), []).append(item)

    new_dict = {k: v for k, v in my_dict.items() if len(v) > 1}
    for k, v in tqdm(new_dict.items()):
        deep_compare(v)

    for path in repeat_list:
        shutil.move(path, opt.target)

    print('总数:{} 重复:{}'.format(len(im_paths), len(repeat_list)))
