import argparse
import shutil
from pathlib import Path
from tqdm import tqdm


# 移动标记种类
def parse_opt(known=False):
    parser = argparse.ArgumentParser()
    parser.add_argument('--source', type=str, default=r'./source', help='labels源文件夹')
    parser.add_argument('--target', type=str, default=r'./target', help='labels目标文件夹')
    parser.add_argument('--filter-cls', type=str, default=['4', '6'])
    parser.add_argument('--sample-move', action='store_true', help='设置使用 move 或 copy')
    return parser.parse_known_args()[0] if known else parser.parse_args()


if __name__ == '__main__':
    opt = parse_opt(True)
    txt_paths = list(Path(opt.source).glob('*.txt'))
    wait_process = list()
    for txt_path in tqdm(list(txt_paths)):
        with open(txt_path, 'r') as f:
            lines = f.readlines()
            x = [line[0] for line in lines]
            if len(set(opt.filter_cls).intersection(set(x))) > 0:
                wait_process.append(txt_path)

    # 选择是 move 还是 copy
    sample_process = shutil.move if opt.sample_move else shutil.copy
    for txt_path in wait_process:
        sample_process(Path(txt_path), Path(opt.target))
