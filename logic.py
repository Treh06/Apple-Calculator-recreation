from PyQt6.QtWidgets import *
from gui import *


class Logic(QMainWindow,Ui_Calculator):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

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
        pass
    def add_button_clicked(self):
        pass
    def subtract_button_clicked(self):
        pass
    def multiplication_button_clicked(self):
        pass
    def divsion_button_clicked(self):
        pass
    def dot_button_clicked(self):
        pass
    def coming_soon_button_clicked(self):
        pass
    def one_button_clicked(self):
        pass
    def two_button_clicked(self):
        pass
    def three_button_clicked(self):
        pass
    def four_button_clicked(self):
        pass
    def five_button_clicked(self):
        pass
    def six_button_clicked(self):
        pass
    def seven_button_clicked(self):
        pass
    def eight_button_clicked(self):
        pass
    def nine_button_clicked(self):
        pass
    def percentage_button_clicked(self):
        pass
    def negative_postive_button_clicked(self):
        pass
    def ac_button_clicked(self):
        pass

    
        