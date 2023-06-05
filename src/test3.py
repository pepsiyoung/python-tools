import shutil
import os
from pathlib import Path
from tqdm import tqdm

# root_path = r'C:\Users\admin\Desktop\气泡切图_1'
# target_path = r'C:\Users\admin\Desktop\气泡Sample'
# paths = Path(root_path).rglob(f'*.json')
# cnt = 0
# for path in paths:
#     new_name = f'{path.parent.name}_{path.name}'
#     path.rename(Path(target_path).joinpath(new_name))
#
# print('finish')


root_image_path = r'C:\Users\admin\Desktop\气泡Sample\image'
root_json_path = r'C:\Users\admin\Desktop\气泡Sample\json'
files = Path(root_image_path).rglob(f'*.bmp')
cnt = 1
for file in files:
    img_path = file
    json_path = Path(root_json_path).joinpath(f'{file.stem}.json')

    if img_path.exists() and json_path.exists():
        new_name = f'bubble_{cnt}'
        os.rename(img_path, fr'C:\Users\admin\Desktop\气泡Sample\111\{new_name}.bmp')
        os.rename(json_path, fr'C:\Users\admin\Desktop\气泡Sample\222\{new_name}.json')
        cnt += 1

print('finish')
