import torch
import pandas as pd
from PIL import Image
from pathlib import Path, PurePath
from tqdm import tqdm

# f = open("data.txt", 'r')
# for (index, line) in enumerate(f):
#     print(index)
#     print(line)


# name = 'xuhan'
# n = 20
# res = f"{n} {name}'???'{'s' * (n > 1)}"
# print(res)


if __name__ == "__main__":
    # # 任意的多组列表
    # a = [1, 2, 3]
    # b = [4, 5, 6]
    # # 字典中的key值即为csv中列名
    # dataframe = pd.DataFrame({'a_name': a, 'b_name': b})
    # # 将DataFrame存储为csv,index表示是否显示行名，default=True
    # dataframe.to_csv("test.csv", index=False, sep=',')

    source_folder = '/Users/pepsiyoung/Downloads/虚焊漏检对比图片/检测出/标注'
    save_path = '/Users/pepsiyoung/Downloads/虚焊漏检对比图片/检测出/剪裁'

    image_paths = Path(source_folder).glob('**/8-*.jpg')
    for im_path in tqdm(list(image_paths)):
        origin_im = Image.open(im_path)
        w, h = origin_im.size
        cut_im = origin_im.crop((320, 15, w - 320, 610))
        cut_im.save("{0}/{1}.jpg".format(save_path, Path(im_path).stem))
