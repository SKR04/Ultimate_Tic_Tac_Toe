from threading import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

from datetime import datetime
import time
import wolframalpha


class Ui_Form(Thread):
	def send(self):
		if not self.textEdit.toPlainText().isspace() and len(self.textEdit.toPlainText()) != 0:
			self.times += 1
			self.text = self.textEdit.toPlainText()
			self.textEdit.setPlainText("")
			VLayout = QVBoxLayout()
			lbl = QLabel(self.SAContents)
			lbl.setMinimumSize(QSize(31, 31))
			lbl.setSizePolicy(QSizePolicy(QSizePolicy.Minimum, QSizePolicy.MinimumExpanding))
			lbl.setLayoutDirection(Qt.RightToLeft)
			lbl.setStyleSheet("""
background-color:qlineargradient(spread:pad, x1:1, y1:0, x2:0, y2:0,stop:0 rgba(217, 86, 94,0.87) ,stop:0.55 rgba(164,149,200,1) ,stop:1 rgba(94,161,180,0.7));
border-radius: 10px;
padding: 5px;
font: 13px;

""")
			lbl.setText(self.text)
			lbl.adjustSize()
			lbl.setWordWrap(True)
			wid = lbl.frameGeometry().width()
			hgt = lbl.frameGeometry().height()
			if hgt > 26:
				lbl.setText("")
				lbl.setWordWrap(False)
				lbl.setText(self.text)
				lbl.setWordWrap(True)
				lbl.adjustSize()

			lbl.setFixedSize(wid, hgt)

			VLayout.addWidget(lbl)
			lbl1 = QLabel(self.SAContents)
			lbl1.setMaximumSize(QSize(16777215, 16))
			lbl1.setMinimumSize(QSize(45, 16))
			lbl1.setAlignment(Qt.AlignLeading | Qt.AlignRight | Qt.AlignTop)
			text1 = datetime.now().strftime("%H:%M ")
			lbl1.setText(text1)
			lbl1.setStyleSheet("background:transparent;")
			VLayout.addWidget(lbl1)
			VLayout.setSpacing(5)
			lll = QLabel(self.SAContents)
			lll.setStyleSheet("background: transparent;")
			hlayout = QHBoxLayout()
			hlayout.addWidget(lll,1)
			hlayout.addLayout(VLayout, 2)
			self.gridLayout.addLayout(hlayout, self.times, 0, 1, 1)
			self.marnum -= (lbl.height() + lbl1.height())
			self.gridLayout.setContentsMargins(-1, self.marnum-20, -1, -1)
			self.times += 1
			app.processEvents()
			time.sleep(0)


		else:
			pass

	def Mcond(self):
		if not self.textEdit.toPlainText().isspace() and len(self.textEdit.toPlainText()) == 0 and self.text != "":
			try:
				client = wolframalpha.Client("UWVJ3J-WK9EQK9JT5")
				res = client.query(self.text)
				output = next(res.results).text
				if 'Wolfram|Alpha' in str(output):
					output = output.replace('Wolfram|Alpha', "Chocolate")
				if 'Stephen Wolfram' in str(output):
					output = output.replace('Stephen Wolfram', "Vimal, Rajasekar, Fawwaaz")
				self.reply = output
			except Exception:
				self.reply = "No results found 😅 \ntry something else."
			self.Reply()
		else:
			pass

	def Reply(self):
		lbl3 = QLabel(self.SAContents)
		lbl3.setLayoutDirection(Qt.LeftToRight)
		lbl3.setStyleSheet("border-radius: 10px;\n"
		                   "padding: 5px;\n"
		                   "background: white;"
		                   "font: 13px;")

		lbl3.setText(self.reply)

		lbl3.setMaximumSize(323, 10000)
		lbl3.adjustSize()
		lbl3.setWordWrap(True)
		wid = lbl3.frameGeometry().width()
		hgt = lbl3.frameGeometry().height()
		if hgt > 26:
			lbl3.setText("")
			lbl3.setWordWrap(False)
			lbl3.setText(self.reply)
			lbl3.setWordWrap(True)
			lbl3.adjustSize()
		else:
			lbl3.setFixedSize(wid, hgt)
		print(hgt)


		VLayout = QVBoxLayout()
		VLayout.addWidget(lbl3)

		lbl4 = QLabel(self.SAContents)
		lbl4.setMinimumSize(QSize(45, 16))
		lbl4.setMaximumSize(QSize(16777215, 16))
		lbl4.setAlignment(Qt.AlignLeading | Qt.AlignLeft | Qt.AlignTop)
		text1 = datetime.now().strftime(" %H:%M")
		lbl4.setText(text1)
		lbl4.setStyleSheet("background: transparent;")
		VLayout.addWidget(lbl4)
		VLayout.setSpacing(5)
		lll = QLabel(self.SAContents)
		lll.setStyleSheet("background: transparent;")
		hlayout = QHBoxLayout()
		hlayout.addLayout(VLayout,2)
		hlayout.addWidget(lll,1)
		self.gridLayout.addLayout(hlayout, self.times, 0, 1, 1)
		self.marnum -= (lbl3.height() + lbl4.height())
		self.gridLayout.setContentsMargins(-1, self.marnum-15, -1, -1)
		self.times += 1
		app.processEvents()
		time.sleep(2)
		self.text = ""

	def setupUi(self, Form):
		self.times = 0
		self.marnum = 390

		Form.resize(431, 600)
		Form.setMinimumSize(QSize(431, 600))
		Form.setMaximumSize(QSize(431, 600))
		Form.setWindowTitle("ChatBot")
		icon = QIcon()
		icon.addPixmap(QPixmap(":/new prefix/logo.png"), QIcon.Normal, QIcon.Off)
		Form.setWindowIcon(icon)

		self.SArea = QScrollArea(Form)
		self.SArea.setGeometry(QRect(0, 61, 431, 474))
		self.SArea.setStyleSheet("""QWidget{\n
background: transparent;\n
}\n
QScrollBar:vertical {\n
border: 1px solid grey;\n
background: url(:/new prefix/bg1.png);\n
width:10px;\n
margin: 4px 0px 0px 0px;\n
}\n
QScrollBar:vertical {
background: transparent;
width: 12px;
border: 1px solid white;
}
QScrollBar::handle:vertical {
background: transparent;
}
QScrollBar::add-line:vertical,QScrollBar::sub-line:vertical {
height: 0px;
}
QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical {
background:white;
""")
		self.SArea.setFrameShape(QFrame.NoFrame)
		self.SArea.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
		self.SArea.setWidgetResizable(True)
		self.SArea.setObjectName("SArea")

		self.SAContents = QWidget()
		self.SAContents.setGeometry(QRect(0, 0, 431, 474))
		self.SAContents.setObjectName("SAContents")

		self.gridLayout = QGridLayout(self.SAContents)
		self.gridLayout.setContentsMargins(-1, self.marnum, -1, -1)
		self.gridLayout.setVerticalSpacing(0)
		self.gridLayout.setObjectName("gridLayout")

		self.verticalLayout = QVBoxLayout()
		self.verticalLayout.setSpacing(5)
		self.verticalLayout.setObjectName("verticalLayout")

		hour = int(datetime.now().hour)
		if hour >= 0 and hour <= 12:
			self.reply = "Good morning, how can I help you."
		elif hour >= 12 and hour <= 16:
			self.reply = "Good afternoon, how can I help you."
		else:
			self.reply = "Good evening, how can I help you."

		self.lbl1 = QLabel(self.SAContents)

		self.lbl1.setFixedSize(QSize(225, 40))
		self.lbl1.adjustSize()
		self.lbl1.setWordWrap(True)
		self.lbl1.setStyleSheet("""background-color:white;
border-radius: 20px;
padding: 5px;
font: 13px""")
		self.lbl1.setText(self.reply)
		self.verticalLayout.addWidget(self.lbl1)
		self.lbl2 = QLabel(self.SAContents)
		self.lbl2.setMinimumSize(QSize(45, 16))
		self.lbl2.setMaximumSize(QSize(300, 16))
		self.lbl2.setAlignment(Qt.AlignLeading | Qt.AlignLeft | Qt.AlignTop)
		self.lbl2.setText(datetime.now().strftime(" %H:%M"))
		self.verticalLayout.addWidget(self.lbl2)

		self.gridLayout.addLayout(self.verticalLayout, self.times, 0, 1, 1)
		self.times += 1

		label = QLabel(self.SAContents)
		self.gridLayout.addWidget(label, 0, 1, 1, 1)

		self.SArea.setWidget(self.SAContents)

		self.Header = QLabel(Form)
		self.Header.setGeometry(QRect(20, 10, 411, 61))
		font = QFont()
		font.setWeight(50)
		self.Header.setFont(font)
		self.Header.setStyleSheet("background:transparent;\n"
		                          "color:rgb(195, 195, 195);\n"
		                          "\n"
		                          "font:40px \"Starcraft\";")
		self.Header.setAlignment(Qt.AlignCenter)
		self.Header.setText("CHAT BOT")

		self.sendB = QPushButton(Form)
		self.sendB.setGeometry(QRect(380, 540, 41, 41))
		self.sendB.setMinimumSize(QSize(41, 41))
		self.sendB.setMaximumSize(QSize(41, 41))
		self.sendB.setStyleSheet("background: transparent;")
		icon1 = QIcon()
		icon1.addPixmap(QPixmap(":/new prefix/send.png"), QIcon.Normal, QIcon.Off)
		self.sendB.setIcon(icon1)
		self.sendB.setIconSize(QSize(41, 41))
		self.sendB.clicked.connect(self.td)

		self.textEdit = QTextEdit(Form)
		self.textEdit.setGeometry(QRect(10, 540, 361, 41))
		font = QFont()
		font.setPointSize(10)
		self.textEdit.setFont(font)
		self.textEdit.setStyleSheet("QScrollBar:vertical {\n"
		                            "border: 0px solid #999999;\n"
		                            "background:white;\n"
		                            "width:8px;\n"
		                            "margin: 0px 0px 0px 0px;\n"
		                            "}\n"
		                            "QScrollBar::handle:vertical {\n"
		                            "background: qlineargradient(x1:0, y1:0, x2:1, y2:0,\n"
		                            " stop: 0 rgb(32, 47, 130), stop: 0.5 rgb(32, 47, 130), stop:1 rgb(32, 47, 130));\n"
		                            " min-height: 10px;\n"
		                            "border-radius: 4px;\n"
		                            "}\n"
		                            "QScrollBar::add-line:vertical {\n"
		                            "height: 0px;\n"
		                            "subcontrol-position: bottom;\n"
		                            "subcontrol-origin: margin;\n"
		                            "}\n"
		                            "QScrollBar::sub-line:vertical {\n"
		                            "height: 0 px;\n"
		                            "subcontrol-position: top;\n"
		                            "subcontrol-origin: margin;\n"
		                            "}\n"
		                            "QTextEdit{\n"
		                            "border-radius: 20px;\n"
		                            "background: palette(base);\n"
		                            "padding-left: 5px;\n"
		                            "padding-right: 11px;\n"
		                            "padding-top: 8px;\n"
		                            "padding-bottom: 2px;\n"
		                            "}")
		self.textEdit.setPlaceholderText("Type a message")
		Form.setStyleSheet("background: url(:/new prefix/bg.png) cover no-repeat fixed;\n")
		self.client = wolframalpha.Client("UWVJ3J-WK9EQK9JT5")
		QMetaObject.connectSlotsByName(Form)

	def td(self):
		global ui

		t1 = Thread(target=ui.send())
		t1.start()
		t2 = Thread(target=ui.Mcond())
		t2.start()
		t1.join()
		t2.join()


import vrf_rc

if __name__ == "__main__":
	import sys

	app = QApplication(sys.argv)
	Form = QWidget()
	ui = Ui_Form()
	ui.setupUi(Form)
	Form.show()
	sys.exit(app.exec_())
