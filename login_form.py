import subprocess
import threading

from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import QMessageBox
import sqlite3
con = sqlite3.connect("userstore.db")
cur = con.cursor()
cur.execute("CREATE TABLE IF NOT EXISTS userstore(name varchar(255) primary key,nickname varhcar(255),password varchar(255),location varchar(255),gender varchar(255));")
con.commit()
cur.execute("select name from userstore;")
namelist = cur.fetchall()

    
    
    
class Ui_Form(object):
    
    def junc(self):
        login.show()
        for i in self.lll:
            i.setText("")
        
        Form1.hide()
        
#         app.quit()
    def appends(self):
        aa=1
        for i in namelist:
            if i[0]==self.username_2.text():
                aa=0
        if self.username_2.text()=="" or self.nickname.text()=="" or self.password_2.text()=="" or self.comboBox_2.currentText()=="" or self.gender_2.currentText()=="":
            self.pop1()

        elif self.password_2.text()==self.cpassword.text() and aa==1:
            self.ll.append(self.username_2.text())
            self.ll.append(self.nickname.text())
            self.ll.append(self.password_2.text())
            self.ll.append(self.comboBox_2.currentText())
            self.ll.append(self.gender_2.currentText())
            ss="insert into userstore values(?,?,?,?,?);"
            cur.execute(ss, self.ll)
            con.commit()
            self.pop2()
            self.junc()
            


        else:
            self.popop()
    def pop1(self):
        self.msg1=QMessageBox()
        self.msg1.setText("All the details are not filled.\nPlease try again")
        self.msg1.setIcon(QMessageBox.Critical)
        self.msg1.exec_()
    def pop2(self):
        self.msg2=QMessageBox()
        self.msg2.setText("User id created suscessfully")
        self.msg2.setIcon(QMessageBox.Information)
        self.msg2.exec_()
    def popop(self):
        self.msg=QMessageBox()
        self.msg.setText("Username is already taken or the password is not matching.\nPlease try again.")
        self.msg.setIcon(QMessageBox.Critical)
        self.msg.exec_()
    def setupUi(self, Form):
        self.ll,self.lll=[],[]

        Form.resize(582, 373)
        Form.setMinimumSize(QtCore.QSize(582, 373))
        Form.setMaximumSize(QtCore.QSize(582, 373))
        Form.setStyleSheet("background-color:rgb(114, 222, 255);")
        self.username = QtWidgets.QLabel(Form)
        self.username.setGeometry(QtCore.QRect(20, 70, 91, 16))
        self.username.setStyleSheet("font: 13pt \"Calibri\";")

        self.username_2 = QtWidgets.QLineEdit(Form)
        self.username_2.setGeometry(QtCore.QRect(20, 90, 241, 31))
        self.username_2.setStyleSheet("font: 14pt \"Calibri\";\n"
"background-color: rgb(255, 255, 255);\n"
"border-radius:10px;\n"
"padding:4px;")
        self.lll.append(self.username_2)
        self.submit = QtWidgets.QPushButton(Form)
        self.submit.setGeometry(QtCore.QRect(250, 310, 81, 31))
        self.submit.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"font: 17pt \"Calibri\";\n"
"border-radius:10px;")
        self.submit.clicked.connect(self.appends)
        self.password = QtWidgets.QLabel(Form)
        self.password.setGeometry(QtCore.QRect(20, 160, 81, 16))
        self.password.setStyleSheet("font: 13pt \"Calibri\";")
        
        self.password_2 = QtWidgets.QLineEdit(Form)
        self.password_2.setGeometry(QtCore.QRect(20, 180, 241, 31))
        self.password_2.setStyleSheet("font: 14pt \"Calibri\";\n"
"background-color: rgb(255, 255, 255);\n"
"border-radius:10px;\n"
"padding:4px;")
        self.password_2.setEchoMode(QtWidgets.QLineEdit.Password)
        self.lll.append(self.password_2)
        
        self.nickname_2 = QtWidgets.QLabel(Form)
        self.nickname_2.setGeometry(QtCore.QRect(320, 70, 81, 16))
        self.nickname_2.setStyleSheet("font: 13pt \"Calibri\";")

        self.Gender = QtWidgets.QLabel(Form)
        self.Gender.setGeometry(QtCore.QRect(20, 240, 61, 16))
        self.Gender.setStyleSheet("font: 13pt \"Calibri\";")

        self.gender_2 = QtWidgets.QComboBox(Form)
        self.gender_2.setGeometry(QtCore.QRect(20, 260, 151, 22))
        self.gender_2.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border-radius:5px;\n"
