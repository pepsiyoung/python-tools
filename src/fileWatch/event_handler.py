import yaml
from watchdog.observers import Observer
from watchdog.events import *
from PIL import Image


# source = '/Users/pepsiyoung/Downloads/listenSource'
# target = '/Users/pepsiyoung/Downloads/listenTarget'


def coord():
    with open('config_border.yaml', 'r', encoding="utf-8") as f:
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


def start(source_path, target_path):
    # print('source', source_path)
    # print('target', target_path)

    print('监听:start')
    observer = Observer()
    event_handler = FileEventHandler(target_path)
    observer.schedule(event_handler, source_path, False)
    observer.start()
    observer.join()


class FileEventHandler(FileSystemEventHandler):
    def __init__(self, target_path):
        FileSystemEventHandler.__init__(self)
        self.target_path = target_path

    def on_created(self, event):
        file_name = os.path.basename(event.src_path)
        print(file_name)
        if file_name.endswith("jpg"):
            cut_im = cut(event.src_path, coord())
            cut_im.save("{0}/{1}".format(self.target_path, file_name))
