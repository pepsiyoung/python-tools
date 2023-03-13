from pathlib import Path
from tqdm import tqdm
import shutil
import argparse


def parse_opt(known=False):
    parser = argparse.ArgumentParser()
    parser.add_argument('--source', type=str, default='./source', help='源文件夹')
    parser.add_argument('--save', default='./target', help='保存文件夹')
    parser.add_argument('--find-file', type=str, default='./source', help='需要查找的文件')
    parser.add_argument('--suffix', default='txt', help='搜索文件后缀')
    return parser.parse_known_args()[0] if known else parser.parse_args()


if __name__ == "__main__":
    opt = parse_opt(True)
    Path(opt.save).mkdir(parents=True, exist_ok=True)

    for path in tqdm(list(Path(opt.find_file).rglob(f"*.{opt.suffix}"))):
        cur = Path(opt.source).joinpath(path.name)
        shutil.copy(str(cur), opt.save)
