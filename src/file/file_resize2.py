import argparse
from pathlib import Path
from tqdm import tqdm
from PIL import Image


# 等比缩放高宽
def parse_opt(known=False):
    parser = argparse.ArgumentParser()
    parser.add_argument('--source', type=str, default='./source', help='源文件夹')
    parser.add_argument('--target', default='./target', help='目标文件夹')
    parser.add_argument('--width', type=int, default=1728, help='等比缩放')
    return parser.parse_known_args()[0] if known else parser.parse_args()


if __name__ == "__main__":
    opt = parse_opt(True)
    im_paths = list(Path(opt.source).glob('*.jpg'))
    for im_path in tqdm(im_paths):
        im = Image.open(im_path)
        w, h = im.size
        ratio = 1728 / w
        resize_im = im.resize((int(w * ratio), int(h * ratio)), Image.ANTIALIAS)
        save_path = Path(opt.target).joinpath(im_path.name)
        resize_im.convert('RGB').save(save_path)
