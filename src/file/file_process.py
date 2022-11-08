import argparse
from PIL import Image
from pathlib import Path
from tqdm import tqdm


class ImageProcess:

    @staticmethod
    def cut_middle(image_path, middle_px):
        im = Image.open(image_path)
        w, h = im.size
        return im.crop((0, 0, middle_px, h)), im.crop((middle_px, 0, w, h))

    @staticmethod
    def cut_around(im: Image, margin):
        w, h = im.size
        box = margin[0], margin[1], w - margin[2], h - margin[3]
        return im.crop(box)


def parse_opt(known=False):
    parser = argparse.ArgumentParser()
    parser.add_argument('--machine-no', type=int, required=True, help='机台号')
    parser.add_argument('--source', type=str, default='./source', help='存放需要裁剪图片的文件夹路径')
    parser.add_argument('--target', default='./target', help='save results to project/name')
    parser.add_argument('--resize', nargs='+', type=int, default=[1728, 608], help='cut size w,h')
    return parser.parse_known_args()[0] if known else parser.parse_args()


config_map = {
    8: {'middle_px': 1788, 'left_box': (48, 14, 0, 30), 'right_box': (0, 14, 30, 25)},
    9: {'middle_px': 1740, 'left_box': (20, 0, 0, 0), 'right_box': (0, 0, 35, 0)},
    10: {'middle_px': 1864, 'left_box': (10, 25, 12, 30), 'right_box': (0, 34, 75, 40)},
    11: {'middle_px': 1800, 'left_box': (30, 0, 0, 0), 'right_box': (0, 0, 15, 0)},
    12: {'middle_px': 1785, 'left_box': (0, 0, 0, 0), 'right_box': (0, 0, 0, 0)},
    13: {'middle_px': 1790, 'left_box': (20, 0, 0, 0), 'right_box': (0, 0, 20, 0)},
    14: {'middle_px': 1740, 'left_box': (40, 25, 0, 30), 'right_box': (0, 30, 0, 45)}
}

if __name__ == "__main__":
    opt = parse_opt(True)
    config = config_map.get(opt.machine_no)
    middle = config['middle_px']
    left_box = config['left_box']
    right_box = config['right_box']
    resize = opt.resize
    Path(opt.target).mkdir(parents=True, exist_ok=True)

    im_paths = list(Path(opt.source).glob('**/*.jpg'))
    for im_path in tqdm(im_paths):
        im_list = zip(ImageProcess.cut_middle(im_path, middle), (left_box, right_box))
        # 原图一张裁剪为二张，针对每张图进行边缘剪裁，最终转换为GRB三通道图并重命名
        for index, item in enumerate(im_list):
            item_im, item_box = item
            cut_im = ImageProcess.cut_around(item_im, item_box)
            resize_im = cut_im.resize(resize, Image.Resampling.LANCZOS)
            save_path = Path(opt.target).joinpath('{}_{}.jpg'.format(im_path.stem, index))
            resize_im.convert('RGB').save(save_path)

# 测试用
# im_path = r"E:\DataProcess\8.7裂片原图_14_3460\14-004838-B.jpg"
# middle = 1740
# left_box = (40, 25, 0, 30)
# right_box = (0, 30, 0, 45)
#
# l_im, r_im = ImageProcess.cut_middle(im_path, middle)
# # l_im.show()
# # r_im.show()
# left_around_im = ImageProcess.cut_around(l_im, left_box)
# right_around_im = ImageProcess.cut_around(r_im, right_box)
# left_around_im.show()
# right_around_im.show()
# print(left_around_im.size)
# print(right_around_im.size)