"padding:4px;\n"
"QComboBox QAbstractItemView\n"
"{\n"
"    border: 2px solid white;\n"
"    color: black;\n"
"    border-radius:10px;\n"
"    padding:3px;\n"
"    background-color: rgb(255, 255, 255);\n"
"}\n")

        self.gender_2.addItem("")
        self.gender_2.setItemText(0, "")
        self.gender_2.addItem("Male")
        self.gender_2.addItem("Female")
        self.gender_2.addItem("Other")
        self.location = QtWidgets.QLabel(Form)
        self.location.setGeometry(QtCore.QRect(320, 240, 71, 21))
        self.location.setStyleSheet("font: 13pt \"Calibri\";")

        self.comboBox_2 = QtWidgets.QComboBox(Form)
        self.comboBox_2.setGeometry(QtCore.QRect(320, 260, 151, 22))
        self.comboBox_2.setStyleSheet("QScrollBar:vertical {\n"
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
"QComboBox QAbstractItemView\n"
"{\n"
"    border: 2px solid white;\n"
"    color: black;\n"
"    border-radius:10px;\n"
"    padding:3px;\n"
"    background-color: rgb(255, 255, 255);\n"
"}\n"
"QComboBox{\n"
"background-color: rgb(255, 255, 255);\n"
"padding:4px;\n"
"border-radius:5px;}")

        self.comboBox_2.addItem("")
        self.comboBox_2.setItemText(0, "")
        self.comboBox_2.addItem("Ariyalur")
        self.comboBox_2.addItem("Chengalpattu")
        self.comboBox_2.addItem("Chennai")
        self.comboBox_2.addItem("Coimbatore")
        self.comboBox_2.addItem("Cuddalore")
        self.comboBox_2.addItem("Dharmapuri")
        self.comboBox_2.addItem("Dindigul")
        self.comboBox_2.addItem("Erode")
        self.comboBox_2.addItem("Kallakurichi")
        self.comboBox_2.addItem("Kanchipuram")
        self.comboBox_2.addItem("Kanyakumari")
        self.comboBox_2.addItem("Karur")
        self.comboBox_2.addItem("Krishnagiri")
        self.comboBox_2.addItem("Madurai")
        self.comboBox_2.addItem("Nagapattinam")
        self.comboBox_2.addItem("Namakkal")
        self.comboBox_2.addItem("Nilgiris")
        self.comboBox_2.addItem("Perambalur")
        self.comboBox_2.addItem("Pudukottai")
        self.comboBox_2.addItem("Ramanathapuram")
        self.comboBox_2.addItem("Ranipet")
        self.comboBox_2.addItem("Salem")
        self.comboBox_2.addItem("Sivaganga")
        self.comboBox_2.addItem("Tenkasi")
        self.comboBox_2.addItem("Thanjavur")
        self.comboBox_2.addItem("Theni")
        self.comboBox_2.addItem("Tuticorin")
        self.comboBox_2.addItem("Tiruchirappalli")
        self.comboBox_2.addItem("Tirunelveli")
        self.comboBox_2.addItem("Tirupathur")
        self.comboBox_2.addItem("Tiruppur")
        self.comboBox_2.addItem("Tiruvallur")
        self.comboBox_2.addItem("Tiruvannamalai")
        self.comboBox_2.addItem("Tiruvarur")
        self.comboBox_2.addItem("Vellore")
        self.comboBox_2.addItem("Viluppuram")
        self.comboBox_2.addItem("Virudhunagar")

        self.cpassword_2 = QtWidgets.QLabel(Form)
        self.cpassword_2.setGeometry(QtCore.QRect(320, 160, 141, 16))
        self.cpassword_2.setStyleSheet("font: 13pt \"Calibri\";")

        self.cpassword = QtWidgets.QLineEdit(Form)
        self.cpassword.setGeometry(QtCore.QRect(320, 180, 241, 31))
        self.cpassword.setStyleSheet("font: 14pt \"Calibri\";\n"
"background-color: rgb(255, 255, 255);\n"
"border-radius:10px;\n"
"padding:4px;")
        self.cpassword.setEchoMode(QtWidgets.QLineEdit.Password)

        self.nickname = QtWidgets.QLineEdit(Form)
        self.nickname.setGeometry(QtCore.QRect(320, 90, 241, 31))
        self.nickname.setStyleSheet("font: 14pt \"Calibri\";\n"
"background-color: rgb(255, 255, 255);\n"
"border-radius:10px;\n"
"padding:4px;")
        self.lll.append(self.cpassword)
        self.lll.append(self.nickname)
        
        self.headder = QtWidgets.QLabel(Form)
        self.headder.setGeometry(QtCore.QRect(240, 20, 101, 31))
        self.headder.setStyleSheet("font: 20pt \"MV Boli\";\n"
"text-decoration: underline;")


        
        Form.setTabOrder(self.username_2, self.nickname)
        Form.setTabOrder(self.nickname, self.password_2)
        Form.setTabOrder(self.password_2, self.cpassword)
        Form.setTabOrder(self.cpassword, self.gender_2)
        Form.setTabOrder(self.gender_2, self.comboBox_2)
        Form.setTabOrder(self.comboBox_2, self.submit)
        
        Form.setWindowTitle("Sign in")
        self.username.setText("Username ")
        self.username_2.setPlaceholderText("Enter a username")
        self.submit.setText("Submit")
        self.password.setText("Password")
        self.password_2.setPlaceholderText("Enter a Password")
        self.nickname_2.setText("Nickname")
        self.nickname.setPlaceholderText("Enter a Nickname")
        self.Gender.setText("Gender")
        self.location.setText("Location")
        self.cpassword_2.setText("Confirm Password")
        self.cpassword.setPlaceholderText("Re-enter the password")
        self.headder.setText("Sign up")
        
        self.pushButton = QtWidgets.QPushButton(Form)

        self.pushButton.setGeometry(QtCore.QRect(343, 352, 25, 16))

        self.pushButton.setStyleSheet("border:none;\n"
"background:none;")
        self.pushButton.clicked.connect(self.junc)

        self.label = QtWidgets.QLabel(Form)

        self.label.setGeometry(QtCore.QRect(212, 352, 125, 16))

        self.label.setObjectName("label")
        self.label.setText("Already have an account?")

        self.pushButton.setText("Login")
        self.pushButton.setStyleSheet("background-color: rgb(114, 222, 255);\n"
"font: 75 8pt \"MS Shell Dlg 2\";\n"
"color: rgb(8, 0, 124);\n"
"border:none;")

