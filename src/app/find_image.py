import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QFileDialog, QLabel, QMessageBox


class FindImage(QWidget):
    def __init__(self):
        super().__init__()

        self.version = 'v1.0.0'
        self.lbl_choose = QLabel(self)
        self.lbl_origin = QLabel(self)
        self.lbl_target = QLabel(self)
        self.btn_start = QPushButton(self)
        self.btn_path = QPushButton(self)

        self.init_ui()

    def init_ui(self):
        self.lbl_choose.setText('请选择txt文件夹')
        self.lbl_choose.move(100, 80)

        self.lbl_origin.setText('请选择原始图文件夹')
        self.lbl_origin.move(100, 150)

        self.lbl_target.setText('请选择目标文件夹')
        self.lbl_target.move(100, 220)

        for widget in [self.lbl_choose, self.lbl_origin, self.lbl_target]:
            source_el_btn = QPushButton('请选择路径', self)
            source_el_btn.move(550, widget.geometry().y())
            source_el_btn.clicked()
            source_el_btn.clicked.connect(lambda: self.open_source_folder(widget))

        # self.btn_path = QPushButton('请选择路径', self)
        # self.btn_path.move(550, 80)
        # self.btn_path.clicked.connect(lambda: self.open_source_folder(self.lbl_choose))

        # self.btn_start.setText('开始')
        # self.btn_start.clicked.connect(self.handle_start)
        # self.btn_start.move(550, 550)
        self.setGeometry(300, 300, 800, 400)
        self.setWindowTitle(f'findImage_{self.version}')
        self.show()

    def open_source_folder(self, control):
        path = QFileDialog.getExistingDirectory(self, "选取监听文件夹", "/")  # 起始路径
        control.setText(path)

    def handle_start(self):
        print('kkk', self.lbl_choose)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = FindImage()
    sys.exit(app.exec_())
