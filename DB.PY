from PyQt5 import QtCore, QtGui, QtWidgets
import sqlite3
from PyQt5.QtWidgets import QMessageBox


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(380, 280)
        Form.setStyleSheet("background-color: rgb(100, 102, 106);")
        self.lineEdit = QtWidgets.QLineEdit(Form)
        self.lineEdit.setGeometry(QtCore.QRect(15, 100, 260, 33))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lineEdit.setFont(font)
        self.lineEdit.setStyleSheet("QLineEdit{\n"
"border: 1px solid rgb(75, 75, 75);\n"
"border-radius: 5px;\n"
"background: rgb(48, 51, 56);\n"
"color:white;\n"
"}\n"
"QLineEdit:hover{\n"
"border: 1px solid black;\n"
"}")
        self.lineEdit.setEchoMode(QtWidgets.QLineEdit.Password)
        self.lineEdit.setObjectName("lineEdit")
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(15, 70, 131, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label.setFont(font)
        self.label.setStyleSheet("color: white;")
        self.label.setObjectName("label")
        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setGeometry(QtCore.QRect(15, 150, 101, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("color:white;")
        self.label_3.setObjectName("label_3")
        self.lineEdit_2 = QtWidgets.QLineEdit(Form)
        self.lineEdit_2.setGeometry(QtCore.QRect(15, 180, 261, 33))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lineEdit_2.setFont(font)
        self.lineEdit_2.setStyleSheet("QLineEdit{\n"
"border: 1px solid rgb(75, 75, 75);\n"
"border-radius: 5px;\n"
"background: rgb(48, 51, 56);\n"
"color:white;\n"
"}\n"
"QLineEdit:hover{\n"
"border: 1px solid black;\n"
"}\n"
"")
        self.lineEdit_2.setEchoMode(QtWidgets.QLineEdit.Password)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(60, 30, 271, 20))
        font = QtGui.QFont()
        font.setFamily("ROBO")
        font.setPointSize(19)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("color: white;")
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(210, 240, 75, 23))
        self.pushButton.setStyleSheet("QPushButton{\n"
"color:white;\n"
"border-radius:8px;\n"
"background:rgb(49, 52, 57);\n"
"}\n"
"QPushButton:hover{\n"
"background:rgb(25, 30, 29);\n"
"}")
        self.pushButton.clicked.connect(self.funt)
        self.pushButton_2 = QtWidgets.QPushButton(Form)
        self.pushButton_2.setGeometry(QtCore.QRect(290, 240, 75, 23))
        self.pushButton_2.setStyleSheet("QPushButton{\n"
"color:white;\n"
"border-radius:8px;\n"
"background:rgb(49, 52, 57);\n"
"}\n"
"QPushButton:hover{\n"
"background:rgb(25, 30, 29);\n"
"}")
        self.pushButton_2.clicked.connect(self.close)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)
    def close(self):
        app.close()
    def funt(self):
        print("hi")
        con = sqlite3.connect("userstore.db")
        cur = con.cursor()
        op = self.lineEdit.text()
        np = self.lineEdit_2.text()
        cur.execute("select * from lastuser;")
        i = cur.fetchall()
        usr = list(i[-1])
        cur.execute(f"select password from userstore where name = '{usr[0]}'")
        resu = cur.fetchall()
        print(resu[0][0])

        if self.lineEdit.text().isspace() or len(self.lineEdit.text()) == 0:
            pass

        elif resu[0][0] != op:
            self.notmatch()
            Form.hide()
        elif len(np) == 0 or np.isspace():
            self.empty()
            Form.hide()
        else:
            cur.execute(f"UPDATE userstore SET password = '{np}' where name = '{usr[0]}';")
            con.commit()
            self.csuccess()
            Form.hide()
    def empty(self):
        self.msg1 = QMessageBox()
        self.msg1.setText("Password can not be empty")
        self.msg1.setIcon(QMessageBox.Critical)
        self.msg1.exec_()

    def notmatch(self):
        self.msg = QMessageBox()
        self.msg.setText("Incorrect password")
        self.msg.setIcon(QMessageBox.Critical)
        self.msg.exec_()

    def csuccess(self):
        self.msg11 = QMessageBox()
        self.msg11.setText("Password changed Sucessfully")
        self.msg11.setIcon(QMessageBox.Information)
        self.msg11.exec_()
    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.lineEdit.setPlaceholderText(_translate("Form", " Enter your current password"))
        self.label.setText(_translate("Form", "CURRENT PASSWORD"))
        self.label_3.setText(_translate("Form", "NEW PASSWORD"))
        self.lineEdit_2.setPlaceholderText(_translate("Form", " Enter your new password"))
        self.label_2.setText(_translate("Form", "Change Password"))
        self.pushButton.setText(_translate("Form", "OK"))
        self.pushButton_2.setText(_translate("Form", "Cancel"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
