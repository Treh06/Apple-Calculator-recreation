# Form implementation generated from reading ui file 'gui.ui'
#
# Created by: PyQt6 UI code generator 6.4.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_Calculator(object):
    def setupUi(self, Calculator):
        Calculator.setObjectName("Calculator")
        Calculator.resize(800, 800)
        Calculator.setMinimumSize(QtCore.QSize(800, 800))
        Calculator.setMaximumSize(QtCore.QSize(800, 800))
        Calculator.setAutoFillBackground(False)
        Calculator.setStyleSheet("background-color: black;")
        self.centralwidget = QtWidgets.QWidget(parent=Calculator)
        self.centralwidget.setObjectName("centralwidget")
        self.num_display = QtWidgets.QLabel(parent=self.centralwidget)
        self.num_display.setGeometry(QtCore.QRect(370, 150, 421, 51))
        self.num_display.setStyleSheet("background-color: black;\n"
"color: white;\n"
"font-size: 30px;")
        self.num_display.setText("")
        self.num_display.setScaledContents(True)
        self.num_display.setAlignment(QtCore.Qt.AlignmentFlag.AlignRight|QtCore.Qt.AlignmentFlag.AlignTrailing|QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.num_display.setWordWrap(True)
        self.num_display.setObjectName("num_display")
        self.equal_button = QtWidgets.QPushButton(parent=self.centralwidget)
        self.equal_button.setGeometry(QtCore.QRect(690, 650, 100, 100))
        font = QtGui.QFont()
        font.setPointSize(-1)
        font.setBold(True)
        self.equal_button.setFont(font)
        self.equal_button.setStyleSheet("background-color: orange;\n"
"color: white;\n"
"font-size: 40px;\n"
"font-weight: bold;\n"
"border-radius: 50px;\n"
"border: none;\n"
"padding: 10px;\n"
"min-width: 80px;\n"
"min-height: 80px;")
        self.equal_button.setObjectName("equal_button")
        self.add_button = QtWidgets.QPushButton(parent=self.centralwidget)
        self.add_button.setGeometry(QtCore.QRect(690, 540, 100, 100))
        font = QtGui.QFont()
        font.setPointSize(-1)
        font.setBold(True)
        self.add_button.setFont(font)
        self.add_button.setStyleSheet("background-color: orange;\n"
"color: white;\n"
"font-size: 40px;\n"
"font-weight: bold;\n"
"border-radius: 50px;\n"
"border: none;\n"
"padding: 10px;\n"
"min-width: 80px;\n"
"min-height: 80px;")
        self.add_button.setObjectName("add_button")
        self.subtraction_button = QtWidgets.QPushButton(parent=self.centralwidget)
        self.subtraction_button.setGeometry(QtCore.QRect(690, 430, 100, 100))
        font = QtGui.QFont()
        font.setPointSize(-1)
        font.setBold(True)
        self.subtraction_button.setFont(font)
        self.subtraction_button.setStyleSheet("background-color: orange;\n"
"color: white;\n"
"font-size: 40px;\n"
"font-weight: bold;\n"
"border-radius: 50px;\n"
"border: none;\n"
"padding: 10px;\n"
"min-width: 80px;\n"
"min-height: 80px;")
        self.subtraction_button.setObjectName("subtraction_button")
        self.multiplication_button = QtWidgets.QPushButton(parent=self.centralwidget)
        self.multiplication_button.setGeometry(QtCore.QRect(690, 320, 100, 100))
        font = QtGui.QFont()
        font.setPointSize(-1)
        font.setBold(True)
        self.multiplication_button.setFont(font)
        self.multiplication_button.setStyleSheet("background-color: orange;\n"
"color: white;\n"
"font-size: 40px;\n"
"font-weight: bold;\n"
"border-radius: 50px;\n"
"border: none;\n"
"padding: 10px;\n"
"min-width: 80px;\n"
"min-height: 80px;")
        self.multiplication_button.setObjectName("multiplication_button")
        self.divsion_button = QtWidgets.QPushButton(parent=self.centralwidget)
        self.divsion_button.setGeometry(QtCore.QRect(690, 210, 100, 100))
        font = QtGui.QFont()
        font.setPointSize(-1)
        font.setBold(True)
        self.divsion_button.setFont(font)
        self.divsion_button.setStyleSheet("background-color: orange;\n"
"color: white;\n"
"font-size: 40px;\n"
"font-weight: bold;\n"
"border-radius: 50px;\n"
"border: none;\n"
"padding: 10px;\n"
"min-width: 80px;\n"
"min-height: 80px;")
        self.divsion_button.setObjectName("divsion_button")
        self.dot_button = QtWidgets.QPushButton(parent=self.centralwidget)
        self.dot_button.setGeometry(QtCore.QRect(580, 650, 100, 100))
        font = QtGui.QFont()
        font.setPointSize(-1)
        font.setBold(True)
        self.dot_button.setFont(font)
        self.dot_button.setStyleSheet("background-color: #505050;\n"
"color: white;\n"
"font-size: 40px;\n"
"font-weight: bold;\n"
"border-radius: 50px;\n"
"border: none;\n"
"padding: 10px;\n"
"min-width: 80px;\n"
"min-height: 80px;")
        self.dot_button.setObjectName("dot_button")
        self.zero_button = QtWidgets.QPushButton(parent=self.centralwidget)
        self.zero_button.setGeometry(QtCore.QRect(470, 650, 100, 100))
        font = QtGui.QFont()
        font.setPointSize(-1)
        font.setBold(True)
        self.zero_button.setFont(font)
        self.zero_button.setStyleSheet("background-color: #505050;\n"
"color: white;\n"
"font-size: 40px;\n"
"font-weight: bold;\n"
"border-radius: 50px;\n"
"border: none;\n"
"padding: 10px;\n"
"min-width: 80px;\n"
"min-height: 80px;")
        self.zero_button.setObjectName("zero_button")
        self.coming_soon_button = QtWidgets.QPushButton(parent=self.centralwidget)
        self.coming_soon_button.setGeometry(QtCore.QRect(360, 650, 100, 100))
        font = QtGui.QFont()
        font.setPointSize(-1)
        font.setBold(True)
        self.coming_soon_button.setFont(font)
        self.coming_soon_button.setStyleSheet("background-color: #505050;\n"
"color: white;\n"
"font-size: 10px;\n"
"font-weight: bold;\n"
"border-radius: 50px;\n"
"border: none;\n"
"padding: 10px;\n"
"min-width: 80px;\n"
"min-height: 80px;")
        self.coming_soon_button.setObjectName("coming_soon_button")
        self.three_button = QtWidgets.QPushButton(parent=self.centralwidget)
        self.three_button.setGeometry(QtCore.QRect(580, 540, 100, 100))
        font = QtGui.QFont()
        font.setPointSize(-1)
        font.setBold(True)
        self.three_button.setFont(font)
        self.three_button.setStyleSheet("background-color: #505050;\n"
"color: white;\n"
"font-size: 40px;\n"
"font-weight: bold;\n"
"border-radius: 50px;\n"
"border: none;\n"
"padding: 10px;\n"
"min-width: 80px;\n"
"min-height: 80px;")
        self.three_button.setObjectName("three_button")
        self.two_button = QtWidgets.QPushButton(parent=self.centralwidget)
        self.two_button.setGeometry(QtCore.QRect(470, 540, 100, 100))
        font = QtGui.QFont()
        font.setPointSize(-1)
        font.setBold(True)
        self.two_button.setFont(font)
        self.two_button.setStyleSheet("background-color: #505050;\n"
"color: white;\n"
"font-size: 40px;\n"
"font-weight: bold;\n"
"border-radius: 50px;\n"
"border: none;\n"
"padding: 10px;\n"
"min-width: 80px;\n"
"min-height: 80px;")
        self.two_button.setObjectName("two_button")
        self.one_button = QtWidgets.QPushButton(parent=self.centralwidget)
        self.one_button.setGeometry(QtCore.QRect(360, 540, 100, 100))
        font = QtGui.QFont()
        font.setPointSize(-1)
        font.setBold(True)
        self.one_button.setFont(font)
        self.one_button.setStyleSheet("background-color: #505050;\n"
"color: white;\n"
"font-size: 40px;\n"
"font-weight: bold;\n"
"border-radius: 50px;\n"
"border: none;\n"
"padding: 10px;\n"
"min-width: 80px;\n"
"min-height: 80px;")
        self.one_button.setObjectName("one_button")
        self.six_button = QtWidgets.QPushButton(parent=self.centralwidget)
        self.six_button.setGeometry(QtCore.QRect(580, 430, 100, 100))
        font = QtGui.QFont()
        font.setPointSize(-1)
        font.setBold(True)
        self.six_button.setFont(font)
        self.six_button.setStyleSheet("background-color: #505050;\n"
"color: white;\n"
"font-size: 40px;\n"
"font-weight: bold;\n"
"border-radius: 50px;\n"
"border: none;\n"
"padding: 10px;\n"
"min-width: 80px;\n"
"min-height: 80px;")
        self.six_button.setObjectName("six_button")
        self.five_button = QtWidgets.QPushButton(parent=self.centralwidget)
        self.five_button.setGeometry(QtCore.QRect(470, 430, 100, 100))
        font = QtGui.QFont()
        font.setPointSize(-1)
        font.setBold(True)
        self.five_button.setFont(font)
        self.five_button.setStyleSheet("background-color: #505050;\n"
"color: white;\n"
"font-size: 40px;\n"
"font-weight: bold;\n"
"border-radius: 50px;\n"
"border: none;\n"
"padding: 10px;\n"
"min-width: 80px;\n"
"min-height: 80px;")
        self.five_button.setObjectName("five_button")
        self.four_button = QtWidgets.QPushButton(parent=self.centralwidget)
        self.four_button.setGeometry(QtCore.QRect(360, 430, 100, 100))
        font = QtGui.QFont()
        font.setPointSize(-1)
        font.setBold(True)
        self.four_button.setFont(font)
        self.four_button.setStyleSheet("background-color: #505050;\n"
"color: white;\n"
"font-size: 40px;\n"
"font-weight: bold;\n"
"border-radius: 50px;\n"
"border: none;\n"
"padding: 10px;\n"
"min-width: 80px;\n"
"min-height: 80px;")
        self.four_button.setObjectName("four_button")
        self.nine_button = QtWidgets.QPushButton(parent=self.centralwidget)
        self.nine_button.setGeometry(QtCore.QRect(580, 320, 100, 100))
        font = QtGui.QFont()
        font.setPointSize(-1)
        font.setBold(True)
        self.nine_button.setFont(font)
        self.nine_button.setStyleSheet("background-color: #505050;\n"
"color: white;\n"
"font-size: 40px;\n"
"font-weight: bold;\n"
"border-radius: 50px;\n"
"border: none;\n"
"padding: 10px;\n"
"min-width: 80px;\n"
"min-height: 80px;")
        self.nine_button.setObjectName("nine_button")
        self.eight_button = QtWidgets.QPushButton(parent=self.centralwidget)
        self.eight_button.setGeometry(QtCore.QRect(470, 320, 100, 100))
        font = QtGui.QFont()
        font.setPointSize(-1)
        font.setBold(True)
        self.eight_button.setFont(font)
        self.eight_button.setStyleSheet("background-color: #505050;\n"
"color: white;\n"
"font-size: 40px;\n"
"font-weight: bold;\n"
"border-radius: 50px;\n"
"border: none;\n"
"padding: 10px;\n"
"min-width: 80px;\n"
"min-height: 80px;")
        self.eight_button.setObjectName("eight_button")
        self.seven_button = QtWidgets.QPushButton(parent=self.centralwidget)
        self.seven_button.setGeometry(QtCore.QRect(360, 320, 100, 100))
        font = QtGui.QFont()
        font.setPointSize(-1)
        font.setBold(True)
        self.seven_button.setFont(font)
        self.seven_button.setStyleSheet("background-color: #505050;\n"
"color: white;\n"
"font-size: 40px;\n"
"font-weight: bold;\n"
"border-radius: 50px;\n"
"border: none;\n"
"padding: 10px;\n"
"min-width: 80px;\n"
"min-height: 80px;")
        self.seven_button.setObjectName("seven_button")
        self.ac_button = QtWidgets.QPushButton(parent=self.centralwidget)
        self.ac_button.setGeometry(QtCore.QRect(360, 210, 100, 100))
        font = QtGui.QFont()
        font.setPointSize(-1)
        font.setBold(True)
        self.ac_button.setFont(font)
        self.ac_button.setStyleSheet("background-color: #D4D4D2;\n"
"color: white;\n"
"font-size: 40px;\n"
"font-weight: bold;\n"
"border-radius: 50px;\n"
"border: none;\n"
"padding: 10px;\n"
"min-width: 80px;\n"
"min-height: 80px;")
        self.ac_button.setObjectName("ac_button")
        self.negative_postive_button = QtWidgets.QPushButton(parent=self.centralwidget)
        self.negative_postive_button.setGeometry(QtCore.QRect(470, 210, 100, 100))
        font = QtGui.QFont()
        font.setPointSize(-1)
        font.setBold(True)
        self.negative_postive_button.setFont(font)
        self.negative_postive_button.setStyleSheet("background-color: #D4D4D2;\n"
"color: white;\n"
"font-size: 40px;\n"
"font-weight: bold;\n"
"border-radius: 50px;\n"
"border: none;\n"
"padding: 10px;\n"
"min-width: 80px;\n"
"min-height: 80px;")
        self.negative_postive_button.setObjectName("negative_postive_button")
        self.percentage_button = QtWidgets.QPushButton(parent=self.centralwidget)
        self.percentage_button.setGeometry(QtCore.QRect(580, 210, 100, 100))
        font = QtGui.QFont()
        font.setPointSize(-1)
        font.setBold(True)
        self.percentage_button.setFont(font)
        self.percentage_button.setStyleSheet("background-color: #D4D4D2;\n"
"color: white;\n"
"font-size: 40px;\n"
"font-weight: bold;\n"
"border-radius: 50px;\n"
"border: none;\n"
"padding: 10px;\n"
"min-width: 80px;\n"
"min-height: 80px;")
        self.percentage_button.setObjectName("percentage_button")
        self.prev_num_display = QtWidgets.QLabel(parent=self.centralwidget)
        self.prev_num_display.setGeometry(QtCore.QRect(370, 90, 421, 51))
        self.prev_num_display.setStyleSheet("background-color: black;\n"
"color: white;")
        self.prev_num_display.setText("")
        self.prev_num_display.setObjectName("prev_num_display")
        Calculator.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(parent=Calculator)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 22))
        self.menubar.setObjectName("menubar")
        Calculator.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(parent=Calculator)
        self.statusbar.setObjectName("statusbar")
        Calculator.setStatusBar(self.statusbar)

        self.retranslateUi(Calculator)
        QtCore.QMetaObject.connectSlotsByName(Calculator)

    def retranslateUi(self, Calculator):
        _translate = QtCore.QCoreApplication.translate
        Calculator.setWindowTitle(_translate("Calculator", "MainWindow"))
        self.equal_button.setText(_translate("Calculator", "="))
        self.add_button.setText(_translate("Calculator", "+"))
        self.subtraction_button.setText(_translate("Calculator", "-"))
        self.multiplication_button.setText(_translate("Calculator", "x"))
        self.divsion_button.setText(_translate("Calculator", "/"))
        self.dot_button.setText(_translate("Calculator", "."))
        self.zero_button.setText(_translate("Calculator", "0"))
        self.coming_soon_button.setText(_translate("Calculator", "Coming soon"))
        self.three_button.setText(_translate("Calculator", "3"))
        self.two_button.setText(_translate("Calculator", "2"))
        self.one_button.setText(_translate("Calculator", "1"))
        self.six_button.setText(_translate("Calculator", "6"))
        self.five_button.setText(_translate("Calculator", "5"))
        self.four_button.setText(_translate("Calculator", "4"))
        self.nine_button.setText(_translate("Calculator", "9"))
        self.eight_button.setText(_translate("Calculator", "8"))
        self.seven_button.setText(_translate("Calculator", "7"))
        self.ac_button.setText(_translate("Calculator", "AC"))
        self.negative_postive_button.setText(_translate("Calculator", "+/-"))
        self.percentage_button.setText(_translate("Calculator", "%"))
