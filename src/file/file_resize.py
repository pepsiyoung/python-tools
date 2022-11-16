import argparse
from pathlib import Path
from tqdm import tqdm
from PIL import Image


def parse_opt(known=False):
    parser = argparse.ArgumentParser()
    parser.add_argument('--source', type=str, default='./source', help='源文件夹')
    parser.add_argument('--target', default='./target', help='目标文件夹')
    parser.add_argument('--resize', nargs='+', type=int, default=[2880, 1280], help='cut size w,h')
    return parser.parse_known_args()[0] if known else parser.parse_args()


if __name__ == "__main__":
    opt = parse_opt(True)
    im_paths = list(Path(opt.source).glob('*.jpg'))
    for im_path in tqdm(im_paths):
        cut_im = Image.open(im_path)
        resize_im = cut_im.resize(opt.resize, Image.Resampling.LANCZOS)
        save_path = Path(opt.target).joinpath(im_path.name)
        resize_im.convert('RGB').save(save_path)
