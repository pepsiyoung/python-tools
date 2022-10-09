import shutil
import argparse
from tqdm import tqdm
from pathlib import Path
from sklearn.model_selection import train_test_split


def parse_opt(known=False):
    parser = argparse.ArgumentParser()
    parser.add_argument('--train', type=str, default='./train', help='')
    parser.add_argument('--valid', type=str, default='./valid', help='')
    parser.add_argument('--size', type=float, default=0.15, help='')
    return parser.parse_known_args()[0] if known else parser.parse_args()


# 随机分隔验证集
if __name__ == "__main__":
    opt = parse_opt(True)
    label_paths = Path(opt.train).joinpath('labels').glob('**/*.txt')
    train_labels, valid_labels = train_test_split(list(label_paths), test_size=opt.size)
    # 创建文件夹
    valid_image_path = Path(opt.valid).joinpath('images')
    valid_label_path = Path(opt.valid).joinpath('labels')
    Path(valid_image_path).mkdir(parents=True, exist_ok=True)
    Path(valid_label_path).mkdir(parents=True, exist_ok=True)

    for label_path in tqdm(valid_labels):
        name = Path(label_path).stem
        image_path = '{}/{}.jpg'.format(Path(opt.train).joinpath('images'), name)

        shutil.move(image_path, valid_image_path)
        shutil.move(label_path, valid_label_path)
