import sys
from PyQt5.QtCore import QCoreApplication, QThread
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QFileDialog, QLabel, QMessageBox
from watchdog.observers import Observer
from event_handler import FileEventHandler
import my_utils

version = 'v3.0.0'


class Example(QWidget):

    def __init__(self):
        super().__init__()

        self.thread = None
        self.observer = None
        self.btn = QPushButton('监听', self)
        self.source_label = QLabel(self)
        self.target_label = QLabel(self)
        self.activate_label = QLabel(self)
        self.valid()
        self.init_ui()

    def valid(self):
        # 验证License
        license_key = my_utils.get_file_licence()
        valid = my_utils.valid_licence(license_key)
        if not valid:
            QMessageBox.warning(self, "警告", "Licence无效3.0", QMessageBox.Yes)
            sys.exit(0)

    def init_ui(self):
        # label控件
        self.source_label.setText('请选择监听文件夹')
        self.source_label.move(100, 80)
        self.source_label.setFixedWidth(400)
        self.target_label.setText('请选择目标文件夹')
        self.target_label.move(100, 150)
        self.target_label.setFixedWidth(400)
        self.activate_label.move(100, 220)

        source_dir = my_utils.get_config('source_dir')
        target_dir = my_utils.get_config('target_dir')
        self.source_label.setText(source_dir)
        self.target_label.setText(target_dir)
        self.activate_label.setText(f'ACTIVATE: {my_utils.get_config("activate")}')

        # 选择目录控件
        source_btn = QPushButton('选择监听文件夹', self)
        source_btn.clicked.connect(self.open_source_folder)
        source_btn.move(550, 80)
        target_btn = QPushButton('选择监目标件夹', self)
        target_btn.clicked.connect(self.open_target_folder)
        target_btn.move(550, 150)

        # 功能button
        # btn.clicked.connect(lambda: handler.start(self.source_label.text(), self.target_label.text()))
        self.btn.clicked.connect(self.listener)
        self.btn.resize(self.btn.sizeHint())
        self.btn.move(220, 300)
        quit_btn = QPushButton('退出', self)
        quit_btn.clicked.connect(QCoreApplication.instance().quit)
        quit_btn.resize(quit_btn.sizeHint())
        quit_btn.move(520, 300)

        self.setGeometry(300, 300, 800, 400)
        self.setWindowTitle(f'串修边程序_{version}')
        self.setWindowIcon(QIcon('./icon.png'))
        self.show()
        # 是否自动启动
        if my_utils.get_config('auto_start') is True:
            self.listener()

    def open_source_folder(self):
        path = QFileDialog.getExistingDirectory(self, "选取监听文件夹", "/")  # 起始路径
        self.source_label.setText(path)

    def open_target_folder(self):
        path = QFileDialog.getExistingDirectory(self, "选取目标文件夹", "/")  # 起始路径
        self.target_label.setText(path)

    def listener(self):
        if self.btn.text() == '监听':
            print(f'{version} 文件监听中。。。')
            self.btn.setText('暂停')
            self.observer = Observer()
            self.thread = ListenerThread(self.observer, self.source_label.text(), self.target_label.text())
            self.thread.start()
        else:
            print('监听结束')
            self.btn.setText('监听')
            self.observer.stop()


class ListenerThread(QThread):

    def __init__(self, observer, source, target):
        super(ListenerThread, self).__init__()
        self.observer = observer
        self.source = source
        self.target = target

    def run(self):
        event_handler = FileEventHandler(self.target)
        self.observer.schedule(event_handler, self.source, True)
        self.observer.start()
        self.observer.join()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
