import argparse
import shutil
from pathlib import Path
from tqdm import tqdm
from PIL import Image


def parse_opt(known=False):
    parser = argparse.ArgumentParser()
    parser.add_argument('--source', type=str, default='./source', help='源文件夹路径')
    parser.add_argument('--target', type=str, default='./target', help='目标文件夹路径')
    return parser.parse_known_args()[0] if known else parser.parse_args()


if __name__ == "__main__":
    opt = parse_opt(True)
    pixel_category = set()

    im_paths = list(Path(opt.source).glob('**/*.jpg'))
    for im_path in tqdm(im_paths):
        im = Image.open(im_path)
        w, h = im.size
        target_path = Path(opt.target).joinpath(f'{w}_{h}')
        if im.size not in pixel_category:
            target_path.mkdir(parents=True, exist_ok=True)
        shutil.copy(str(im_path), str(target_path))
        pixel_category.add(im.size)
