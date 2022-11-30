import argparse
from pathlib import Path
from tqdm import tqdm


def parse_opt(known=False):
    parser = argparse.ArgumentParser()
    parser.add_argument('--source', type=str, default=r'D:\Datasets\批量打标计划_28G\有效样本\_WG\1128WG\CCC\labels', help='源文件夹')
    parser.add_argument('--target', default=r'D:\Datasets\批量打标计划_28G\有效样本\_WG\1128WG\CCC\labels2', help='目标文件夹')
    return parser.parse_known_args()[0] if known else parser.parse_args()


if __name__ == '__main__':
    opt = parse_opt(True)
    # {old:new}
    replace_map = {4: 0}
    Path(opt.target).mkdir(parents=True, exist_ok=True)

    txt_paths = list(Path(opt.source).glob('*.txt'))
    for file in tqdm(list(txt_paths)):
        file_data = ''
        with open(file, 'r') as f:
            for line in f:
                if not line[0].isdigit():
                    print(file)
                old_category = int(line[0])
                new_category = replace_map.get(old_category)
                file_data += line if new_category is None else f'{new_category}{line[1:]}'

        target_file = Path(opt.target).joinpath(file.name)
        with open(target_file, 'w') as f:
            f.write(file_data)
