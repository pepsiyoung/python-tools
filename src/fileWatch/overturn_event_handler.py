import time
from PIL import Image
from pathlib import Path
from watchdog.events import FileSystemEventHandler
from my_utils import valid_image


class OverturnEventHandler(FileSystemEventHandler):
    def __init__(self, target_path):
        FileSystemEventHandler.__init__(self)
        self.target_path = target_path

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
            file_name = Path(event.src_path).stem
            if suffix.endswith("jpg"):
                im = Image.open(event.src_path)
                cur_date = time.strftime("%Y-%m-%d", time.localtime())
                save_path = Path(self.target_path).joinpath(cur_date)
                Path(save_path).mkdir(parents=True, exist_ok=True)
                im_save_path = Path(save_path).joinpath('{}{}'.format(file_name, suffix))
                im.transpose(Image.Transpose.FLIP_LEFT_RIGHT).save(im_save_path)
        except Exception as err:
            print(err, event.src_path)
