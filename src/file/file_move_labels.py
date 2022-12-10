import argparse
import shutil
from pathlib import Path
from tqdm import tqdm


# 移动标记种类
def parse_opt(known=False):
    parser = argparse.ArgumentParser()
    parser.add_argument('--source', type=str, default=r'D:\Datasets\DataProcess\prepare\1202EL_8\labels', help='labels源文件夹')
    parser.add_argument('--target', type=str, default=r'D:\Datasets\DataProcess\prepare\1202EL_8\labels_1', help='labels目标文件夹')
    return parser.parse_known_args()[0] if known else parser.parse_args()


if __name__ == '__main__':
    opt = parse_opt(True)
    txt_paths = list(Path(opt.source).glob('*.txt'))
    for txt_path in tqdm(list(txt_paths)):
        # with open(txt_path, 'r') as f:
        #     lines = f.readlines()
        #     x = [line[0] for line in lines]
        #     if '1' in x:
        #         shutil.copy(Path(txt_path), Path(opt.target))

        with open(txt_path, 'r') as f:
            lines = (i for i in f.readlines() if int(i[0]) < 4)
            file_path = Path(opt.target).joinpath(txt_path.name)
            file_new = open(file_path, 'w')
            file_new.writelines(lines)
            file_new.close()
