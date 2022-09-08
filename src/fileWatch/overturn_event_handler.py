import time
import numpy as np
from PIL import Image
from pathlib import Path
from watchdog.events import FileSystemEventHandler
from my_utils import valid_image
from overturn_global_var import get_value


class OverturnEventHandler(FileSystemEventHandler):
    def __init__(self):
        FileSystemEventHandler.__init__(self)
        self.last = (None, None)

    def process(self, path):
        # wg 落盘之后先翻转 再翻转EL
        last_path = self.last[0]
        last_time = time.time() if self.last[1] is None else self.last[1]
        # 防抖 如果收到的图像与上一张同名并且在3秒内，就不进行处理
        if last_path == path and int(time.time() - last_time) < 3:
            return

        im_suffix = Path(path).suffix
        im_name = Path(path).name
        if im_suffix.endswith('jpg'):
            cur_date = time.strftime("%Y-%m-%d", time.localtime())
            height = get_value('height')
            source_el_path = Path(get_value('source_el_dir')).joinpath(im_name)
            source_wg_path = Path(get_value('source_wg_dir')).joinpath(im_name)
            target_el_path = Path(get_value('target_el_dir')).joinpath(cur_date).joinpath(im_name)
            target_wg_path = Path(get_value('target_wg_dir')).joinpath(cur_date).joinpath(im_name)

            OverturnEventHandler.spin_im(source_wg_path)
            OverturnEventHandler.transpose_save(source_wg_path, target_wg_path, height)

            OverturnEventHandler.spin_im(source_el_path)
            OverturnEventHandler.transpose_save(source_el_path, target_el_path, height)

            self.last = (path, time.time())

    @staticmethod
    def spin_im(path):
        # 自旋判断图片完整性，超过 N 秒直接执行
        sleep_count = 0
        time.sleep(0.5)
        while not valid_image(path) and sleep_count < 8:
            time.sleep(0.5)

    @staticmethod
    def transpose_save(source_path, target_path, height):
        # 水平翻转图像并保存
        print('transpose:', source_path)
        try:
            im = Image.open(source_path).convert('RGB')
            w, h = im.size
            transpose_h = h - height
            Path(target_path).parent.mkdir(parents=True, exist_ok=True)
            im_np = np.array(im)
            im_new_np = np.concatenate((im_np[:transpose_h, ::-1, :], im_np[transpose_h:, :, :]), axis=0)
            Image.fromarray(im_new_np).save(target_path)
        except Exception as err:
            print(err, source_path)

    def on_created(self, event):
        print('on_created:', event.src_path)
        self.process(event.src_path)

    def on_modified(self, event):
        print('on_modified:', event.src_path)
        self.process(event.src_path)
