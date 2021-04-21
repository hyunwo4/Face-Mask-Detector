import sys
from PyQt5.QtWidgets import QMainWindow, QLabel, QPushButton, \
    QApplication, QFileDialog, QMessageBox
from PyQt5.QtGui import QPixmap

'''
버튼을 클릭해서 화면에 이미지를 추가한다. 파일 경로도 표현한다.    
'''
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        # 윈도우 설정
        self.setGeometry(300, 300, 400, 300)  # x, y, w, h
        self.setWindowTitle('Status Window')

        # QButton 위젯 생성 - FileDialog 을 띄위기 위한 버튼
        self.button = QPushButton('QFileDialog Open', self)
        self.button.clicked.connect(self.filedialog_open)
        self.button.setGeometry(10, 10, 200, 30)

        # 이미지를 추가할 라벨
        self.label = QLabel(self)

    def filedialog_open(self):
        fname = QFileDialog.getOpenFileName(self, 'Open File', '',
                                            'All File(*);; Image File(*.png *.jpg)')

        if fname[0]:
            # QPixmap 객체
            pixmap = QPixmap(fname[0])

            self.label.setPixmap(pixmap)  # 이미지 세팅
            self.label.setContentsMargins(10, 50, 10, 10)
            self.label.resize(pixmap.width(), pixmap.height())

            # 이미지의 크기에 맞게 Resize
            self.resize(pixmap.width(), pixmap.height())

        else:
            QMessageBox.about(self, 'Warning', '파일을 선택하지 않았습니다.')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    mainWindow = MainWindow()
    mainWindow.show()
    sys.exit(app.exec_())