class log(object):
    def junction(self):
        login.hide()
        self.usered.setText("")
        self.passtd.setText("")
        Form1.show()
        
    def check(self):
        usr=self.usered.text()
        pasd=self.passtd.text()
        tu=(usr,pasd)
        cur.execute("select name,password from userstore;")
        if tu not in cur:
            self.popop()
        else:
            cur.execute("CREATE TABLE IF NOT EXISTS lastuser(name varchar(255));")
            con.commit()
            s = "INSERT into lastuser values(?);"
            cur.execute(s,[usr])
            con.commit()
            cur.close()
            con.close()
            aa=threading.Thread(target=self.tryshow)
            aa.start()
            login.hide()
    def tryshow(self):
        subprocess.call(["python", "splash.py"])
        subprocess.call(["python", "main.py"])

    def popop(self):
        self.msg = QMessageBox()
        self.msg.setText("Your Username or password is incorrect.\nPLease try again.")
        self.msg.setIcon(QMessageBox.Critical)
        self.msg.exec_()
    def setupUi(self, login):
        login.resize(454, 307)
        login.setMinimumSize(QtCore.QSize(454, 307))
        login.setMaximumSize(QtCore.QSize(454, 307))
        login.setStyleSheet("background-color: rgb(114, 222, 255);")
        login.setWindowTitle("Login")

        self.usered = QtWidgets.QLineEdit(login)
        self.usered.setGeometry(QtCore.QRect(91, 80, 271, 41))
        self.usered.setStyleSheet("border-radius:10px;\n"
"background-color: rgb(255, 255, 255);\n"
"padding:5px;\n"
"font: 12pt \"Calibri\";")
        self.usered.setPlaceholderText("Enter your Username")

        self.userlbl = QtWidgets.QLabel(login)
        self.userlbl.setGeometry(QtCore.QRect(90, 60, 101, 16))
        self.userlbl.setStyleSheet("font: 12pt \"Calibri\";")
        self.userlbl.setText("Username")
        self.passtd = QtWidgets.QLineEdit(login)
        self.passtd.setGeometry(QtCore.QRect(91, 160, 271, 41))
        self.passtd.setStyleSheet("border-radius:10px;\n"
"background-color: rgb(255, 255, 255);\n"
"padding:5px;\n"
"font: 12pt \"Calibri\";")
        self.passtd.setPlaceholderText("Enter your Password")
        self.passtd.setEchoMode(QtWidgets.QLineEdit.Password)
        self.passlbl = QtWidgets.QLabel(login)
        self.passlbl.setGeometry(QtCore.QRect(90, 140, 81, 16))
        self.passlbl.setStyleSheet("font: 12pt \"Calibri\";")
        self.passlbl.setText("Password")

        self.loglbl = QtWidgets.QLabel(login)
        self.loglbl.setGeometry(QtCore.QRect(200, 20, 61, 31))
        self.loglbl.setStyleSheet("font: 20pt \"Kalam\";")
        self.loglbl.setText("Login")

        self.submit = QtWidgets.QPushButton(login)
        self.submit.setGeometry(QtCore.QRect(180, 240, 81, 31))
        self.submit.setStyleSheet("border-radius:10px;\n"
"font: 14pt \"Calibri\";\n"
"background-color: rgb(255, 255, 255);\n"
"padding:5px;")
        self.submit.setDefault(False)
        self.submit.setText("Submit")
        self.submit.clicked.connect(self.check)
        self.signupbl = QtWidgets.QPushButton(login)
        self.signupbl.setGeometry(QtCore.QRect(245, 280, 41, 16))
        self.signupbl.setStyleSheet("background-color: rgb(114, 222, 255);\n"
"font: 75 8pt \"MS Shell Dlg 2\";\n"
"color: rgb(8, 0, 124);\n"
"border:none;")
        self.signupbl.setText("Sign-up")
        self.signupbl.clicked.connect(self.junction)

        self.label = QtWidgets.QLabel(login)
        self.label.setGeometry(QtCore.QRect(130, 280, 141, 16))
        self.label.setText("Don't have an account?")

        self.rem = QtWidgets.QCheckBox(login)
        self.rem.setGeometry(QtCore.QRect(100, 210, 151, 18))
        self.rem.setText("Remember on this device")

        login.setTabOrder(self.usered, self.passtd)
        login.setTabOrder(self.passtd, self.rem)
        login.setTabOrder(self.rem, self.submit)
        login.setTabOrder(self.submit, self.signupbl)

        self.signupbl.raise_()


