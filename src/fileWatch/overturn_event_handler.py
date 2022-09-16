import time
import my_utils
from pathlib import Path
from watchdog.events import FileSystemEventHandler
from overturn_global_var import get_value
from lru_cache import LRUCache

lru_list = LRUCache(128)


class OverturnEventHandler(FileSystemEventHandler):
    def __init__(self):
        FileSystemEventHandler.__init__(self)
        self.last = (None, None)

    @staticmethod
    def build_im_name(im_stem):
        im_count = len(list(Path(get_value('target_wg_dir')).glob(f'**/{im_stem}*.jpg')))
        print('im_count', im_count)
        if im_count == 0:
            return f'{im_stem}.jpg'
        else:
            return f'{im_stem}_{im_count}.jpg'

    def process(self, path):
        im_suffix = Path(path).suffix
        if im_suffix.endswith('jpg'):
            cur_date = time.strftime("%Y-%m-%d", time.localtime())
            height = get_value('height')
            im_stem = Path(path).stem

            source_el_path = Path(get_value('source_el_dir')).joinpath(f'{im_stem}.jpg')
            source_wg_path = Path(get_value('source_wg_dir')).joinpath(f'{im_stem}.jpg')
            im_target_name = self.build_im_name(im_stem)
            target_el_path = Path(get_value('target_el_dir')).joinpath(cur_date).joinpath(im_target_name)
            target_wg_path = Path(get_value('target_wg_dir')).joinpath(cur_date).joinpath(im_target_name)

            my_utils.spin_im(source_wg_path)
            my_utils.transpose_save(source_wg_path, target_wg_path, height)

            my_utils.spin_im(source_el_path)
            my_utils.transpose_save(source_el_path, target_el_path, height)

    @LRUCache.run(lru_list)
    def on_created(self, event):
        print('on_created:', event.src_path)
        self.process(event.src_path)

    @LRUCache.run(lru_list)
    def on_modified(self, event):
        print('on_modified:', event.src_path)
        self.process(event.src_path)
