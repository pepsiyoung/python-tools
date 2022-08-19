import shutil
import argparse
from PIL import Image
from PIL import ImageChops
from pathlib import Path
from tqdm import tqdm


def parse_opt(known=False):
    parser = argparse.ArgumentParser()
    parser.add_argument('--source', type=str, required=True, help='加载文件夹路径')
    parser.add_argument('--target', type=str, required=True, help='重复图片移动到此文件夹')
    return parser.parse_known_args()[0] if known else parser.parse_args()


# 图片去重
if __name__ == '__main__':
    opt = parse_opt(True)

    repeat_list = []
    im_paths = Path(opt.source).glob('**/*.jpg')
    im_list = [(path, Image.open(path)) for path in im_paths]

    for index, im in enumerate(tqdm(im_list[:-1])):
        for next_im in im_list[index + 1:]:
            try:
                diff = ImageChops.difference(im[1], next_im[1])
                if diff.getbbox() is None:
                    # 相同
                    repeat_list.append(im[0])
                    break
            except ValueError as e:
                print(e, im[0], next_im[0])

    for path in repeat_list:
        shutil.move(path, opt.target)
    print('相同图片数：{}'.format(len(repeat_list)))
