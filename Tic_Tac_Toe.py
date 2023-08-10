from PyQt5 import QtCore, QtGui, QtWidgets
import random

class TTT_Form(QtWidgets.QMainWindow):
    def ai(self,Mboard):
        if self.player==2:
            pv = 'O'
            cv = 'X'
        else: 
            pv = 'X'
            cv = 'O'
        if Mboard == [['X','',''],['','O',''],['','','X']]\
         or Mboard == [['','','X'],['','O',''],['X','','']]:
            return self.chooseRandom(Mboard, [[0,1],[1,0],[1,2],[2,1]]) 
        for i in range(3):
            for j in range(3):
                board = self.copy_board()
                if board[i][j] == '':
                    board[i][j] = cv
                    if self.AiCheckWin(board,cv):
                        return [i,j]
        for i in range(3):
            for j in range(3):
                board = self.copy_board()
                if board[i][j] == '':
                    board[i][j] = pv
                    if self.AiCheckWin(board,pv):
                        
                        return [i,j]
                    
        if Mboard[1][1] == '':
            return [1,1]
        move = self.chooseRandom(Mboard,[[0,0],[0,2],[2,0],[2,2]])
        if move != None:
            return move
        
        return self.chooseRandom(Mboard, [[0,1],[1,0],[1,2],[2,1]])
    def chooseRandom(self,board,list_):
        pm = []
        for i in list_:
            if board[i[0]][i[1]] == '':
                pm.append(i)
        if len(pm)!=0:
            return random.choice(pm)
        else:
            return None
    def AiCheckWin(self,bo,var):
        for i in range(3): 
            if bo[0][i] == bo[1][i] and bo[0][i] == bo[2][i] and bo[0][i] != '' and bo[0][i] == var: 
                return True
# Row Check
            if bo[i][0] == bo[i][1] and bo[i][0] == bo[i][2] and bo[i][0] != '' and bo[i][0] == var: 
                return True 
# Diagonal Check
        if bo[0][0] == bo[1][1] and bo[0][0] == bo[2][2] and bo[0][0] != '' and bo[0][0] == var: 
            return True
# if other diagonal is crossed 
        if bo[0][2] == bo[1][1] and bo[1][1] == bo[2][0] and bo[0][2] != '' and bo[0][2] == var: 
            return True
        return False
        
    def copy_board(self):
        s = self.temp[:]
        ja = [['','',''],['','',''],['','','']]
        for i in range(3):
            for j in range(3):
                if s[i][j].text() != '':
                    ja[i][j] = s[i][j].text()
        return ja
    
    def single_player(self):
        
        lst = ["Player 1 (X)","Player 2 (O)"]
        self.dialog = QtWidgets.QInputDialog()
        self.player,cond = self.dialog.getItem(self, "Choose player", "Choose your player:", lst)
        
        if cond == False or self.player not in lst:
            self.stackedWidget.setCurrentIndex(0)
        else:
            for i in self.temp:
                for j in i:
                    j.setEnabled(True)
            self.player = int(self.player[-5])
            #conditions for single player game 
            if self.player == 2:
                self.label.setText("Computer's Turn")
                loop = QtCore.QEventLoop()
                QtCore.QTimer.singleShot(750, loop.quit)
                loop.exec_()
                self.comp_move()
            else:
                self.label.setText("Player, your Turn")
                
            
    def multi_player(self):
        self.label.setText("Player X your turn")
        self.P2Header.setText("MULTIPLAYER")
        for i in self.temp:
            for j in i:
                j.setEnabled(True)
        #UNIQUE CONDITIONS
    def clear_all(self):
        for i in range(3):
            for j in range(3):
                self.temp[i][j].setEnabled(False)
    def Mode(self):
        sender = self.sender()
        self.mode = sender.text()
        self.P2Header.setText(self.mode)
        self.stackedWidget.setCurrentIndex(1)     
        if self.mode == 'SINGLE-PLAYER':          
            self.single_player()                  
        else:                                     
            self.multi_player()                   
                                                  
    def options(self,sender):                     
        for i in self.opt:                        
            if i == sender:                       
                self.opt.remove(i)                
    def Reset(self):
        self.opt = []
        for i in self.temp:
            for j in i:
                j.setEnabled(True)
                j.setText("")
                j.setStyleSheet("")
                self.opt.append(j)
        self.flag = 0
        self.label.setText('')
        if self.mode == 'SINGLE-PLAYER':
            self.single_player()
        else:
            self.multi_player()
        
    def BACK(self):
        self.opt = []
        for i in self.temp:
            for j in i:
                j.setEnabled(False)
                j.setText("")
                j.setStyleSheet("")
                self.opt.append(j)
        self.flag = 0
        self.flag1 = 0
        self.mode = ''
        self.stackedWidget.setCurrentIndex(0)
        
    
    
    def check_win(self):
        
