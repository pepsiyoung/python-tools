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
    parser.add_argument('--resize', nargs='+', type=int, default=[1728, 576], help='cut size w,h')
    return parser.parse_known_args()[0] if known else parser.parse_args()


config_map = {8: {'middle_px': 1788, 'left_box': (48, 14, 0, 50), 'right_box': (0, 14, 30, 45), 'resize': (1728, 576)}}

if __name__ == "__main__":
    opt = parse_opt(True)
    config = config_map.get(opt.machine_no)
    middle = config['middle_px']
    left_box = config['left_box']
    right_box = config['right_box']
    resize = config['resize']
    Path(opt.target).mkdir(parents=True, exist_ok=True)

    im_paths = Path(opt.source).glob('**/*.jpg')
    for im_path in tqdm(list(im_paths)):
        cut_im = ImageProcess.cut_middle(im_path, middle)
        im_list = zip(cut_im, (left_box, right_box))
        for item in im_list:
            item_im = ImageProcess.cut_around(item[0], item[1])
            resize_im = item_im.resize(resize, Image.Resampling.LANCZOS)
            resize_im.show()
