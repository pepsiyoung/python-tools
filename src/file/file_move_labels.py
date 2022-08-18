import shutil
from pathlib import Path
from tqdm import tqdm

# 移动标记种类
txt_paths = Path("D:\datasets\CSI_0815").glob('**/*.txt')
count = 0
for txt_path in tqdm(list(txt_paths)):
    with open(txt_path, 'r') as f:
        lines = f.readlines()
        x = [line[0] for line in lines]
        if len(x) == x.count('0'):
            shutil.copy(Path(txt_path), Path('D:\datasets\labels'))
            count += 1
        # print(x.count('0'))

        # for line in lines:
        #     value = line[0]

print(count)
