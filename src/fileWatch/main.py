import os
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QToolTip, QPushButton, QFileDialog, QLabel
from PyQt5.QtGui import QIcon, QFont
from PyQt5.QtCore import QCoreApplication, QRect
import event_handler as handler


class Example(QWidget):

    def __init__(self):
        super().__init__()

        self.source_label = QLabel(self)
        self.target_label = QLabel(self)
        self.initUI()

    def initUI(self):
        # label控件
        self.source_label.setText('请选择监听文件夹')
        self.source_label.move(150, 80)
        self.source_label.setFixedWidth(300)
        self.target_label.setText('请选择目标文件夹')
        self.target_label.move(150, 150)
        self.target_label.setFixedWidth(300)

        # 选择目录控件
        source_btn = QPushButton('选择监听文件夹', self)
        source_btn.clicked.connect(self.open_source_folder)
        source_btn.move(550, 80)
        target_btn = QPushButton('选择监目标件夹', self)
        target_btn.clicked.connect(self.open_target_folder)
        target_btn.move(550, 150)

        # 功能button
        btn = QPushButton('监听', self)
        btn.clicked.connect(lambda: handler.start(self.source_label.text(), self.target_label.text()))
        btn.resize(btn.sizeHint())
        btn.move(220, 300)
        quit_btn = QPushButton('退出', self)
        quit_btn.clicked.connect(QCoreApplication.instance().quit)
        quit_btn.resize(quit_btn.sizeHint())
        quit_btn.move(520, 300)

        self.setGeometry(300, 300, 800, 400)
        self.setWindowTitle('Icon')
        self.setWindowIcon(QIcon('./icon.png'))
        self.show()

    def open_source_folder(self):
        path = QFileDialog.getExistingDirectory(self, "选取监听文件夹", "/")  # 起始路径
        self.source_label.setText(path)

    def open_target_folder(self):
        path = QFileDialog.getExistingDirectory(self, "选取目标文件夹", "/")  # 起始路径
        self.target_label.setText(path)


if __name__ == '__main__':
    os.chdir('/Users/pepsiyoung/Project/my/python/python-tools/src/fileWatch')
    print(os.getcwd())
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
