import time
import numpy as np
from PIL import Image
from pathlib import Path
from watchdog.events import FileSystemEventHandler
from my_utils import valid_image


class OverturnEventHandler(FileSystemEventHandler):
    def __init__(self, target_path, height):
        FileSystemEventHandler.__init__(self)
        self.target_path = target_path
        self.height = height
        self.last = (None, None)

    def process(self, path):
        last_path = self.last[0]
        last_time = time.time() if self.last[1] is None else self.last[1]
        # 防抖 如果收到的图像与上一张同名并且在3秒内，就不进行处理
        if last_path == path and int(time.time() - last_time) < 3:
            return
        print('process:', path)
        # 自旋判断图片完整性，超过 N 秒跳过
        sleep_count = 0
        time.sleep(0.5)
        while not valid_image(path) and sleep_count < 8:
            time.sleep(0.5)
            sleep_count += 1
            print('sleep_count:', sleep_count)

        try:
            suffix = Path(path).suffix
            file_name = Path(path).name
            if suffix.endswith("jpg"):
                im = Image.open(path).convert('RGB')
                w, h = im.size
                transpose_h = h - self.height
                cur_date = time.strftime("%Y-%m-%d", time.localtime())
                save_path = Path(self.target_path).joinpath(cur_date)
                Path(save_path).mkdir(parents=True, exist_ok=True)
                im_save_path = Path(save_path).joinpath('{}'.format(file_name))

                im_np = np.array(im)
                im_new_np = np.concatenate((im_np[:transpose_h, ::-1, :], im_np[transpose_h:, :, :]), axis=0)
                Image.fromarray(im_new_np).save(im_save_path)
                self.last = (path, time.time())
        except Exception as err:
            print(err, path)

    def on_created(self, event):
        print('on_created:', event.src_path)
        self.process(event.src_path)

    def on_modified(self, event):
        print('on_modified:', event.src_path)
        self.process(event.src_path)

    def on_moved(self, event):
        print('on_moved:', event.src_path)

    def on_deleted(self, event):
        print('on_deleted:', event.src_path)
