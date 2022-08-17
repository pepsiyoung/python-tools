import shutil
from pathlib import Path
from tqdm import tqdm
from PIL import Image

# paths = Path(r'E:\pythonDemo\image').glob('**/*.jpg')
# for path in tqdm(list(paths)):
#     shutil.copy(path, Path(r'E:\pythonDemo\source\222'))

# fo = open("E:\\pythonDemo\\image\\222\\08-0001.jpg", "w")
# print("文件名: ", fo.name)

# im = Image.open("/Users/pepsiyoung/userfiles/source/9-201140-B.jpg")
im = Image.open("/Users/pepsiyoung/userfiles/source/Java面试宝典.jpg")
print(im.verify())
