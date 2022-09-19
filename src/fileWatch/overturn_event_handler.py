import time
import my_utils
from pathlib import Path
from watchdog.events import FileSystemEventHandler
from overturn_global_var import get_value


class OverturnEventHandler(FileSystemEventHandler):
    def __init__(self, source_dir, target_dir):
        FileSystemEventHandler.__init__(self)
        self.source_dir = source_dir
        self.target_dir = target_dir

    def process(self, path):
        im_suffix = Path(path).suffix
        if im_suffix.endswith('jpg'):
            cur_date = time.strftime("%Y-%m-%d", time.localtime())
            im_stem = Path(path).stem

            source_path = Path(self.source_dir).joinpath(f'{im_stem}.jpg')
            target_path = Path(self.target_dir).joinpath(cur_date).joinpath(f'{im_stem}.jpg')

            my_utils.spin_im(source_path)
            my_utils.transpose_save(source_path, target_path, get_value('height'))

    def on_created(self, event):
        print('on_created:', event.src_path)
        self.process(event.src_path)
