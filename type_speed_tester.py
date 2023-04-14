from PyQt5 import QtCore, QtGui, QtWidgets
import random
import time

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        self.s=0
        self.e=0
        self.incorret_word=""
        self.correct_word=""
        self.texts=open("random sentences.txt","r").read().split("\n")
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(502, 510)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(120, 0, 251, 71))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        
        self.plainTextEdit = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.plainTextEdit.setGeometry(QtCore.QRect(30, 200, 441, 81))
        self.plainTextEdit.setPlainText("")
        self.plainTextEdit.setObjectName("plainTextEdit")
        
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(30, 100, 441, 61))
        font_1 = QtGui.QFont()
        font_1.setPointSize(12)
        self.label_2.setFont(font_1)
        self.label_2.setText("Welcome! to the type speed tester build using python.")
        self.label_2.setObjectName("label_2")

        
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(190, 330, 75, 23))
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.reset)

        
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(30, 290, 47, 13))
        self.label_5.setObjectName("label_5")
        
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(70, 290, 300, 13))
        self.label_6.setText("")
        self.label_6.setObjectName("label_6")
        
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(30, 330, 75, 23))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_2.clicked.connect(self.start)

        
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(110, 330, 75, 23))
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_3.clicked.connect(self.submit)

        
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(30, 400, 141, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(180, 400, 200, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 502, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "Typing Speed Test"))
        self.pushButton.setText(_translate("MainWindow", "Reset"))
        self.label_5.setText(_translate("MainWindow", "Status:"))
        self.pushButton_2.setText(_translate("MainWindow", "Start"))
        self.pushButton_3.setText(_translate("MainWindow", "Submit"))
        self.label_3.setText(_translate("MainWindow", "Words Per minute:"))
        self.label_4.setText(_translate("MainWindow", "0.0"))

    def reset(self):
        self.plainTextEdit.clear()
        self.label_6.setText("")
        self.label_4.setText("0.0")
        self.load_sentence()
        
    def load_sentence(self):
        text=random.choice(self.texts)
        self.label_2.setText(text)

    def start(self):
        w_text=self.plainTextEdit.toPlainText()
        if w_text=="":
            self.s=time.time()
        else:
            self.label_6.setText("First press start button before start writing.(click reset)")
            self.label_6.setStyleSheet("color:red")
            
        
    def check(self,sentence):
        g_text=self.label_2.text()
        g_text=g_text.split()
        w_text=sentence.split()
        for i in range(len(w_text)):
            if w_text[i]!=g_text[i]:
                self.incorret_word=w_text[i]
                self.correct_word=g_text[i]
                return 0
        return 1
    
    def length(self,sentence):
        g_text=self.label_2.text()
        g_text=g_text.split()
        return len(g_text)
    
    def submit(self):
        if self.s!=0:
            w_text=self.plainTextEdit.toPlainText()
            if self.check(w_text):
                self.e=time.time()
                d=self.e-self.s
                n=self.length(w_text)
                speed=(n/d)*60
                self.label_6.setText("correct! (click reset for next round)")
                self.label_6.setStyleSheet("color:green")
                self.label_4.setText(str(speed))
                self.s=0
            else:
                self.label_6.setText("Incorrect! | "+self.incorret_word+" instead of "+self.correct_word+" | (click reset)")
                self.label_6.setStyleSheet("color:red")
                self.s=0
        else:
            self.label_6.setText("First press start button before start writing.(click reset)")
            self.label_6.setStyleSheet("color:red")
        

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
