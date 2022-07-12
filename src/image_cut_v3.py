import math
import argparse
from pathlib import Path, PurePath
from PIL import Image
from tqdm import tqdm


def parse_opt(known=False):
    parser = argparse.ArgumentParser()
    parser.add_argument('--border', nargs='+', type=int, default=None, help='边框预剪裁（上 右 下 左）')
    parser.add_argument('--img-size', nargs='+', type=int, default=[640, 640], help='cut size h,w')
    parser.add_argument('--source', type=str, default='./images', help='存放需要裁剪图片的文件夹路径')
    parser.add_argument('--target', default='./target', help='save results to project/name')
    parser.add_argument('--show-img', action='store_true', help='展示裁剪图片')
    parser.add_argument('--no-save', action='store_true', help='do not save images')
    return parser.parse_known_args()[0] if known else parser.parse_args()


def cut(img_path):
    origin_im = Image.open(img_path)
    if opt.border is not None:
        origin_im = border_cut(origin_im, opt.border)
        if opt.show_img:
            origin_im.show()
            print(origin_im.size)

    origin_w, origin_h = origin_im.size
    cut_w, cut_h = opt.img_size
    row_num = math.floor(origin_w / cut_w)
    col_num = math.floor(origin_h / cut_h)
    # 图片剪裁编号
    serial_num = 0

    # 遍历列
    for col_index in range(col_num):
        # 遍历行
        for row_index in range(row_num):
            serial_num += 1
            x1, y1 = row_index * cut_w, col_index * cut_h
            x2, y2 = (row_index + 1) * cut_w, (col_index + 1) * cut_h
            cut_im = origin_im.crop((x1, y1, x2, y2))
            if not opt.no_save:
                save(cut_im, img_path, serial_num)


# 边框预剪裁
def border_cut(image: Image, border):
    padding_top, padding_right, padding_bottom, padding_left = border
    w, h = image.size
    return image.crop((padding_left, padding_top, w - padding_right, h - padding_bottom))


def save(image: Image, img_path, serial_num):
    img_name = Path(img_path).stem
    save_path = Path(opt.target).resolve().joinpath(img_name)
    Path(save_path).mkdir(parents=True, exist_ok=True)
    image.save("{0}/{1}_{2}.jpg".format(save_path, img_name, serial_num))


if __name__ == "__main__":
    Image.MAX_IMAGE_PIXELS = None
    opt = parse_opt(True)

    image_paths = Path(opt.source).glob('**/*.jpg')
    for item in tqdm(list(image_paths)):
        cut(item.resolve())
