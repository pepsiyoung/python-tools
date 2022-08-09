import os
import yaml
import argparse
from watchdog.observers import Observer
from watchdog.events import *
from PIL import Image


def parse_opt(known=False):
    parser = argparse.ArgumentParser()
    parser.add_argument('--source', type=str, default='./source', help='存放需要裁剪图片的文件夹路径')
    parser.add_argument('--target', type=str, default='./target', help='目标文件夹')
    return parser.parse_known_args()[0] if known else parser.parse_args()


def coord():
    print(os.getcwd())
    with open('fileWatch/config_border.yaml', 'r', encoding="utf-8") as f:
        file_data = f.read()
        data = yaml.load(file_data, Loader=yaml.FullLoader)

    config_list, activate = data['border'], data['activate']
    res = list(filter(lambda x: (x['name'] == activate), config_list))[0]['px']
    return tuple(list(map(int, res.split(","))))


def cut(img_path, point):
    origin_im = Image.open(img_path)
    x1, y1, x2, y2 = point
    w, h = origin_im.size
    return origin_im.crop((x1, y1, w - x2, h - y2))


class FileEventHandler(FileSystemEventHandler):
    def __init__(self):
        FileSystemEventHandler.__init__(self)

    def on_created(self, event):
        opt = parse_opt(True)
        file_name = os.path.basename(event.src_path)
        print(file_name)
        if file_name.endswith("jpg"):
            cut_im = cut(event.src_path, coord())
            cut_im.save("{0}/{1}".format(opt.target, file_name))


if __name__ == "__main__":
    opt = parse_opt(True)
    observer = Observer()
    event_handler = FileEventHandler()
    observer.schedule(event_handler, opt.source, False)
    observer.start()
    print('运行')

    # try:
    #     while True:
    #         time.sleep(1)
    # except KeyboardInterrupt:
    #     observer.stop()
    observer.join()
