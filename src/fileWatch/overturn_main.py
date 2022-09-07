import sys
from PyQt5.QtCore import QCoreApplication, QThread
from PyQt5.QtGui import QIcon, QIntValidator, QFont
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QFileDialog, QLabel, QMessageBox, QLineEdit
from watchdog.observers import Observer
from overturn_event_handler import OverturnEventHandler
import my_utils


# 图像水平翻转
class Example(QWidget):

    def __init__(self):
        super().__init__()

        self.thread_el = None
        self.thread_wg = None
        self.observer_el = None
        self.observer_wg = None
        self.btn = QPushButton('监听', self)
        self.quit_btn = QPushButton('退出', self)
        self.source_el_label = QLabel(self)
        self.source_wg_label = QLabel(self)
        self.target_el_label = QLabel(self)
        self.target_wg_label = QLabel(self)
        self.height_edit = QLineEdit(self)
        self.valid()
        self.init_ui()

    def valid(self):
        # 验证License
        license_key = my_utils.get_file_licence()
        valid = my_utils.valid_licence(license_key)
        if not valid:
            QMessageBox.warning(self, "警告", "Licence无效", QMessageBox.Yes)
            sys.exit(0)

    def init_ui(self):
        # label控件
        self.source_el_label.setText('请选择EL监听文件夹')
        self.source_el_label.move(100, 70)
        self.source_el_label.setFixedWidth(400)

        self.source_wg_label.setText('请选择WG监听文件夹')
        self.source_wg_label.move(100, 100)
        self.source_wg_label.setFixedWidth(400)

        self.target_el_label.setText('请选择EL目标文件夹')
        self.target_el_label.move(100, 170)
        self.target_el_label.setFixedWidth(400)

        self.target_wg_label.setText('请选择WG目标文件夹')
        self.target_wg_label.move(100, 200)
        self.target_wg_label.setFixedWidth(400)

        self.height_edit.setValidator(QIntValidator())
        self.height_edit.setMaxLength(4)
        self.height_edit.setText('80')
        self.height_edit.move(100, 250)

        # 选择目录控件
        source_el_btn = QPushButton('选择监听EL文件夹', self)
        source_el_btn.clicked.connect(lambda: self.open_source_folder('el'))
        source_el_btn.move(550, 70)

        source_wg_btn = QPushButton('选择监听WG文件夹', self)
        source_wg_btn.clicked.connect(lambda: self.open_source_folder('wg'))
        source_wg_btn.move(550, 100)

        target_el_btn = QPushButton('选择目标EL文件夹', self)
        target_el_btn.clicked.connect(lambda: self.open_target_folder('el'))
        target_el_btn.move(550, 170)

        target_wg_btn = QPushButton('选择目标WG文件夹', self)
        target_wg_btn.clicked.connect(lambda: self.open_target_folder('wg'))
        target_wg_btn.move(550, 200)

        # 测试
        self.source_el_label.setText(r"E:\temp\source1")
        self.source_wg_label.setText(r"E:\temp\source2")
        self.target_el_label.setText(r"E:\temp\target1")
        self.target_wg_label.setText(r"E:\temp\target2")

        # 功能button
        self.btn.clicked.connect(lambda: self.listener(self.height_edit.text()))
        self.btn.resize(self.btn.sizeHint())
        self.btn.move(220, 300)

        self.quit_btn.clicked.connect(QCoreApplication.instance().quit)
        self.quit_btn.resize(self.quit_btn.sizeHint())
        self.quit_btn.move(520, 300)

        self.setGeometry(300, 300, 800, 400)
        self.setWindowTitle('overturn')
        self.setWindowIcon(QIcon('./icon.png'))
        self.show()

    def open_source_folder(self, model):
        path = QFileDialog.getExistingDirectory(self, "选取监听文件夹", "/")  # 起始路径
        if model == 'el':
            self.source_el_label.setText(path)
        else:
            self.source_wg_label.setText(path)

    def open_target_folder(self, model):
        path = QFileDialog.getExistingDirectory(self, "选取目标文件夹", "/")  # 起始路径
        if model == 'el':
            self.target_el_label.setText(path)
        else:
            self.target_wg_label.setText(path)

    def listener(self, height):
        if self.btn.text() == '监听':
            print('v1.1.2 overturn 文件监听中。。。')
            self.btn.setText('暂停')
            self.observer_el = Observer()
            self.observer_wg = Observer()
            self.thread_el = ListenerThread(self.observer_el, self.source_el_label.text(), self.target_el_label.text(),
                                            int(height))
            self.thread_wg = ListenerThread(self.observer_wg, self.source_wg_label.text(), self.target_wg_label.text(),
                                            int(height))
            self.thread_el.start()
            self.thread_wg.start()
        else:
            print('监听结束')
            self.btn.setText('监听')
            self.observer_el.stop()
            self.observer_wg.stop()


class ListenerThread(QThread):

    def __init__(self, observer, source, target, height):
        super(ListenerThread, self).__init__()
        self.observer = observer
        self.source = source
        self.target = target
        self.height = height

    def run(self):
        event_handler = OverturnEventHandler(self.target, self.height)
        self.observer.schedule(event_handler, self.source, True)
        self.observer.start()
        self.observer.join()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
