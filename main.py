import os
import sys
import pandas as pd
import Ui_interface
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import *
import numpy as np


class MainApplication(QtWidgets.QMainWindow, Ui_interface.Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.directory = os.getcwd()
        self.data = None
        self.pushButton.clicked.connect(lambda:self.draw())
        self.pushButton_3.clicked.connect(lambda:self.clear())

    def draw(self):
        x = np.random.normal(size=1000)
        y = np.random.normal(size=(3,1000))
        for i in range(3):
            self.graphicsView.plot(x,y[i],pen=(i,3))
    

    def clear(self):
        self.graphicsView.clear()


def main():
  app = QtWidgets.QApplication(sys.argv)
  window = MainApplication()
  window.show()
  app.exec_()


if __name__ == '__main__':
  main()
