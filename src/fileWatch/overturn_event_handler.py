import time
import my_utils
from pathlib import Path
from watchdog.events import FileSystemEventHandler
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

            my_utils.spin_im(source_wg_path)
            my_utils.transpose_save(source_wg_path, target_wg_path, height)

            my_utils.spin_im(source_el_path)
            my_utils.transpose_save(source_el_path, target_el_path, height)

            self.last = (path, time.time())

    def on_created(self, event):
        print('on_created:', event.src_path)
        self.process(event.src_path)

    def on_modified(self, event):
        print('on_modified:', event.src_path)
        self.process(event.src_path)
