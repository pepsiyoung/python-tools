import argparse
import shutil
from pathlib import Path
from tqdm import tqdm


def parse_opt(known=False):
    parser = argparse.ArgumentParser()
    parser.add_argument('--source1', type=str, default=r'E:\detectImage\exam01', help='需要从此文件夹中找图')
    parser.add_argument('--source2', type=str, default=r'D:\Project\yolov5\runs\detect\labels', help='需要找的图片')
    parser.add_argument('--target', default=r'E:\detectImage\test111', help='目标文件夹')
    parser.add_argument('--suffix', default='txt', help='搜索文件后缀')
    return parser.parse_known_args()[0] if known else parser.parse_args()


if __name__ == "__main__":
    opt = parse_opt(True)
    paths = Path(opt.source2).glob('**/*.{}'.format(opt.suffix))
    for json_path in tqdm(list(paths)):
        find_path = Path(opt.source1).joinpath(f'{json_path.stem}.jpg')
        shutil.copy(str(find_path), str(opt.target))
