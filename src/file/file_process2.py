import argparse
from PIL import Image
from tqdm import tqdm
from pathlib import Path, PurePath


# 8号 3568*650
# python main.py --img-size 1504 640 --left-width 325 --right-width 325
# 9号
# python main.py --img-size 1504 640 --left-width 340 --right-width 320

# 10号 3728*680
# python main.py --img-size 1504 640 --left-width 318 --right-width 360 --h-dynamic 15 15
# 10号 3728*660
# python main.py --img-size 1504 640 --left-width 370 --right-width 335  --right-dynamic 0 7 --h-dynamic 20 0

# 11号 3636*660
# python main.py --img-size 1504 640 --left-width 360 --right-width 325 --left-dynamic 0 5 --right-dynamic 12 0 --h-dynamic 10 10
# 12号 3668*650
# python main.py --img-size 1504 640 --left-width 390 --right-width 308 --left-dynamic 0 30 --right-dynamic 40 0
# 12号 3728*650
# python main.py --img-size 1504 640 --left-width 425 --right-width 370 --left-dynamic 0 20 --right-dynamic 25 0
# 13号 3672*600
# python main.py --img-size 1504 640 --left-width 370 --right-width 350 --left-dynamic 18 15 --right-dynamic 12 5
# 14号 3460*650
# python main.py --img-size 1504 640 --left-width 295 --right-width 285 --left-dynamic 0 10 --right-dynamic 5 -2 --h-dynamic 10 0


def parse_opt(known=False):
    parser = argparse.ArgumentParser()
    parser.add_argument('--img-size', nargs='+', type=int, default=None, help='cut size w,h')
    parser.add_argument('--left-width', type=int, default=318, help='截断图片左边px')
    parser.add_argument('--right-width', type=int, default=360, help='截断图片右边px')

    parser.add_argument('--left-dynamic', nargs='+', type=int, default=[0, 0], help='动态调整左边距')
    parser.add_argument('--right-dynamic', nargs='+', type=int, default=[0, 0], help='动态调整右边距')
    parser.add_argument('--h-dynamic', nargs='+', type=int, default=[0, 0], help='动态调整上下边距')

    parser.add_argument('--source', type=str, default='./source', help='存放需要裁剪图片的文件夹路径')
    parser.add_argument('--target', default='./target', help='save results to project/name')
    parser.add_argument('--no-save', action='store_true', help='do not save images')
    parser.add_argument('--show-left', action='store_true', help='展示裁剪图片')
    parser.add_argument('--show-right', action='store_true', help='展示裁剪图片')
    return parser.parse_known_args()[0] if known else parser.parse_args()


def save_img(image: Image, save_name):
    if not opt.no_save:
        save_path = Path(opt.target).resolve().joinpath(save_name)
        Path(opt.target).mkdir(parents=True, exist_ok=True)
        image.save(save_path)


def resize_img(image: Image):
    if opt.img_size is not None:
        image = image.resize(opt.img_size, Image.ANTIALIAS)
    return image


def show_img(image: Image, show: bool):
    if show:
        image.show()


if __name__ == "__main__":
    opt = parse_opt(True)
    l_x1_d, l_x2_d = opt.left_dynamic
    r_x1_d, r_x2_d = opt.right_dynamic
    top_d, bottom_d = opt.h_dynamic

    # im_paths = ['/Users/pepsiyoung/Project/CSI/收集数据/预处理图片/10号/10-{}.jpg'.format(str(i).rjust(4, '0')) for i in
    #             range(5, 11)]
    im_paths = Path(opt.source).glob('**/*.jpg')
    for im_path in tqdm(list(im_paths)):
        im = Image.open(im_path)
        w, h = im.size
        im_name = Path(im_path).stem

        l_x1, l_y1 = opt.left_width + l_x1_d, top_d
        l_x2, l_y2 = int(w / 2) + l_x2_d, h - bottom_d
        l_im = im.crop((l_x1, l_y1, l_x2, l_y2))
        l_im = resize_img(l_im)
        # 展示左图
        show_img(l_im, opt.show_left)
        save_img(l_im, '{}_l.jpg'.format(im_name))

        r_x1, r_y1 = int(w / 2) + r_x1_d, top_d
        r_x2, r_y2 = w - opt.right_width + r_x2_d, h - bottom_d
        r_im = im.crop((r_x1, r_y1, r_x2, r_y2))
        r_im = resize_img(r_im)
        # 展示右图
        show_img(r_im, opt.show_right)
        save_img(r_im, '{}_r.jpg'.format(im_name))
