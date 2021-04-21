import sys
import urllib.request
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import Qt

class Qpixmap_App(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        img_url = 'https://i.imgur.com/8gBnljd.jpg'
        img_data = urllib.request.urlopen(img_url).read()
        img_obj = QPixmap()
        img_obj.loadFromData(img_data)
        img_obj = img_obj.scaledToWidth(700)
        lb_img = QLabel()
        lb_img.setPixmap(img_obj)
        lb_size = QLabel(f'너비: {str(img_obj.width())}, 높이: {str(img_obj.height())}')
        lb_size.setAlignment(Qt.AlignCenter)

        vbox = QVBoxLayout()
        vbox.addWidget(lb_img)
        vbox.addWidget(lb_size)
        self.setLayout(vbox)

        self.setWindowTitle('이미지 표시')
        self.move(500,500)

        self.show()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ax = Qpixmap_App()
    sys.exit(app.exec_())