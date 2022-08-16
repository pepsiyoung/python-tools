import os
import shutil
from PIL import Image
from PIL import ImageChops
from pathlib import Path
from tqdm import tqdm

if __name__ == '__main__':
    load_path = 'D:\\datasets\\CSI_0812\\train\\images'

    repeat_list = []
    im_paths = Path(load_path).glob('**/*.jpg')
    im_list = list(im_paths)

    for index, path in enumerate(im_list[:-1]):
        for next_path in im_list[index + 1:]:
            im1, im2 = Image.open(path), Image.open(next_path)
            diff = ImageChops.difference(im1, im2)
            if diff.getbbox() is None:
                repeat_list.append(path)
                break

    print(repeat_list)
    print(len(repeat_list))

    # print(diff.getbbox())

    # load_path = 'E:\\测试图片集(未去重)'  # 要去重的文件夹
    # save_path = 'E:\\测试图片集(重复照片)'  # 空文件夹，用于存储检测到的重复的照片
    # os.makedirs(save_path, exist_ok=True)
    #
    # # 获取图片列表 file_map，字典{文件路径filename : 文件大小image_size}
    # file_map = {}
    # image_size = 0
    # # 遍历filePath下的文件、文件夹（包括子目录）
    # for parent, dirnames, filenames in os.walk(load_path):
    #     # for dirname in dirnames:
    #     # print('parent is %s, dirname is %s' % (parent, dirname))
    #     for filename in filenames:
    #         # print('parent is %s, filename is %s' % (parent, filename))
    #         # print('the full name of the file is %s' % os.path.join(parent, filename))
    #         image_size = os.path.getsize(os.path.join(parent, filename))
    #         file_map.setdefault(os.path.join(parent, filename), image_size)
    #
    # # 获取的图片列表按 文件大小image_size 排序
    # file_map = sorted(file_map.items(), key=lambda d: d[1], reverse=False)
    # file_list = []
    # for filename, image_size in file_map:
    #     file_list.append(filename)
    #
    # # 取出重复的图片
    # file_repeat = []
    # for currIndex, filename in enumerate(file_list):
    #     dir_image1 = file_list[currIndex]
    #     dir_image2 = file_list[currIndex + 1]
    #     result = (dir_image1, dir_image2)
    #     if (result == "两张图相同"):
    #         file_repeat.append(file_list[currIndex + 1])
    #         print("\n相同的图片：", file_list[currIndex], file_list[currIndex + 1])
    #     else:
    #         print('\n不同的图片：', file_list[currIndex], file_list[currIndex + 1])
    #     currIndex += 1
    #     if currIndex >= len(file_list) - 1:
    #         break
    #
    # # 将重复的图片移动到新的文件夹，实现对原文件夹降重
    # for image in file_repeat:
    #     shutil.move(image, save_path)
    #     print("正在移除重复照片：", image)
