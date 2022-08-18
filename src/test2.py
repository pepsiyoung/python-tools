import os
from PIL import Image
from PIL import ImageChops
import shutil


def found_same_img_2(path):
    dir_list = []  # 创建一个空列表
    for img_name in os.listdir(path):  # 遍历文件夹下面的文件和目录     listdir() 返回path 目录下的文件和目录列表
        img_dir = path + './' + img_name  # 拼接好每个照片的绝对路径
        dir_list.append(img_dir)  # 生成一个列表
    print('共：', len(dir_list), '张')  # 返回一共有多少张照片
    j = 1
    for No, img_message in enumerate(
            dir_list):  # 将照片的地址组合为索引序列  enumerate() 函数用于将一个可遍历的数据对象(如列表、元组或字符串)组合为一个索引序列，同时列出数据和数据下标，一般用在 for 循环当中。
        img = Image.open(img_message)  # 获取照片的信息    Image.open()打开的图片是PIL类型的，它自带resize函数。
        i = 0
        for other_img_message in dir_list[No + 1:]:
            i += 1
            other_img = Image.open(other_img_message)  # 获取另外一张照片的信息
            try:
                diff = ImageChops.difference(img,other_img)  # 比较两张照片    ImageChops.difference计算“两个图像之间逐像素差异的绝对值”,这将导致返回差异图像.
                if diff.getbbox() is None:  # 两张照片如果一样则进行下程序的执行
                    print('Same:', img_message, '----', other_img_message)  # 打印出两张照片的绝对路径
                    oldpath = img_message  # 这是原来的照片绝对路径
                    newpath = os.path.abspath('D:\Desktop\相同的照片' + './' + str(j) + '.jpg')  # 这是将要移到的文件夹里面的绝对路径，并且重新命名
                    shutil.move(os.path.abspath(oldpath), os.path.abspath(newpath))  # 将相同的照片（排序在前面的）移到新的文件夹中
                    j += 1
            except:
                print('报错，图片不匹配：', img_message, '----', other_img_message)  # 如果两张照片不一样，则打印出两张照片的绝对路径
                continue
        print('还剩多少次比较:', i, '次')  # 还剩多少次


if __name__ == '__main__':
    path = input('请输入要整理的文件夹的绝对路径：')  # 输入要整理的文件夹的绝对路径
    found_same_img_2(path)  # 调用函数

# 注意：代码中 D:\Desktop\相同的照片 是我自己建的一个文件夹
#     可以替换成自己建的文件夹的绝对路径
