import shutil
from pathlib import Path
from tqdm import tqdm

# 移动标记种类

source = r'D:\Datasets\批量打标计划_28G\有效样本\_WG\1128WG\AAA\labels'
target = r'D:\Datasets\批量打标计划_28G\有效样本\_WG\1128WG\AAA\labels1'
txt_paths = Path(source).glob('**/*.txt')
count = 0
for txt_path in tqdm(list(txt_paths)):
    with open(txt_path, 'r') as f:
        lines = f.readlines()
        x = [line[0] for line in lines]
        if len(x) == x.count('4'):
            shutil.copy(Path(txt_path), Path(target))
            count += 1
print(count)
