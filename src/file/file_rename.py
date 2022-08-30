import os
import argparse
from pathlib import Path
from tqdm import tqdm


def parse_opt(known=False):
    parser = argparse.ArgumentParser()

    parser.add_argument('--source', type=str, default='./source', help='存放需要裁剪图片的文件夹路径')
    parser.add_argument('--rename', type=str, required=True, help='重命名名称 例如:8-lie')
    parser.add_argument('--index', type=int, default=0, help='序号')
    return parser.parse_known_args()[0] if known else parser.parse_args()


if __name__ == "__main__":

    opt = parse_opt(True)
    index = opt.index

    image_paths = Path(opt.source).glob('**/*.jpg')
    for im_path in tqdm(list(image_paths)):
        index += 1
        new_name = '{}-{}.jpg'.format(opt.rename, str(index).rjust(4, '0'))
        new_file_path = Path(opt.source).joinpath(new_name)
        os.rename(im_path, new_file_path)
