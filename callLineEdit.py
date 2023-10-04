import sys

from PyQt6.QtWidgets import QDialog

from layout import *



class MyForm(QDialog):

    def __init__(self):
        super().__init__()
        self.ui = Ui_Dialog()