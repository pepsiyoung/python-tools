import argparse
import shutil
from pathlib import Path
from tqdm import tqdm


def parse_opt(known=False):
    parser = argparse.ArgumentParser()
    parser.add_argument('--source', type=str, default='./source', help='需要移动的文件')
    parser.add_argument('--target', default='./target', help='目标文件夹')
    return parser.parse_known_args()[0] if known else parser.parse_args()


if __name__ == "__main__":
    opt = parse_opt(True)
    paths = Path(opt.source).glob('**/*.json')
    for path in tqdm(list(paths)):
        shutil.copy(str(path), opt.target)
