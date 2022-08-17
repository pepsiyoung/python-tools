import yaml
import time
from pathlib import Path
from watchdog.events import *
from PIL import Image
from PIL import UnidentifiedImageError


def coord():
    with open('config_border.yaml', 'r', encoding="utf-8") as f:
        file_data = f.read()
        data = yaml.load(file_data, Loader=yaml.FullLoader)

    config_list, activate = data['border'], data['activate']
    res = list(filter(lambda x: (x['name'] == activate), config_list))[0]['px']
    return tuple(list(map(int, res.split(","))))


def cut(img_path, point):
    origin_im = Image.open(Path(img_path))
    x1, y1, x2, y2 = point
    w, h = origin_im.size
    return origin_im.crop((x1, y1, w - x2, h - y2))


def valid_image(path):
    b_valid = True
    try:
        Image.open(path).verify()
    except (UnidentifiedImageError, PermissionError):
        b_valid = False
    return b_valid


class FileEventHandler(FileSystemEventHandler):
    def __init__(self, target_path):
        FileSystemEventHandler.__init__(self)
        self.target_path = target_path

    def on_created(self, event):
        print('on_created:', event.src_path)
        # 自旋判断图片完整性，超过 N 秒跳过
        sleep_count = 0
        while not valid_image(event.src_path) and sleep_count < 8:
            time.sleep(0.5)
            sleep_count += 1
            print(sleep_count)

        try:
            suffix = Path(event.src_path).suffix
            file_name = Path(event.src_path).stem
            if suffix.endswith("jpg"):
                cut_im = cut(event.src_path, coord())
                cur_date = time.strftime("%Y-%m-%d", time.localtime())
                save_path = Path(self.target_path).joinpath(cur_date)
                Path(save_path).mkdir(parents=True, exist_ok=True)
                im_save_path = Path(save_path).joinpath('{}.{}'.format(file_name, suffix))
                cut_im.save(im_save_path)
        except Exception as err:
            print(err, event.src_path)
