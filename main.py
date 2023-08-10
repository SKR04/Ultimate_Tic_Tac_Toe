from datetime import datetime
# from MW import wtu,command,condition
import time
from PyQt5 import QtCore, QtGui, QtWidgets
import sys
from threading import Thread
import subprocess
import sqlite3


class Ui_MainWindow(QtWidgets.QMainWindow):
	def tchangepw(self):
		subprocess.call(["python","DB.py"])
	def changepw(self):
		cpw=Thread(target=self.tchangepw)
		cpw.start()
	def editor(self):
		global i,con,cur
		if self.nflag %2 == 0:

			self.Namelbl.hide()
			self.ldit=QtWidgets.QLineEdit(self.SMF1)
			font = QtGui.QFont()
			font.setPointSize(12)
			self.ldit.setFont(font)
			self.ldit.setGeometry(QtCore.QRect(70, 40, 211, 31))
			self.ldit.setPlaceholderText("Enter your new name")
			self.ldit.setStyleSheet("""background: palette(base);
border-radius: 6px;
""")
			self.ldit.show()
		else:
			nick = self.ldit.text()
			var = i[0][0]
			if nick.isspace() or len(nick) == 0:
				pass
			else:
				s = f"UPDATE userstore SET nickname = '{nick}' WHERE name = '{var}';"
				cur.execute(s)
				con.commit()
				self.ldit.hide()
				self.Namelbl.setText(nick)
				self.Namelbl.show()
		self.nflag += 1

	def swish(self):
		self.stackedWidget.setCurrentIndex(1)
		app.processEvents()
		wtu()
	def mine(self):
		d=Thread(target=self.mineshow)
		d.start()
	def mineshow(self):
		subprocess.call(["python","./minesweeper/minesweeper.py"])
	def ttt(self):
		c=Thread(target=self.tttshow)
		c.start()
	def tttshow(self):
		subprocess.call(["python","Tic_Tac_Toe.py"])
	def cht(self):
		b=Thread(target=self.chatbotshow)
		b.start()
	def chatbotshow(self):
		subprocess.call(["python","Chatscreen.py"])
	def stp(self):
		a= Thread(target=self.stopwatchshow)
		a.start()
	def stopwatchshow(self):
		subprocess.call(["python","Stopwatchf.py"])

	def swap0(self):
		self.stackedWidget.setCurrentIndex(0)
	def swap1(self):
		self.stackedWidget.setCurrentIndex(1)
	def sset(self):
		self.swap0()
		self.set_show()
	def set_show(self):
		# import sqlite3
		# con = sqlite3.connect("userstore.db")
		# cur = con.cursor()
		# cur.execute("select * from lastuser")

		if self.flag%2 == 0:
			self.SMenu.show()
			icon7 = QtGui.QIcon()
			if self.gender == "Male":
				icon7.addPixmap(QtGui.QPixmap(":new prefix/profile (1).png"),QtGui.QIcon.Normal, QtGui.QIcon.Off)
			else:
				icon7.addPixmap(QtGui.QPixmap(":new prefix/profile (2).png"),QtGui.QIcon.Normal, QtGui.QIcon.Off)
			self.pushButton_4.setIcon(icon7)
			self.anim = QtCore.QPropertyAnimation(self.SMenu,b'geometry')
			self.anim.setDuration(500)
			self.anim.setStartValue(QtCore.QRect(35,98,0,0))
			self.anim.setEndValue(QtCore.QRect(35,98,381,524))
			self.anim.start()

		else:

			self.anim1 = QtCore.QPropertyAnimation(self.SMenu, b'geometry')
			self.anim1.setDuration(500)
			self.anim1.setStartValue(QtCore.QRect(35, 98, 381, 524))
			self.anim1.setEndValue(QtCore.QRect(35, 98, 0, 0))
			self.anim1.start()
			# self.SMenu.hide()
		self.flag+=1
	def timeshow(self):
		today = datetime.today()
		date = today.strftime("%A, %B %d")
		time = today.strftime("%I:%M %p")
		self.fdate.setText(date)
		self.ftime.setText(time)

	def tvcsend(self):
		VLayout = QtWidgets.QVBoxLayout()
		lbl = QtWidgets.QLabel(self.scrollw)
		lbl.setMinimumSize(QtCore.QSize(31, 31))
		lbl.setSizePolicy(QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.MinimumExpanding))
		lbl.setLayoutDirection(QtCore.Qt.RightToLeft)
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
		lbl1 = QtWidgets.QLabel(self.scrollw)
		lbl1.setMaximumSize(QtCore.QSize(16777215, 16))
		lbl1.setMinimumSize(QtCore.QSize(45, 16))
		lbl1.setAlignment(QtCore.Qt.AlignLeading | QtCore.Qt.AlignRight | QtCore.Qt.AlignTop)
		text1 = datetime.now().strftime("%H:%M ")
		lbl1.setText(text1)
		lbl1.setStyleSheet("""background:transparent;
color:white;""")
		VLayout.addWidget(lbl1)
		VLayout.setSpacing(5)
		lll = QtWidgets.QLabel(self.scrollw)
		lll.setStyleSheet("background: transparent;")
		hlayout = QtWidgets.QHBoxLayout()
		hlayout.addWidget(lll,1)
		hlayout.addLayout(VLayout, 2)
		self.gridLayout.addLayout(hlayout, self.times, 0, 1, 1)
		self.marnum -= (lbl.height() + lbl1.height()+20)
		self.gridLayout.setContentsMargins(-1, self.marnum, -1, -1)
		self.times += 1
		app.processEvents()
		time.sleep(0)
	def command(self):
		self.text=command()
		self.tvcsend()
		self.vcreply()


	def vcreply(self):
		self.creply=condition(self.text)
		self.vctxt()
	def vctxt(self):
		lbl3 = QtWidgets.QLabel(self.scrollw)
		lbl3.setLayoutDirection(QtCore.Qt.LeftToRight)
		lbl3.setStyleSheet("border-radius: 10px;\n"
		                   "padding: 5px;\n"
		                   "background: white;"
		                   "font: 13px;")
		lbl3.setMaximumSize(338, 10000)
		lbl3.setText(self.creply)
		lbl3.adjustSize()
		lbl3.setWordWrap(True)
		wid = lbl3.frameGeometry().width()
		hgt = lbl3.frameGeometry().height()
		if hgt > 26:
			lbl3.setText("")
			lbl3.setWordWrap(False)
			lbl3.setText(self.creply)
			lbl3.setWordWrap(True)
			lbl3.adjustSize()
		else:
			lbl3.setFixedSize(wid, hgt)
		VLayout = QtWidgets.QVBoxLayout()
		VLayout.addWidget(lbl3)

		lbl4 = QtWidgets.QLabel(self.scrollw)
		lbl4.setMinimumSize(QtCore.QSize(45, 16))
		lbl4.setMaximumSize(QtCore.QSize(16777215, 16))
		lbl4.setAlignment(QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignTop)
		text1 = datetime.now().strftime(" %H:%M")
		lbl4.setText(text1)
		lbl4.setStyleSheet("""background: transparent;
color:white;""")
		VLayout.addWidget(lbl4)
		VLayout.setSpacing(5)
		lll = QtWidgets.QLabel(self.scrollw)
		lll.setStyleSheet("background: transparent;")
		hlayout = QtWidgets.QHBoxLayout()
		hlayout.addLayout(VLayout, 2)
		hlayout.addWidget(lll, 1)
		self.gridLayout.addLayout(hlayout, self.times, 0, 1, 1)
		self.marnum -= (lbl3.height() + lbl4.height())
		self.gridLayout.setContentsMargins(-1, self.marnum, -1, -1)
		self.times += 1
		app.processEvents()


	def setupUi(self, MainWindow):
		global con,cur,i
		self.nflag = 0
		self.flag,self.times,self.marnum = 0,0,390
		MainWindow.setObjectName("MainWindow")
		MainWindow.setEnabled(True)
		MainWindow.setGeometry(QtCore.QRect(500,50,450,650))
		MainWindow.setFixedSize(QtCore.QSize(450, 650))
		# MainWindow.setMaximumSize(QtCore.QSize(450, 651))
		font = QtGui.QFont()
		font.setFamily("Arial")
		MainWindow.setFont(font)
		self.centralwidget = QtWidgets.QWidget(MainWindow)
		self.centralwidget.setObjectName("centralwidget")
		self.stackedWidget = QtWidgets.QStackedWidget(self.centralwidget)
		self.stackedWidget.setGeometry(QtCore.QRect(0, 0, 451, 651))
		self.stackedWidget.setMaximumSize(QtCore.QSize(451, 651))
		self.stackedWidget.setStyleSheet("background-image: url(:/new prefix/MABG.png);")
		self.stackedWidget.setObjectName("stackedWidget")
		self.page = QtWidgets.QWidget()
		self.page.setObjectName("page")
		self.tictactoe = QtWidgets.QPushButton(self.page)
		self.tictactoe.setGeometry(QtCore.QRect(60, 473, 61, 61))
		self.tictactoe.setMinimumSize(QtCore.QSize(61, 61))
		self.tictactoe.setMaximumSize(QtCore.QSize(61, 61))
		self.tictactoe.setStyleSheet("""QPushButton{
background:transparent;
background:rgba(0, 0, 0,170);
border-radius: 10px;
border:5px solid transparent;
}
QPushButton:hover{
background:rgba(0, 0, 0,200);
border-radius: 10px;
}""")
		self.tictactoe.setText("")
		icon = QtGui.QIcon()
		icon.addPixmap(QtGui.QPixmap(":/new prefix/sm.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
		self.tictactoe.setIcon(icon)
		self.tictactoe.setIconSize(QtCore.QSize(64, 61))
		self.tictactoe.clicked.connect(self.ttt)
		self.minesweeper = QtWidgets.QPushButton(self.page)
		self.minesweeper.setGeometry(QtCore.QRect(330, 473, 61, 61))
		self.minesweeper.setMinimumSize(QtCore.QSize(61, 61))
		self.minesweeper.setMaximumSize(QtCore.QSize(61, 61))
		self.minesweeper.setStyleSheet("QPushButton{\n"
		                               "background:transparent;\n"
		                               "}\n"
		                               "QPushButton:hover{\n"
		                               "background:rgba(0, 0, 0,170);\n"
		                               "border-radius: 20px;\n"
		                               "}")
		self.minesweeper.setText("")
		icon1 = QtGui.QIcon()
		icon1.addPixmap(QtGui.QPixmap(":/new prefix/miner.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
		self.minesweeper.setIcon(icon1)
		self.minesweeper.setIconSize(QtCore.QSize(61, 61))
		self.minesweeper.clicked.connect(self.mine)

		self.stopwatch = QtWidgets.QPushButton(self.page)
		self.stopwatch.setGeometry(QtCore.QRect(130, 383, 61, 61))
		self.stopwatch.setMinimumSize(QtCore.QSize(61, 61))
		self.stopwatch.setMaximumSize(QtCore.QSize(61, 61))
		self.stopwatch.setStyleSheet("QPushButton{\n"
		                             "background:transparent;\n"
		                             "}\n"
		                             "QPushButton:hover{\n"
		                             "background:rgba(0, 0, 0,170);\n"
		                             "border-radius: 10px;\n"
		                             "}")
		self.stopwatch.setText("")
		icon2 = QtGui.QIcon()
		icon2.addPixmap(QtGui.QPixmap(":/new prefix/stp.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
		self.stopwatch.setIcon(icon2)
		self.stopwatch.setIconSize(QtCore.QSize(61, 61))
		self.stopwatch.clicked.connect(self.stp)

		self.chatobt = QtWidgets.QPushButton(self.page)
		self.chatobt.setGeometry(QtCore.QRect(260, 380, 70, 70))
		self.chatobt.setMinimumSize(QtCore.QSize(70, 70))
		self.chatobt.setMaximumSize(QtCore.QSize(61, 61))
		self.chatobt.setStyleSheet("QPushButton{\n"
		                           "background:transparent;\n"
		                           "}\n"
		                           "QPushButton:hover{\n"
		                           "background:rgba(0, 0, 0,170);\n"
		                           "border-radius: 20px;\n"
		                           "}")
		self.chatobt.setText("")
		icon3 = QtGui.QIcon()
		icon3.addPixmap(QtGui.QPixmap(":/new prefix/bot.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
		self.chatobt.setIcon(icon3)
		self.chatobt.setIconSize(QtCore.QSize(70, 70))
		self.chatobt.clicked.connect(self.cht)
		self.speak = QtWidgets.QPushButton(self.page)
		self.speak.setGeometry(QtCore.QRect(190, 550, 80, 61))
		self.speak.setMinimumSize(QtCore.QSize(61, 61))
		self.speak.setMaximumSize(QtCore.QSize(80, 61))
		self.speak.setStyleSheet("QPushButton{\n"
		                         "background:transparent;\n"
		                         "}\n"
		                         "QPushButton:hover{\n"
		                         "background:rgba(0, 0, 0,170);\n"
		                         "border-radius: 20px;\n"
		                         "}")
		self.speak.setText("")
		icon4 = QtGui.QIcon()
		icon4.addPixmap(QtGui.QPixmap(":/new prefix/vbutton.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
		self.speak.setIcon(icon4)
		self.speak.setIconSize(QtCore.QSize(80, 74))
		self.speak.clicked.connect(self.swish)
		self.fsettings = QtWidgets.QPushButton(self.page)
		self.fsettings.setGeometry(QtCore.QRect(410, 70, 31, 31))
		self.fsettings.setStyleSheet("QPushButton{\n"
		                             "background:transparent;\n"
		                             "}\n"
		                             "QPushButton:hover{\n"
		                             "background:rgba(255, 255, 255,170);\n"
		                             "border-radius: 8px;\n"
		                             "}")
		self.fsettings.setText("")
		icon5 = QtGui.QIcon()
		icon5.addPixmap(QtGui.QPixmap(":/new prefix/seth.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
		self.fsettings.setIcon(icon5)
		self.fsettings.setIconSize(QtCore.QSize(31, 31))
		self.fsettings.setObjectName("fsettings")
		self.ftime = QtWidgets.QLabel(self.page)
		self.ftime.setGeometry(QtCore.QRect(110, 210, 231, 61))
		font = QtGui.QFont()
		font.setFamily("BatmanForeverAlternate")
		font.setPointSize(25)
		self.ftime.setFont(font)
		self.ftime.setStyleSheet("border-radius: 20px;\n"
		                         "background:transparent;")
		self.ftime.setAlignment(QtCore.Qt.AlignCenter)
		self.fdate = QtWidgets.QLabel(self.page)
		self.fdate.setGeometry(QtCore.QRect(110, 270, 231, 20))
		timer=QtCore.QTimer(self)
		timer.timeout.connect(self.timeshow)
		timer.start(1000)
		font = QtGui.QFont()
		font.setFamily("Segoe Print")
		font.setPointSize(12)
		font.setBold(True)
		font.setWeight(75)
		self.fdate.setFont(font)
		self.fdate.setStyleSheet("background:transparent;")
		self.fdate.setAlignment(QtCore.Qt.AlignCenter)
		self.fheader = QtWidgets.QLabel(self.page)
		self.fheader.setGeometry(QtCore.QRect(75, 10, 301, 31))
		font = QtGui.QFont()
		font.setFamily("Starcraft")
		font.setPointSize(23)
		font.setBold(False)
		font.setItalic(False)
		font.setWeight(50)
		self.fheader.setFont(font)
		self.fheader.setStyleSheet("font: 23pt \"Starcraft\";\n"
		                           "background:transparent;")
		self.fheader.setAlignment(QtCore.Qt.AlignCenter)
		self.fheader.setObjectName("fheader")
		self.SMenu = QtWidgets.QFrame(self.page)
		self.SMenu.setGeometry(QtCore.QRect(35, 98, 381, 524))
		self.SMenu.setStyleSheet("background: rgba(24, 24, 24,1);")
		self.SMenu.setFrameShape(QtWidgets.QFrame.StyledPanel)
		self.SMenu.setFrameShadow(QtWidgets.QFrame.Raised)
		self.SMenu.setObjectName("SMenu")
		self.rdButton = QtWidgets.QPushButton(self.SMenu)
		self.rdButton.setGeometry(QtCore.QRect(230, 420, 131, 31))
		font = QtGui.QFont()
		font.setPointSize(10)
		font.setBold(True)
		font.setUnderline(False)
		font.setWeight(75)
		self.rdButton.setFont(font)
		self.rdButton.setStyleSheet("QPushButton{\n"
		                            "background: transparent;\n"
		                            "color: white;\n"
		                            "}\n"
		                            "QPushButton:hover{\n"
		                            "    text-decoration: underline;\n"
		                            "}")
		self.rdButton.clicked.connect(self.rest)
		self.cpButton = QtWidgets.QPushButton(self.SMenu)
		self.cpButton.setGeometry(QtCore.QRect(30, 420, 131, 31))
		font = QtGui.QFont()
		font.setPointSize(10)
		font.setBold(True)
		font.setUnderline(False)
		font.setWeight(75)
		self.cpButton.setFont(font)
		self.cpButton.setStyleSheet("QPushButton{\n"
		                            "border-radius: 5px;\n"
		                            "background: rgb(114, 137, 218);\n"
		                            "color: white;\n"
		                            "}\n"
		                            "QPushButton:hover{\n"
		                            "background:rgb(87, 106, 167);\n"
		                            "}")
		self.cpButton.clicked.connect(self.changepw)
		self.SMF4 = QtWidgets.QFrame(self.SMenu)
		self.SMF4.setGeometry(QtCore.QRect(0, 310, 381, 81))
		self.SMF4.setStyleSheet("QFrame{\n"
		                        "background: transparent;\n"
		                        "}\n"
		                        "QFrame:hover{\n"
		                        "background: black;\n"
		                        "}")
		self.SMF4.setFrameShape(QtWidgets.QFrame.Box)
		self.SMF4.setFrameShadow(QtWidgets.QFrame.Raised)
		self.SMF4.setObjectName("SMF4")
		self.Vollbl = QtWidgets.QLabel(self.SMF4)
		self.Vollbl.setGeometry(QtCore.QRect(70, 10, 51, 21))
		font = QtGui.QFont()
		font.setPointSize(11)
		self.Vollbl.setFont(font)
		self.Vollbl.setStyleSheet("background: transparent;\n"
		                          "color: white;")
		self.Vollbl.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
		self.Vollbl.setObjectName("Vollbl")
		self.horizontalSlider_2 = QtWidgets.QSlider(self.SMF4)
		self.horizontalSlider_2.setGeometry(QtCore.QRect(70, 35, 201, 20))
		self.horizontalSlider_2.setStyleSheet("QSlider{\n"
		                                      "background:transparent;\n"
		                                      "}\n"
		                                      "QSlider:handle{\n"
		                                      "border: 1px solid white;\n"
		                                      "background:rgba(24, 24, 24,1);\n"
		                                      "}\n"
		                                      "")
		self.horizontalSlider_2.setOrientation(QtCore.Qt.Horizontal)
		self.horizontalSlider_2.setObjectName("horizontalSlider_2")
		self.SMF1 = QtWidgets.QFrame(self.SMenu)
		self.SMF1.setGeometry(QtCore.QRect(0, 60, 381, 91))
		self.SMF1.setStyleSheet("QFrame{\n"
		                        "background: transparent;\n"
		                        "}\n"
		                        "QFrame:hover{\n"
		                        "background: black;\n"
		                        "}")
		self.SMF1.setFrameShape(QtWidgets.QFrame.Box)
		self.SMF1.setFrameShadow(QtWidgets.QFrame.Raised)
		self.SMF1.setObjectName("SMF1")
		self.label = QtWidgets.QLabel(self.SMF1)
		self.label.setGeometry(QtCore.QRect(70, 10, 51, 31))
		font = QtGui.QFont()
		font.setPointSize(11)
		self.label.setFont(font)
		self.label.setStyleSheet("background: transparent;\n"
		                         "color: white;")
		self.label.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
		self.label.setObjectName("label")
		self.Namelbl = QtWidgets.QLabel(self.SMF1)
		self.Namelbl.setGeometry(QtCore.QRect(70, 40, 211, 31))
		font = QtGui.QFont()
		font.setPointSize(12)
		self.Namelbl.setFont(font)
		self.Namelbl.setStyleSheet("background: transparent;\n"
		                           "border-radius: 5px;\n"
		                           "color: white;")
		self.Namelbl.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
		self.NEButton = QtWidgets.QPushButton(self.SMF1)
		self.NEButton.setGeometry(QtCore.QRect(290, 50, 21, 21))
		self.NEButton.setStyleSheet("QPushButton{\n"
		                            "background: transparent;\n"
		                            "}\n"
		                            "QFrame:hover{\n"
		                            "background: red;\n"
		                            "padding: 5px;\n"
		                            "}\n"
		                            "")
		self.NEButton.setText("")
		icon6 = QtGui.QIcon()
		icon6.addPixmap(QtGui.QPixmap(":/new prefix/pencil.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
		self.NEButton.setIcon(icon6)
		self.NEButton.setIconSize(QtCore.QSize(20, 20))
		self.NEButton.setObjectName("NEButton")
		self.NEButton.clicked.connect(self.editor)
		self.pushButton_4 = QtWidgets.QPushButton(self.SMF1)
		self.pushButton_4.setGeometry(QtCore.QRect(14, 28, 41, 41))
		self.pushButton_4.setStyleSheet("background:transparent;")
		self.pushButton_4.setText("")

		self.pushButton_4.setIconSize(QtCore.QSize(35, 35))
		self.pushButton_4.setObjectName("pushButton_4")
		self.SMHeader = QtWidgets.QLabel(self.SMenu)
		self.SMHeader.setGeometry(QtCore.QRect(105, 10, 171, 41))
		font = QtGui.QFont()
		font.setFamily("ROBO")
		font.setPointSize(25)
		self.SMHeader.setFont(font)
		self.SMHeader.setStyleSheet("background: transparent;\n"
		                            "color: white;")
		self.SMHeader.setAlignment(QtCore.Qt.AlignCenter)
		self.SMHeader.setObjectName("SMHeader")
		self.SMF3 = QtWidgets.QFrame(self.SMenu)
		self.SMF3.setGeometry(QtCore.QRect(0, 230, 381, 81))
		self.SMF3.setStyleSheet("QFrame{\n"
		                        "background: transparent;\n"
		                        "}\n"
		                        "QFrame:hover{\n"
		                        "background: black;\n"
		                        "}")
		self.SMF3.setFrameShape(QtWidgets.QFrame.Box)
		self.SMF3.setFrameShadow(QtWidgets.QFrame.Raised)
		self.SMF3.setObjectName("SMF3")
		self.Speedlbl = QtWidgets.QLabel(self.SMF3)
		self.Speedlbl.setGeometry(QtCore.QRect(70, 10, 51, 21))
		font = QtGui.QFont()
		font.setPointSize(11)
		self.Speedlbl.setFont(font)
		self.Speedlbl.setStyleSheet("background: transparent;\n"
		                            "color: white;")
		self.Speedlbl.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
		self.Speedlbl.setObjectName("Speedlbl")
		self.horizontalSlider = QtWidgets.QSlider(self.SMF3)
		self.horizontalSlider.setGeometry(QtCore.QRect(70, 36, 201, 20))
		self.horizontalSlider.setStyleSheet("QSlider{\n"
		                                    "background:transparent;\n"
		                                    "}\n"
		                                    "QSlider:handle{\n"
		                                    "border: 1px solid white;\n"
		                                    "background:rgba(24, 24, 24,1);\n"
		                                    "}")
		self.horizontalSlider.setOrientation(QtCore.Qt.Horizontal)
		self.horizontalSlider.setObjectName("horizontalSlider")
		self.SMF2 = QtWidgets.QFrame(self.SMenu)
		self.SMF2.setGeometry(QtCore.QRect(0, 150, 381, 81))
		self.SMF2.setStyleSheet("QFrame{\n"
		                        "background: transparent;\n"
		                        "}\n"
		                        "QFrame:hover{\n"
		                        "background: black;\n"
		                        "}")
		self.SMF2.setFrameShape(QtWidgets.QFrame.Box)
		self.SMF2.setFrameShadow(QtWidgets.QFrame.Raised)
		self.SMF2.setObjectName("SMF2")
		self.Voicelbl = QtWidgets.QLabel(self.SMF2)
		self.Voicelbl.setGeometry(QtCore.QRect(70, 10, 51, 31))
		font = QtGui.QFont()
		font.setPointSize(11)
		self.Voicelbl.setFont(font)
		self.Voicelbl.setStyleSheet("background: transparent;\n"
		                            "color: white;")
		self.Voicelbl.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
		self.Voicelbl.setObjectName("Voicelbl")
		self.VoiceBox_2 = QtWidgets.QComboBox(self.SMF2)
		self.VoiceBox_2.setGeometry(QtCore.QRect(70, 40, 111, 22))
		self.VoiceBox_2.setStyleSheet("background-color: white;\n"
		                              "color: black;")
		self.VoiceBox_2.setObjectName("VoiceBox_2")
		self.VoiceBox_2.currentTextChanged.connect(self.tqbo)
		self.VoiceBox_2.addItem("Male")
		self.VoiceBox_2.addItem("Female")
		self.stackedWidget.addWidget(self.page)
		self.page_2 = QtWidgets.QWidget()
		self.page_2.setMinimumSize(QtCore.QSize(451, 651))
		self.page_2.setMaximumSize(QtCore.QSize(451, 651))
		self.page_2.setStyleSheet("background: url(:/new prefix/Vabg.png) NO-REPEAT CENTER FIXED;")
		self.page_2.setObjectName("page_2")
		self.shome = QtWidgets.QPushButton(self.page_2)
		self.shome.setGeometry(QtCore.QRect(10, 60, 31, 31))
		self.shome.setStyleSheet("QPushButton{\n"
		                         "background:transparent;\n"
		                         "}\n"
		                         "QPushButton:hover{\n"
		                         "background:rgba(255, 255, 255,170);\n"
		                         "border-radius: 10px;\n"
		                         "}")
		self.shome.setText("")
		icon8 = QtGui.QIcon()
		icon8.addPixmap(QtGui.QPixmap(":/new prefix/home.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
		self.shome.setIcon(icon8)
		self.shome.setIconSize(QtCore.QSize(25, 25))
		self.shome.clicked.connect(self.swap0)

		self.scrollArea = QtWidgets.QScrollArea(self.page_2)
		self.scrollArea.setGeometry(QtCore.QRect(10, 100, 431, 461))
		self.scrollArea.setStyleSheet("""QWidget{
background: transparent;
}
QScrollBar:vertical {
background: transparent;
width: 10px;
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
}""")
		self.scrollArea.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
		self.scrollArea.setWidgetResizable(True)
		self.scrollArea.setObjectName("scrollArea")
		self.scrollw = QtWidgets.QWidget()
		self.scrollw.setGeometry(QtCore.QRect(0, 0, 427, 457))
		self.gridLayout = QtWidgets.QGridLayout(self.scrollw)
		self.gridLayout.setContentsMargins(-1, self.marnum, -1, -1)
		self.gridLayout.setObjectName("gridLayout")
		self.verticalLayout = QtWidgets.QVBoxLayout()
		self.verticalLayout.setSpacing(2)
		self.ssentr = QtWidgets.QLabel(self.scrollw)
		self.ssentr.setFixedSize(QtCore.QSize(200, 40))
		font = QtGui.QFont()
		font.setPointSize(10)
		self.ssentr.setFont(font)
		self.ssentr.setStyleSheet("border-radius: 10%;\n"
		                          "padding: 2px;\n"
		                          "background: white;")
		self.ssentr.setWordWrap(True)
		self.ssentr.adjustSize()
		self.ssentr.setText(f"hi i am vimal how may i help you")
		self.verticalLayout.addWidget(self.ssentr)
		self.stimer = QtWidgets.QLabel(self.scrollw)
		self.stimer.setMaximumSize(QtCore.QSize(16777215, 16))
		self.stimer.setStyleSheet("color:white;")
		text2 = datetime.now().strftime(" %H:%M")
		self.stimer.setText(text2)
		self.verticalLayout.addWidget(self.stimer)
		self.gridLayout.addLayout(self.verticalLayout, self.times, 0, 1, 1)
		self.times+=1
		self.scrollArea.setWidget(self.scrollw)
		self.sspeak = QtWidgets.QPushButton(self.page_2)
		self.sspeak.setGeometry(QtCore.QRect(180, 570, 90, 61))
		self.sspeak.setStyleSheet("QPushButton{\n"
		                          "background: transparent;\n"
		                          "}\n"
		                          "QPushButton:hover{\n"
		                          "background:rgba(0, 0, 0,170);\n"
		                          "border-radius: 20px;\n"
		                          "}")
		self.sspeak.setText("")
		self.sspeak.setIcon(icon4)
		self.sspeak.setIconSize(QtCore.QSize(80, 80))
		self.sspeak.clicked.connect(self.command)
		self.ssetting = QtWidgets.QPushButton(self.page_2)
		self.ssetting.setGeometry(QtCore.QRect(410, 60, 31, 31))
		self.ssetting.setStyleSheet("QPushButton{\n"
		                            "background:transparent;\n"
		                            "}\n"
		                            "QPushButton:hover{\n"
		                            "background:rgba(255, 255, 255,170);\n"
		                            "border-radius: 10px;\n"
		                            "}")
		self.ssetting.setText("")
		icon9 = QtGui.QIcon()
		icon9.addPixmap(QtGui.QPixmap(":/new prefix/set.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
		self.ssetting.setIcon(icon9)
		self.ssetting.setIconSize(QtCore.QSize(25, 25))
		self.ssetting.clicked.connect(self.sset)
		self.sheader = QtWidgets.QLabel(self.page_2)
		self.sheader.setGeometry(QtCore.QRect(50, 14, 350, 31))
		font = QtGui.QFont()
		font.setFamily("Starcraft")
		font.setPointSize(22)
		self.sheader.setFont(font)
		self.sheader.setStyleSheet("background: transparent;\n"
		                           "color: #C9D5D7;")
		self.sheader.setAlignment(QtCore.Qt.AlignCenter)
		self.sheader.setObjectName("sheader")
		self.stackedWidget.addWidget(self.page_2)
		MainWindow.setCentralWidget(self.centralwidget)
		self.SMenu.hide()
		self.fsettings.clicked.connect(self.set_show)

		self.retranslateUi(MainWindow)
		self.stackedWidget.setCurrentIndex(0)

		con = sqlite3.connect("userstore.db")
		cur = con.cursor()
		cur.execute("select * from lastuser;")
		a = cur.fetchall()
		var = "select * from userstore where name = ?;"
		cur.execute(var, list(a[-1]))
		i = cur.fetchall()
		self.gender = i[0][-1]
		self.namess = i[0][1]
		self.Namelbl.setText(self.namess)
		self.horizontalSlider.setRange(100,300)
		self.horizontalSlider.setValue(175)
		self.horizontalSlider_2.setRange(0,10)
		self.horizontalSlider_2.setValue(10)
		self.horizontalSlider.valueChanged.connect(self.sld)
		self.horizontalSlider_2.valueChanged.connect(self.vld)
		self.opacity = QtWidgets.QGraphicsOpacityEffect()
		self.opacity.setOpacity(0.888)
		self.SMenu.setGraphicsEffect(self.opacity)
		self.label_4 = QtWidgets.QLabel(self.scrollw)
		self.label_4.setText("")
		self.gridLayout.addWidget(self.label_4, 0, 1, 1, 1)
		QtCore.QMetaObject.connectSlotsByName(MainWindow)
	def qbo(self):
		from MW import adjusta
		if self.VoiceBox_2.currentText() == "Male":
			adjusta(0)
		else:
			adjusta(1)
	def tqbo(self):
		bo=Thread(target=self.qbo)
		bo.start()
	def tsld(self):
		from MW import adjustr
		adjustr(self.horizontalSlider.value())
	def sld(self):
		sl=Thread(target=self.tsld)
		sl.start()
	def tvld(self):
		from MW import adjustv
		adjustv(self.horizontalSlider_2.value()/10)
	def vld(self):
		dl = Thread(target=self.tvld)
		dl.start()
	def rest(self):
		self.horizontalSlider_2.setValue(10)
		self.horizontalSlider.setValue(175)
		self.tvld()
		self.tsld()
	def retranslateUi(self, MainWindow):
		_translate = QtCore.QCoreApplication.translate
		MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
		self.fheader.setText(_translate("MainWindow", "AI Assistant"))
		self.rdButton.setText(_translate("MainWindow", "Restore Defaults"))
		self.cpButton.setText(_translate("MainWindow", "Change Password"))
		self.Vollbl.setText(_translate("MainWindow", "Volume"))
		self.label.setText(_translate("MainWindow", "Name"))
		self.SMHeader.setText(_translate("MainWindow", "Settings"))
		self.Speedlbl.setText(_translate("MainWindow", "Speed"))
		self.Voicelbl.setText(_translate("MainWindow", "Voice"))
		self.sheader.setText(_translate("MainWindow", "Voice assistant"))
# import vrf_rc


if __name__ == "__main__":
	import sys
	app = QtWidgets.QApplication(sys.argv)
	MainWindow = QtWidgets.QMainWindow()
	ui = Ui_MainWindow()
	ui.setupUi(MainWindow)
	MainWindow.show()
	sys.exit(app.exec_())
