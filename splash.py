from PyQt5.QtGui import QMovie
import sys
from PyQt5.QtWidgets import QApplication,QLabel
from PyQt5.QtCore import QTimer,Qt
app = QApplication(sys.argv)
gif = QMovie('ft.gif')
gif.start()
label1=QLabel()
label1.setMovie(gif)
# 1366 x 768
label1.setGeometry(283,130,800,508)
label1.setWindowFlags(Qt.SplashScreen|Qt.FramelessWindowHint)
label1.show()
QTimer.singleShot(6000,app.quit)
sys.exit(app.exec_())

