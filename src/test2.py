import shutil
from pathlib import Path
from tqdm import tqdm

# paths = Path(r'E:\pythonDemo\image').glob('**/*.jpg')
# for path in tqdm(list(paths)):
#     shutil.copy(path, Path(r'E:\pythonDemo\source\222'))

fo = open("E:\\pythonDemo\\image\\222\\08-0001.jpg", "w")
print("文件名: ", fo.name)
