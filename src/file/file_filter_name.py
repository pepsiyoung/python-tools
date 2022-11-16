from pathlib import Path
from tqdm import tqdm
import shutil

if __name__ == "__main__":
    source_dir = r'C:\Users\Administrator\Desktop\批量打标计划\数据未处理\EL-待切图\12'
    target_dir = r'C:\Users\Administrator\Desktop\批量打标计划\数据未处理\EL-待切图\12_A'
    paths = Path(source_dir).glob('*.{}'.format('jpg'))
    for path in tqdm(list(paths)):
        if 'A' in path.stem:
            shutil.move(str(path), target_dir)
