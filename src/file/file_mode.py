import argparse
from PIL import Image
from pathlib import Path
from tqdm import tqdm


def parse_opt(known=False):
    parser = argparse.ArgumentParser()
    parser.add_argument('--source', type=str, required=True, help='图像存放的位置')
    return parser.parse_known_args()[0] if known else parser.parse_args()


if __name__ == "__main__":
    opt = parse_opt(True)
    values_cnt = {'RGB': 0, 'L': 0}
    paths = list(Path(opt.source).glob('**/*.jpg'))

    for path in tqdm(paths):
        im_mode = Image.open(path).mode
        values_cnt[im_mode] = values_cnt.get(im_mode, 0) + 1

    print(values_cnt)
