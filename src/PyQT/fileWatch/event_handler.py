import time
import global_var
import my_utils
from pathlib import Path
from watchdog.events import FileSystemEventHandler
from my_utils import valid_image, cut, coord


class FileEventHandler(FileSystemEventHandler):
    def __init__(self, target_path):
        FileSystemEventHandler.__init__(self)
        self.target_path = target_path

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
                cut_im = cut(event.src_path, coord(file_name))
                cur_date = time.strftime("%Y-%m-%d", time.localtime())
                save_path = Path(self.target_path).joinpath(cur_date)
                Path(save_path).mkdir(parents=True, exist_ok=True)
                im_save_path = Path(save_path).joinpath('{}{}'.format(file_name, suffix))
                cut_im.save(im_save_path)
                # 外观图修改名称
                if my_utils.get_config("rename_dir") is not None:
                    print('等待：外观图修改名称')
                    queue = global_var.get_queue()
                    wg_im_path = Path(queue.get())
                    wg_im_path.rename(wg_im_path.parent.joinpath('{}{}'.format(file_name, suffix)))
                    print('完成：外观图修改名称')

        except Exception as err:
            print(err, event.src_path)
