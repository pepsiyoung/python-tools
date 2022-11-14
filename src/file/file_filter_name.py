from pathlib import Path
from tqdm import tqdm
import shutil

if __name__ == "__main__":
    source_dir = r'E:\DataProcess\1114'
    target_dir = r'E:\DataProcess\1114\test'
    paths = Path(source_dir).glob('*.{}'.format('jpg'))
    for path in tqdm(list(paths)):
        if 'A' in path.stem:
            shutil.move(str(path), target_dir)