# Column Check
        for i in range(3): 
            if self.temp[0][i].text() == self.temp[1][i].text() \
            and self.temp[0][i].text() == self.temp[2][i].text() \
            and self.temp[0][i].text() != "": 
                self.clear_all()
                return self.temp[0][i].text()
# Row Check
            if self.temp[i][0].text() == self.temp[i][1].text() \
            and self.temp[i][0].text() == self.temp[i][2].text() \
            and self.temp[i][0].text() != "": 
                self.clear_all()
                return self.temp[i][0].text() 
# Diagonal Check
        if self.temp[0][0].text() == self.temp[1][1].text() \
        and self.temp[0][0].text() == self.temp[2][2].text() \
        and self.temp[0][0].text() != "": 
            self.clear_all()
            return self.temp[0][0].text()
# if other diagonal is crossed 
        if self.temp[0][2].text() == self.temp[1][1].text() \
        and self.temp[1][1].text() == self.temp[2][0].text() \
        and self.temp[0][2].text() != "": 
            self.clear_all()
            return self.temp[0][2].text()
        return False
    def main_prog(self):

        sender = self.sender()
        if self.flag%2 == 0:
            mark = 'X'
            sender.setStyleSheet("""background-color: rgb(35, 35, 35);\n
color: red;""")
        else:
            mark = 'O'
            sender.setStyleSheet("""background-color: rgb(35, 35, 35);\n
color: rgb(83, 71, 255);""")
        self.flag += 1
        sender.setText(mark)
        sender.setEnabled(False)
        result = self.check_win()
        if result != False:
            self.label.setText(result+" won the game")
            return
        elif self.flag == 9:
            self.label.setText("Match is draw")
            return
        if self.mode == 'SINGLE-PLAYER':
            self.label.setText("Computer's turn")
            self.options(sender)
            loop = QtCore.QEventLoop()
            QtCore.QTimer.singleShot(500, loop.quit)
            loop.exec_()
            #computer's move
            self.comp_move()
        else:
            if mark == 'O':
                self.label.setText("Player X, your turn")
            else:
                self.label.setText("Player O, your turn")
    def comp_move(self):

        self.Mboard = self.copy_board()

        var = self.ai(self.Mboard)

        sender = self.temp[var[0]][var[1]]

        self.options(sender)
        if self.flag%2 == 0:
            mark = 'X'
            sender.setStyleSheet("""background-color: rgb(35, 35, 35);\n
color: red;""")
        else:
            mark = 'O'
            sender.setStyleSheet("""background-color: rgb(35, 35, 35);\n
color: rgb(83, 71, 255);""")
        sender.setText(mark)
        sender.setEnabled(False)
        self.flag+=1
        result = self.check_win()
        if result != False:
            self.label.setText("Computer wins")
            return
        elif self.flag == 9:
            self.label.setText("Match is draw")
            return
        self.label.setText("Player, Your Turn")   
    
    def setupUi(self, Form, app):
        self.flag1 = 0
        self.flag = 0
        self.mode = ''
        self.temp1,self.temp2,self.temp3,self.temp,self.opt = [],[],[],[],[]
        Form.resize(351, 501)
        Form.setMaximumSize(QtCore.QSize(351, 501))
        
        self.stackedWidget = QtWidgets.QStackedWidget(Form)
        self.stackedWidget.setGeometry(QtCore.QRect(0, 0, 351, 501))
        self.stackedWidget.setStyleSheet("background-color: rgb(69,69,69);")
        
        self.page_1 = QtWidgets.QWidget()
        self.page_1.setStyleSheet("background:  black;")
        self.page_1.setObjectName("page_1")
        
        self.PushB1 = QtWidgets.QPushButton(self.page_1)
        self.PushB1.setGeometry(QtCore.QRect(60, 196, 231, 51))
        font = QtGui.QFont()
        font.setFamily("ROBO")
        font.setPointSize(16)
        self.PushB1.setFont(font)
        self.PushB1.setStyleSheet("QPushButton{\n"
"background: rgb(0, 255, 0);\n"
"border-radius: 6px;\n"
"}\n"
"QPushButton:hover{\n"
"background:rgb(157, 65, 188);\n"
"}\n"
"QPushButton:pressed{\n"
"border: 7px solid black;\n"
"border-radius: 12px;\n"
"}")
        self.PushB1.clicked.connect(self.Mode)
        
        
        
        self.PushB2 = QtWidgets.QPushButton(self.page_1)
        self.PushB2.setGeometry(QtCore.QRect(60, 322, 231, 51))
        font = QtGui.QFont()
        font.setFamily("ROBO")
        font.setPointSize(16)
        self.PushB2.setFont(font)
        self.PushB2.setStyleSheet("QPushButton{\n"
"background: rgb(0, 255, 0);\n"
"border-radius: 6px;\n"
"}\n"
"QPushButton:hover{\n"
"background:rgb(157, 65, 188);\n"
"}\n"
"QPushButton:pressed{\n"
"border: 7px solid black;\n"
"border-radius: 12px;\n"
"}")
        self.PushB2.clicked.connect(self.Mode)
        
        
        
        self.P1Header = QtWidgets.QLabel(self.page_1)
        self.P1Header.setGeometry(QtCore.QRect(40, 40, 271, 51))
        font = QtGui.QFont()
        font.setFamily("Starcraft")
        font.setPointSize(24)
        self.P1Header.setFont(font)
        self.P1Header.setStyleSheet("background-color: rgb(0, 255, 0);\n"
"border-radius: 10px;")
        self.P1Header.setAlignment(QtCore.Qt.AlignCenter)
        
        
        self.stackedWidget.addWidget(self.page_1)
        
        
        self.page_2 = QtWidgets.QWidget()
        
        
        self.reset = QtWidgets.QPushButton(self.page_2)
        self.reset.setGeometry(QtCore.QRect(26, 430, 101, 41))
        font = QtGui.QFont()
        font.setFamily("ROBO")
        font.setPointSize(15)
        self.reset.setFont(font)
        self.reset.setStyleSheet("QPushButton{\n"
"border:3px solid rgb(255, 114, 42);\n"
"color:cyan;\n"
"background-color: dark grey;\n"
"border-radius: 10px;\n"
"}\n"
"QPushButton:hover{\n"
"border: 3px solid cyan ;\n"
"color:rgb(255, 114, 42);\n"
"}\n"
"QPushButton:pressed{\n"
"border:4px solid cyan;\n"
"}")
        self.reset.clicked.connect(self.Reset)
        
        
        self.layoutWidget = QtWidgets.QWidget(self.page_2)
        self.layoutWidget.setGeometry(QtCore.QRect(45, 100, 261, 261))
        
        
        self.MGLayout = QtWidgets.QGridLayout(self.layoutWidget)
        self.MGLayout.setContentsMargins(0, 0, 0, 0)
        
        
        self.pb1 = QtWidgets.QPushButton(self.layoutWidget)
        self.pb1.setEnabled(False)
        self.pb1.setMinimumSize(QtCore.QSize(81, 81))
        self.pb1.setMaximumSize(QtCore.QSize(81, 81))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(28)
        font.setBold(True)
        font.setWeight(75)
        self.pb1.setFont(font)
        self.MGLayout.addWidget(self.pb1, 0, 0, 1, 1)
        self.temp1.append(self.pb1)
        self.pb1.clicked.connect(self.main_prog)
        
        
        self.pb2 = QtWidgets.QPushButton(self.layoutWidget)
        self.pb2.setEnabled(False)
        self.pb2.setMinimumSize(QtCore.QSize(81, 81))
        self.pb2.setMaximumSize(QtCore.QSize(81, 81))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(28)
        font.setBold(True)
        font.setWeight(75)
        self.pb2.setFont(font)
        self.MGLayout.addWidget(self.pb2, 0, 1, 1, 1)
        self.temp1.append(self.pb2)
        self.pb2.clicked.connect(self.main_prog)
        
        self.pb3 = QtWidgets.QPushButton(self.layoutWidget)
        self.pb3.setEnabled(False)
        self.pb3.setMinimumSize(QtCore.QSize(81, 81))
        self.pb3.setMaximumSize(QtCore.QSize(81, 81))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(28)
        font.setBold(True)
        font.setWeight(75)
        self.pb3.setFont(font)
        self.MGLayout.addWidget(self.pb3, 0, 2, 1, 1)
        self.temp1.append(self.pb3)
        self.pb3.clicked.connect(self.main_prog)
        
        self.pb4 = QtWidgets.QPushButton(self.layoutWidget)
        self.pb4.setEnabled(False)
        self.pb4.setMinimumSize(QtCore.QSize(81, 81))
        self.pb4.setMaximumSize(QtCore.QSize(81, 81))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(28)
        font.setBold(True)
        font.setWeight(75)
        self.pb4.setFont(font)
        self.MGLayout.addWidget(self.pb4, 1, 0, 1, 1)
        self.temp2.append(self.pb4)
        self.pb4.clicked.connect(self.main_prog)
        
        self.pb5 = QtWidgets.QPushButton(self.layoutWidget)
        self.pb5.setEnabled(False)
        self.pb5.setMinimumSize(QtCore.QSize(81, 81))
        self.pb5.setMaximumSize(QtCore.QSize(81, 81))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(28)
        font.setBold(True)
        font.setWeight(75)
        self.pb5.setFont(font)
        self.MGLayout.addWidget(self.pb5, 1, 1, 1, 1)
        self.temp2.append(self.pb5)
        self.pb5.clicked.connect(self.main_prog)
        
        self.pb6 = QtWidgets.QPushButton(self.layoutWidget)
        self.pb6.setEnabled(False)
        self.pb6.setMinimumSize(QtCore.QSize(81, 81))
        self.pb6.setMaximumSize(QtCore.QSize(81, 81))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(28)
        font.setBold(True)
        font.setWeight(75)
        self.pb6.setFont(font)
        self.MGLayout.addWidget(self.pb6, 1, 2, 1, 1)
        self.temp2.append(self.pb6)
        self.pb6.clicked.connect(self.main_prog)
        
        self.pb7 = QtWidgets.QPushButton(self.layoutWidget)
        self.pb7.setEnabled(False)
        self.pb7.setMinimumSize(QtCore.QSize(81, 81))
        self.pb7.setMaximumSize(QtCore.QSize(81, 81))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(28)
        font.setBold(True)
        font.setWeight(75)
        self.pb7.setFont(font)
        self.MGLayout.addWidget(self.pb7, 2, 0, 1, 1)
        self.temp3.append(self.pb7)
        self.pb7.clicked.connect(self.main_prog)
        
        self.pb8 = QtWidgets.QPushButton(self.layoutWidget)
        self.pb8.setEnabled(False)
        self.pb8.setMinimumSize(QtCore.QSize(81, 81))
        self.pb8.setMaximumSize(QtCore.QSize(81, 81))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(28)
        font.setBold(True)
        font.setWeight(75)
        self.pb8.setFont(font)
        self.MGLayout.addWidget(self.pb8, 2, 1, 1, 1)
        self.temp3.append(self.pb8)
        self.pb8.clicked.connect(self.main_prog)
        
        self.pb9 = QtWidgets.QPushButton(self.layoutWidget)
        self.pb9.setEnabled(False)
        self.pb9.setMinimumSize(QtCore.QSize(81, 81))
        self.pb9.setMaximumSize(QtCore.QSize(81, 81))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(28)
        font.setBold(True)
        font.setWeight(75)
        self.pb9.setFont(font)
        self.MGLayout.addWidget(self.pb9, 2, 2, 1, 1)    
        self.temp3.append(self.pb9)
        self.pb9.clicked.connect(self.main_prog)
        
        self.P2Header = QtWidgets.QLabel(self.page_2)
        self.P2Header.setGeometry(QtCore.QRect(40, 20, 271, 51))
        font = QtGui.QFont()
        font.setFamily("ROBO")
        font.setPointSize(20)
        self.P2Header.setFont(font)
        self.P2Header.setStyleSheet("background-color: rgb(0, 0, 0);\n"
"color:white;\n"
"border-radius:10px;")
        self.P2Header.setAlignment(QtCore.Qt.AlignCenter)
        
        
        self.back = QtWidgets.QPushButton(self.page_2)
        self.back.setGeometry(QtCore.QRect(224, 430, 101, 41))
        font = QtGui.QFont()
        font.setFamily("ROBO")
        font.setPointSize(15)
        self.back.setFont(font)
        self.back.setStyleSheet("QPushButton{\n"
"border:3px solid rgb(255, 114, 42);\n"
"color:cyan;\n"
"background-color: dark grey;\n"
"border-radius: 10px;\n"
"}\n"
"QPushButton:hover{\n"
"border: 3px solid cyan ;\n"
"color:rgb(255, 114, 42);\n"
"}\n"
"QPushButton:pressed{\n"
"border:4px solid cyan;\n"
"}")    
        self.back.clicked.connect(self.BACK)
        
        
        self.label = QtWidgets.QLabel(self.page_2)
        self.label.setGeometry(QtCore.QRect(30, 370, 291, 41))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(22)
        self.label.setFont(font)
        self.label.setStyleSheet("background-color: rgb(0, 0, 0);\n"
"color:white;\n"
"border-radius:10px;")
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        
        
        
        self.temp.append(self.temp1)
        self.temp.append(self.temp2)
        self.temp.append(self.temp3)        
        for i in self.temp:
            for j in i:
                self.opt.append(j)
        
        
        self.stackedWidget.addWidget(self.page_2)

        self.stackedWidget.setCurrentIndex(0)
        Form.setWindowTitle("Tic-Tac-Toe")
        self.PushB1.setText("SINGLE-PLAYER")
        self.PushB2.setText("MULTIPLAYER")
        self.P1Header.setText("TIC TAC TOE")
        self.reset.setText("RESET")
        self.P2Header.setText("Single-Player")
        self.back.setText("BACK")

if __name__ == "__main__":
    import sys
    TTT_app = QtWidgets.QApplication(sys.argv)
    T_Form = QtWidgets.QWidget()
    TTT_ui = TTT_Form()
    TTT_ui.setupUi(T_Form,TTT_app)
    T_Form.show()
    sys.exit(TTT_app.exec_())
