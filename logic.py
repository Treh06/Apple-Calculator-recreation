from PyQt6.QtWidgets import *
from gui import *


class Logic(QMainWindow,Ui_Calculator):
    def __init__(self):
        super().__init__()
        self.setupUi(self)


        #array for storing label contents
        self.num_display.setText("Hello")
        self.label_array = []
        #self.last_item = self.label_array[-1]

        #connect buttons to functions

        self.equal_button.clicked.connect(self.equal_button_clicked)
        self.add_button.clicked.connect(self.add_button_clicked)
        self.subtraction_button.clicked.connect(self.subtract_button_clicked)
        self.multiplication_button.clicked.connect(self.multiplication_button_clicked)
        self.divsion_button.clicked.connect(self.divsion_button_clicked)
        self.dot_button.clicked.connect(self.dot_button_clicked)
        self.coming_soon_button.clicked.connect(self.coming_soon_button_clicked)
        self.one_button.clicked.connect(self.one_button_clicked)
        self.two_button.clicked.connect(self.two_button_clicked)
        self.three_button.clicked.connect(self.three_button_clicked)
        self.four_button.clicked.connect(self.four_button_clicked)
        self.five_button.clicked.connect(self.five_button_clicked)
        self.six_button.clicked.connect(self.six_button_clicked)
        self.seven_button.clicked.connect(self.seven_button_clicked)
        self.eight_button.clicked.connect(self.eight_button_clicked)
        self.nine_button.clicked.connect(self.nine_button_clicked)
        self.percentage_button.clicked.connect(self.percentage_button_clicked)
        self.negative_postive_button.clicked.connect(self.negative_postive_button_clicked)
        self.ac_button.clicked.connect(self.ac_button_clicked)
    
    #Functions


    def equal_button_clicked(self):
        if self.equal_button.clicked.connect:
            pass

    def add_button_clicked(self):
        if self.add_button.clicked.connect:
            self.label_array.append('+')
            self.update_num_disply()


    def subtract_button_clicked(self):
        if self.subtraction_button.clicked.connect:
            self.label_array.append('-')
            self.update_num_disply()


    def multiplication_button_clicked(self):
        if self.multiplication_button.clicked.connect:
            self.label_array.append('*')
            self.update_num_disply()


    def divsion_button_clicked(self):
        if self.divsion_button.clicked.connect:
            self.label_array.append('/')
            self.update_num_disply()


    def dot_button_clicked(self):
        if self.dot_button.clicked.connect:
            self.label_array.append('.')
            self.update_num_disply()


    def coming_soon_button_clicked(self):
        if self.coming_soon_button.clicked.connect:
            pass
    def one_button_clicked(self):
        if self.one_button.clicked.connect:
            self.label_array.append('1')
            self.update_num_disply()


    def two_button_clicked(self):
        if self.two_button.clicked.connect:
            self.label_array.append('2')
            self.update_num_disply()

    def three_button_clicked(self):
        if self.three_button.clicked.connect:
            self.label_array.append('3')
            self.update_num_disply()

    def four_button_clicked(self):
        if self.four_button.clicked.connect:
            self.label_array.append('4')
            self.update_num_disply()

    def five_button_clicked(self):
        if self.five_button.clicked.connect:
            self.label_array.append('5')
            self.update_num_disply()

    def six_button_clicked(self):
        if self.six_button.clicked.connect:
            self.label_array.append('6')
            self.update_num_disply()

    def seven_button_clicked(self):
        if self.seven_button.clicked.connect:
            self.label_array.append('7')
            self.update_num_disply()

    def eight_button_clicked(self):
        if self.eight_button.clicked.connect:
            self.label_array.append('8')
            self.update_num_disply()

    def nine_button_clicked(self):
        if self.nine_button.clicked.connect:
            self.label_array.append('9')
            self.update_num_disply()

    def percentage_button_clicked(self):
        if self.percentage_button.clicked.connect:
            pass
    def negative_postive_button_clicked(self):
        if self.negative_postive_button.clicked.connect:
            pass
    def ac_button_clicked(self):
        if self.ac_button.clicked.connect:
            pass

    def update_num_disply(self):
        x = ''.join(self.label_array)
        self.num_display.setText(f"{x}")
        