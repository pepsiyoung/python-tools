import os
from pathlib import Path
from tqdm import tqdm

if __name__ == "__main__":
    source_folder = '/Users/pepsiyoung/Project/CSI/收集数据/预处理图片/14号裂纹裂片'

    index = 0
    image_paths = Path(source_folder).glob('**/*.jpg')
    for im_path in tqdm(list(image_paths)):
        index += 1
        new_name = '14-liepian-{}.jpg'.format(str(index).rjust(4, '0'))
        new_file_path = Path(source_folder).joinpath(new_name)
        os.rename(im_path, new_file_path)
