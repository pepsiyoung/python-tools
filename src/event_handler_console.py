import yaml
import argparse
from watchdog.observers import Observer
from PIL import Image
import time
from pathlib import Path
from watchdog.events import FileSystemEventHandler
from fileWatch.my_utils import valid_image, cut, coord


def parse_opt(known=False):
    parser = argparse.ArgumentParser()
    parser.add_argument('--source', type=str, default='./source', help='存放需要裁剪图片的文件夹路径')
    parser.add_argument('--target', type=str, default='./target', help='目标文件夹')
    return parser.parse_known_args()[0] if known else parser.parse_args()


def coord():
    # print(os.getcwd())
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
        print('on_created:', event.src_path)
        # 自旋判断图片完整性，超过 N 秒跳过
        sleep_count = 0
        time.sleep(0.5)
        while not valid_image(event.src_path) and sleep_count < 4:
            time.sleep(0.5)
            sleep_count += 1
            print('sleep_count:', sleep_count)

        try:
            suffix = Path(event.src_path).suffix
            file_name = Path(event.src_path).stem
            if suffix.endswith("jpg"):
                cut_im = cut(event.src_path, coord())
                cur_date = time.strftime("%Y-%m-%d", time.localtime())
                save_path = Path(opt.target).joinpath(cur_date)
                Path(save_path).mkdir(parents=True, exist_ok=True)
                im_save_path = Path(save_path).joinpath('{}{}'.format(file_name, suffix))
                cut_im.save(im_save_path)
        except Exception as err:
            print(err, event.src_path)

    def on_modified(self, event):
        print('on_modified:', event.src_path)

    def on_moved(self, event):
        print('on_moved:', event.src_path)

    def on_deleted(self, event):
        print('on_deleted:', event.src_path)


if __name__ == "__main__":
    opt = parse_opt(True)
    observer = Observer()
    event_handler = FileEventHandler()
    observer.schedule(event_handler, opt.source, True)
    observer.start()
    print('运行')

    # try:
    #     while True:
    #         time.sleep(1)
    # except KeyboardInterrupt:
    #     observer.stop()
    observer.join()
