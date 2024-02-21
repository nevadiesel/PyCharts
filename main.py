import os
import sys
import pandas as pd
import Ui_interface
import numpy as np
import sympy as sp
import pyqtgraph as pg
from PyQt5 import QtWidgets
from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QIcon



class MainApplication(QtWidgets.QMainWindow, Ui_interface.Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.directory = os.getcwd()
        self.setWindowTitle("PyCharts ")
        self.setWindowIcon(QIcon('pie-chart.ico'))
        self.table = None
        self.color = 'r'
        self.marker = 'o'
        self.line_style = QtCore.Qt.SolidLine
        self.graphicsView.setBackground('#31394D')
        self.graphicsView.showGrid(x=True, y=True, alpha = 1)
        self.graphicsView.addLegend()

        self.pushButton_6.clicked.connect(lambda: self.background_color_b())
        self.pushButton_7.clicked.connect(lambda: self.background_color_w())

        
        self.pushButton.clicked.connect(lambda: self.draw())
        self.pushButton_3.clicked.connect(lambda: self.clear())
        self.pushButton_4.clicked.connect(lambda: self.clear_all())
        self.pushButton_2.clicked.connect(lambda: self.open_xlsx())

        self.select_color_blue.clicked.connect(lambda: self.set_blue())
        self.select_color_green.clicked.connect(lambda: self.set_green())
        self.select_color_red.clicked.connect(lambda: self.set_red())
        self.select_color_purple.clicked.connect(lambda: self.set_purple())

        self.select_marker_point.clicked.connect(lambda: self.set_point())
        self.select_marker_triangle.clicked.connect(lambda: self.set_trianglle())
        self.select_marker_star.clicked.connect(lambda: self.set_star())
        self.select_marker_diamond.clicked.connect(lambda: self.set_diamond())

        self.select_marker_point_2.clicked.connect(lambda: self.set_SolidLine())
        self.select_marker_point_5.clicked.connect(lambda: self.set_DashLine())
        self.select_marker_point_3.clicked.connect(lambda: self.set_DotLine())
        self.select_marker_point_4.clicked.connect(lambda: self.set_DashDotLine())

    def background_color_b(self):
        self.graphicsView.setBackground('#31394D')

    def background_color_w(self):
        self.graphicsView.setBackground('w')


    def set_blue(self):
        self.color = 'b'
    def set_purple(self):
        self.color = 'purple'
    def set_green(self):
        self.color = 'g'
    def set_red(self):
        self.color = 'red'

    def set_point(self):
        self.marker = 'o'
    def  set_trianglle(self):
        self.marker = 't'
    def set_star(self):
        self.marker = 'star'
    def set_diamond(self):
        self.marker = 'd'

    def set_SolidLine(self):
        self.line_style = QtCore.Qt.SolidLine
    def set_DashLine(self):
        self.line_style = QtCore.Qt.DashLine
    def set_DotLine(self):
        self.line_style = QtCore.Qt.DotLine
    def set_DashDotLine(self):
        self.line_style = QtCore.Qt.DashDotLine


    def open_xlsx(self):
        options = QFileDialog.Options()
        fileName, _ = QFileDialog.getOpenFileName(
            self, "Open File", "", "Excel file (*.xlsx)", options=options)
        if fileName:
            self.table = pd.read_excel(fileName)

    def draw(self):
        if self.select_funtion.text():
            x = np.linspace(int(self.lineEdit.text()), int(self.lineEdit_2.text()), 500)
            self.symbolSize = 0.1
            try:
                # func = lambda x: eval(self.select_funtion.text())
                func = sp.lambdify(sp.Symbol('x'), self.select_funtion.text())
                y = func(x)
            except:
                pass
            self.plot_item_func = self.graphicsView.plot(x, y, pen = pg.mkPen(self.color, width=2, style=self.line_style), name='test')
        else:
            x = self.table.values[:, 0]
            y = self.table.values[:, 1]
            self.symbolSize = 15
            self.plot_item_xlsx = self.graphicsView.plot(x, y, pen = pg.mkPen(
                self.color, width=2, style=self.line_style), symbol=self.marker, symbolBrush='black', symbolSize=self.symbolSize, name='xlsx')
        print(self.plot_item_func)
        print(self.plot_item_xlsx)

    def clear(self):
        self.graphicsView.clear()
    
    def clear_all(self):
        self.graphicsView.removeItem(self.plot_item_xlsx)


def main():
    app = QtWidgets.QApplication(sys.argv)
    window = MainApplication()
    window.show()
    app.exec_()


if __name__ == '__main__':
    main()