class UiForm(object):
    def func(self):
        Form1.show()
        Form.hide()
    def func1(self):
        login.show()
        Form.hide()
        
    def setupgUi(self, Form):
        
        Form.resize(400, 250)
        Form.setMinimumSize(QtCore.QSize(400, 250))
        Form.setMaximumSize(QtCore.QSize(400, 250))
        Form.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(140, 130, 111, 31))
        self.pushButton.setStyleSheet("background-color: rgb(94, 145, 255);\n"
"border-radius:10px;\n"
"font: 14pt \"SWEET  DREAM\";")
        self.pushButton.setText("Login")
        self.pushButton_2 = QtWidgets.QPushButton(Form)
        self.pushButton_2.setGeometry(QtCore.QRect(140, 70, 111, 31))
        self.pushButton_2.setStyleSheet("background-color: rgb(94, 145, 255);\n"
"font: 14pt \"SWEET  DREAM\";\n"
"border-radius:10px;\n"
"")
        QtCore.QMetaObject.connectSlotsByName(Form)
        Form.setWindowTitle("Login form")
        self.pushButton_2.setText("sign up")
        self.pushButton_2.clicked.connect(self.func)
        self.pushButton.clicked.connect(self.func1)


import sys
app = QtWidgets.QApplication(sys.argv)
Form1 = QtWidgets.QWidget()
ui1 = Ui_Form()
ui1.setupUi(Form1)


app3 = QtWidgets.QApplication(sys.argv)
login = QtWidgets.QWidget()
ui3 = log()
ui3.setupUi(login)


if __name__ == "__main__":
    
    app1 = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = UiForm()
    ui.setupgUi(Form)
    Form.show()
    
    sys.exit(app1.exec_())

