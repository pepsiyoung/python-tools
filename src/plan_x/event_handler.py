import time
import requests
import pprint
from PIL import Image
from PIL import UnidentifiedImageError
from pathlib import Path
from watchdog.events import FileSystemEventHandler


def valid_image(path):
    b_valid = True
    try:
        with open(path, 'rb') as f:
            buf = f.read()
            if buf[6:10] in (b'JFIF', b'Exif'):
                if not buf.rstrip(b'\0\r\n').endswith(b'\xff\xd9'):
                    b_valid = False

        Image.open(path).verify()
    except (UnidentifiedImageError, PermissionError, FileNotFoundError):
        b_valid = False
    return b_valid


DETECTION_URL = "http://localhost:5050/v1/object-detection/yolov5s"


class EventHandler(FileSystemEventHandler):
    def __init__(self):
        FileSystemEventHandler.__init__(self)

    def on_created(self, event):
        print('on_created:', event.src_path)
        # 自旋判断图片完整性，最多等待 N 秒
        sleep_count = 0
        time.sleep(0.5)
        while not valid_image(event.src_path) and sleep_count < 6:
            time.sleep(0.5)

        try:
            suffix = Path(event.src_path).suffix
            if suffix.endswith("jpg") or suffix.endswith("jpeg"):
                with open(event.src_path, "rb") as f:
                    image_data = f.read()

                response = requests.post(DETECTION_URL, files={"image": image_data}).json()
                pprint.pprint(response)
        except Exception as err:
            print(err, event.src_path)
