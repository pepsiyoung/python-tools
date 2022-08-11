import argparse
import shutil
from pathlib import Path


def parse_opt(known=False):
    parser = argparse.ArgumentParser()
    parser.add_argument('--source', type=str, default='./source', help='需要移动的文件')
    parser.add_argument('--target', default='./target', help='目标文件夹')
    parser.add_argument('--suffix', default='json', help='搜索文件后缀')
    return parser.parse_known_args()[0] if known else parser.parse_args()


if __name__ == "__main__":

    opt = parse_opt(True)

    # 创建文件夹
    images_folder = Path(opt.target).joinpath('images')
    labels_folder = Path(opt.target).joinpath('labels')
    images_folder.mkdir(parents=True, exist_ok=True)
    labels_folder.mkdir(parents=True, exist_ok=True)
    # 遍历
    paths = Path(opt.source).glob('**/*.{}'.format(opt.suffix))
    for json_path in paths:
        img_name = '{}.jpg'.format(json_path.stem)
        img_path = Path(opt.source).joinpath(img_name)
        if json_path.exists() and img_path.exists():
            print(str(json_path))
            shutil.copy(str(img_path), str(images_folder))
            shutil.copy(str(json_path), str(labels_folder))
