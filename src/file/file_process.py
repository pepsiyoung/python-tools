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
    parser.add_argument('--machine-no', type=str, required=True, help='机台号')
    parser.add_argument('--source', type=str, default='./source', help='存放需要裁剪图片的文件夹路径')
    parser.add_argument('--target', default='./target', help='save results to project/name')
    parser.add_argument('--disable-resize', action='store_true', default=False, help='禁用resize')
    parser.add_argument('--resize', nargs='+', type=int, default=[1728, 608], help='cut size w,h')
    return parser.parse_known_args()[0] if known else parser.parse_args()


config_map = {
    '08-A': {'middle_px': 1788, 'left_box': (48, 14, 0, 30), 'right_box': (0, 14, 30, 25)},
    '08-B': {'middle_px': 1788, 'left_box': (48, 25, 0, 30), 'right_box': (0, 25, 30, 25)},
    '09-A': {'middle_px': 1760, 'left_box': (55, 25, 0, 25), 'right_box': (0, 25, 35, 12)},
    '10-A': {'middle_px': 1864, 'left_box': (10, 25, 12, 30), 'right_box': (0, 34, 75, 40)},
    '10-B': {'middle_px': 1864, 'left_box': (80, 40, 0, 5), 'right_box': (0, 34, 28, 5)},
    '11-A': {'middle_px': 1835, 'left_box': (60, 30, 0, 30), 'right_box': (0, 25, 15, 25)},
    '12-3668': {'middle_px': 1878, 'left_box': (90, 20, 5, 20), 'right_box': (0, 10, 12, 25)},
    '12-3728': {'middle_px': 1885, 'left_box': (110, 0, 0, 40), 'right_box': (0, 0, 70, 40)},
    '13-A': {'middle_px': 1850, 'left_box': (80, 5, 0, 0), 'right_box': (0, 0, 40, 0)},
    '14-A': {'middle_px': 1740, 'left_box': (10, 10, 0, 35), 'right_box': (0, 10, 0, 40)},
    '14-B': {'middle_px': 1740, 'left_box': (10, 25, 0, 0), 'right_box': (0, 30, 0, 5)},
    '14-one': {'middle_px': 1690, 'left_box': (0, 0, 0, 85), 'right_box': (0, 0, 50, 100)},
    'cut-08': {'middle_px': 1655, 'left_box': (0, 0, 0, 0), 'right_box': (0, 0, 0, 0)},
    'cut-09': {'middle_px': 1740, 'left_box': (20, 0, 0, 0), 'right_box': (0, 0, 35, 0)},
    'cut-10': {'middle_px': 1895, 'left_box': (30, 0, 0, 0), 'right_box': (0, 0, 0, 0)},
    'cut-11': {'middle_px': 1722, 'left_box': (15, 0, 0, 0), 'right_box': (0, 0, 15, 0)},
    'cut-12': {'middle_px': 1785, 'left_box': (0, 0, 0, 0), 'right_box': (0, 0, 0, 0)},
    'cut-13': {'middle_px': 1790, 'left_box': (20, 0, 0, 0), 'right_box': (0, 0, 20, 0)},
    'cut-14': {'middle_px': 1740, 'left_box': (40, 25, 0, 30), 'right_box': (0, 30, 0, 45)},
    'other-3180-610': {'middle_px': 1590, 'left_box': (0, 10, 0, 85), 'right_box': (0, 10, 0, 85)},
    'other-3180-620': {'middle_px': 1590, 'left_box': (0, 0, 0, 110), 'right_box': (0, 0, 0, 110)},
    'other-3180-670': {'middle_px': 1590, 'left_box': (0, 0, 0, 70), 'right_box': (0, 0, 0, 70)},
    'wg7242': {'middle_px': 4425, 'left_box': (50, 120, 0, 45), 'right_box': (0, 85, 75, 45)},
    'wg7415': {'middle_px': 4475, 'left_box': (40, 10, 0, 40), 'right_box': (0, 20, 70, 45)},
    'wg7424': {'middle_px': 4485, 'left_box': (65, 75, 0, 70), 'right_box': (0, 65, 95, 60)},
    'test': {'middle_px': 4132, 'left_box': (70, 75, 0, 70), 'right_box': (0, 65, 95, 60)},
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
            # 是否禁用resize
            if opt.disable_resize:
                resize_im = cut_im
            else:
                resize_im = cut_im.resize(resize, Image.Resampling.LANCZOS)
            save_path = Path(opt.target).joinpath('{}_{}.jpg'.format(index, im_path.stem))
            resize_im.convert('RGB').save(save_path)
