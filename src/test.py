from PIL import Image
from pathlib import Path, PurePath
from tqdm import tqdm
import os

source_folder = 'F:\deep-learning\datasets\CSI-AIDI\CSI-AIDI\Detection_0\source'

index = 0
image_paths = Path(source_folder).glob('**/*.jpg')
for im_path in tqdm(list(image_paths)):
    new_name = '{}.png'.format(Path(im_path).stem)
    new_file_path = Path(source_folder).joinpath(new_name)
    os.rename(im_path, new_file_path)