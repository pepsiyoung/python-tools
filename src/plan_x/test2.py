import time
import yaml
from PIL import Image
from pathlib import Path
from watchdog.events import FileSystemEventHandler
from watchdog.observers import Observer
from fileWatch.my_utils import valid_image


class EventHandler(FileSystemEventHandler):
    def __init__(self):
        FileSystemEventHandler.__init__(self)

    def on_created(self, event):
        print('on_created:', event.src_path)
        # 自旋判断图片完整性，超过 N 秒跳过
        sleep_count = 0
        time.sleep(0.5)
        while not valid_image(event.src_path) and sleep_count < 6:
            time.sleep(0.5)
            sleep_count += 1
            print('sleep_count:', sleep_count)

        try:
            suffix = Path(event.src_path).suffix
            if suffix.endswith("jpg"):
                im = Image.open(event.src_path)
                # save_path = Path(self.target_path).joinpath(cur_date)
                # Path(save_path).mkdir(parents=True, exist_ok=True)
                im_save_path = Path('../target').joinpath(Path(event.src_path).name)
                im.transpose(Image.Transpose.FLIP_LEFT_RIGHT).save(im_save_path)
        except Exception as err:
            print(err, event.src_path)


if __name__ == "__main__":
    with open('config.yaml', 'r', encoding="utf-8") as f:
        file_data = f.read()
        data = yaml.load(file_data, Loader=yaml.FullLoader)
        print(data['source'])

    path1 = r'E:\temp\source1'
    path2 = r'E:\temp\source2'
    observer = Observer()
    event_handler = EventHandler()
    observer.schedule(event_handler, path1, True)
    observer.schedule(event_handler, path2, True)
    observer.start()
    print('运行')
    observer.join()
