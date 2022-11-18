import argparse
import shutil
from pathlib import Path
from tqdm import tqdm


def parse_opt(known=False):
    parser = argparse.ArgumentParser()
    parser.add_argument('--source', type=str, default='./source')
    parser.add_argument('--new-name', type=str, required=True)
    parser.add_argument('--index', type=int, default=0, help='序号')
    parser.add_argument('--suffix', default='txt', help='后缀名')
    return parser.parse_known_args()[0] if known else parser.parse_args()


if __name__ == "__main__":
    opt = parse_opt(True)
    images_folder = Path(opt.source).joinpath('images')
    labels_folder = Path(opt.source).joinpath('labels')
    index = opt.index
    new_name = opt.new_name

    # 遍历
    paths = Path(labels_folder).glob('**/*.{}'.format(opt.suffix))
    for txt_path in tqdm(list(paths)):
        img_path = Path(images_folder).joinpath('{}.jpg'.format(txt_path.stem))
        if txt_path.exists() and img_path.exists():
            index += 1
            index_num = str(index).rjust(4, '0')
            new_img_path = Path(images_folder).joinpath('{}-{}.jpg'.format(new_name, index_num))
            new_txt_path = Path(labels_folder).joinpath('{}-{}.{}'.format(new_name, index_num, opt.suffix))
            shutil.move(str(img_path), str(new_img_path))
            shutil.move(str(txt_path), str(new_txt_path))
