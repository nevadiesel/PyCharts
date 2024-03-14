import os
import sys
import pandas as pd
from Ui_interface import Ui_MainWindow
import numpy as np
import sympy as sp
import pyqtgraph as pg
import pyqtgraph.exporters
from PyQt5 import QtWidgets, QtCore, QtWidgets, QtSql, QtGui
from PyQt5.QtWidgets import QFileDialog, QMessageBox
from PyQt5.QtGui import QIcon
from PyQt5.QtSql import QSqlTableModel  


class MainApplication(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.ui = Ui_MainWindow()
        self.directory = os.getcwd()
        self.setWindowTitle("PyCharts ")
        self.setWindowIcon(QIcon('pie-chart.ico'))
        # self.setWindowIcon(QIcon('ico.ico'))
        self.table = None
        self.color = 'blue'
        self.marker = 'o'
        self.lst_item = []
        self.line_style = QtCore.Qt.SolidLine
        self.graphicsView.setBackground('#31394D')
        self.graphicsView.showGrid(x=True, y=True, alpha=1)
        self.graphicsView.addLegend()
        self.create_db()
        self.view_data()
        self.setup_signals()

    def setup_signals(self):
        self.pushButton_6.clicked.connect(
            lambda: self.set_background_color('#31394D'))
        self.pushButton_7.clicked.connect(
            lambda: self.set_background_color('w'))
        self.pushButton.clicked.connect(self.draw_chart)
        self.pushButton_3.clicked.connect(self.delete_chart)
        self.pushButton_4.clicked.connect(self.clear_all)
        self.pushButton_2.clicked.connect(self.open_xlsx)
        self.open_close_side_bar_btn.clicked.connect(self.slideMenu)

        # Установка цвета
        self.select_color_blue.clicked.connect(lambda: self.set_color('blue'))
        self.select_color_green.clicked.connect(
            lambda: self.set_color('green'))
        self.select_color_red.clicked.connect(lambda: self.set_color('red'))
        self.select_color_purple.clicked.connect(
            lambda: self.set_color('purple'))

        # Установка маркера
        self.select_marker_point.clicked.connect(lambda: self.set_marker('o'))
        self.select_marker_triangle.clicked.connect(
            lambda: self.set_marker('t'))
        self.select_marker_star.clicked.connect(
            lambda: self.set_marker('star'))
        self.select_marker_diamond.clicked.connect(
            lambda: self.set_marker('d'))

        # Установка стиля линии
        self.select_marker_point_2.clicked.connect(
            lambda: self.set_line_style(QtCore.Qt.SolidLine))
        self.select_marker_point_5.clicked.connect(
            lambda: self.set_line_style(QtCore.Qt.DashLine))
        self.select_marker_point_3.clicked.connect(
            lambda: self.set_line_style(QtCore.Qt.DotLine))
        self.select_marker_point_4.clicked.connect(
            lambda: self.set_line_style(QtCore.Qt.DashDotLine))

    def slideMenu(self):
        width = self.right_menu_widget.width()

        if width == 0:
            newWidth = 250
        else:
            newWidth = 0

        self.animation = QtCore.QPropertyAnimation(
            self.right_menu_widget, b"maximumWidth")
        self.animation.setDuration(250)
        self.animation.setStartValue(width)
        self.animation.setEndValue(newWidth)
        self.animation.setEasingCurve(QtCore.QEasingCurve.InOutQuart)
        self.animation.start()

        hight = self.tableView.height()

        if hight == 0:
            newhight = 192
        else:
            newhight = 0

        self.animation1 = QtCore.QPropertyAnimation(
            self.tableView, b"maximumHeight")
        self.animation1.setDuration(250)
        self.animation1.setStartValue(hight)
        self.animation1.setEndValue(newhight)
        self.animation1.setEasingCurve(QtCore.QEasingCurve.InOutQuart)
        self.animation1.start()

    def set_background_color(self, color):
        self.graphicsView.setBackground(color)

    def set_color(self, color):
        self.color = color

    def set_marker(self, marker):
        self.marker = marker

    def set_line_style(self, style):
        self.line_style = style

    def open_xlsx(self):
        options = QFileDialog.Options()
        fileName, _ = QFileDialog.getOpenFileName(
            self, "Open File", "", "Excel file (*.xlsx)", options=options)
        if fileName:
            self.table = pd.read_excel(fileName)

    def view_data(self):
        self.model = QSqlTableModel()
        self.model.setTable('charts')
        self.model.select()
        self.tableView.setModel(self.model)
        self.tableView.setColumnWidth(0, 80)
        self.tableView.setColumnWidth(1, 200)
        self.tableView.setColumnWidth(2, 120)
        self.tableView.setColumnWidth(3, 120)
        self.tableView.setColumnWidth(4, 140)
        self.tableView.setColumnWidth(5, 90)
        # self.tableView.setTextAlignment(QtCore.Qt.AlignCenter)
        # item = QTableVievItem(Func) # create the item
        # item.setTextAlignment(Qt.AlignHCenter)

    def add_new_chart(self):
        function_text = self.select_function.text(
        ) if self.select_function.text() else 'xlsx'
        x_min = int(self.lineEdit_2.text())
        x_max = int(self.lineEdit.text())
        color = self.color
        line_style = self.line_style

        self.new_chart_query(
            function_text, x_min, x_max, color, line_style)
        self.view_data()

    def new_chart_query(self, function_text, x_min, x_max, color, line_style):
        sql_query = "INSERT INTO charts (Func, Min, Max, Color, Style) VALUES (?, ?, ?, ?, ?)"
        self.delete_query_id(
            sql_query, [function_text, x_min, x_max, color, line_style])

    def delete_query_id(self, sql_query, query_values=None):
        query = QtSql.QSqlQuery()
        query.prepare(sql_query)

        if query_values is not None:
            for query_value in query_values:
                query.addBindValue(query_value)

        query.exec()

        return query

    def create_db(self):
        db = QtSql.QSqlDatabase.addDatabase('QSQLITE')
        db.setDatabaseName('chart_db.db')

        if not db.open():
            QtWidgets.QMessageBox.critical(None, "Cannot open database",
                                           "Click Cancel to exit.", QtWidgets.QMessageBox.Cancel)
            return False

        query = QtSql.QSqlQuery()
        query.exec("CREATE TABLE IF NOT EXISTS charts (ID integer primary key AUTOINCREMENT, Func TEXT, Min INTEGER, "
                   "Max INTEGER, Color TEXT, Style TEXT)")
        return True

    def delete_data_from_db(self, id):
        sql_query = "DELETE FROM charts WHERE ID=?"
        self.delete_query_id(sql_query, [id])

    def delete_chart(self):
        index = self.tableView.selectedIndexes()[0]
        id = str(self.tableView.model().data(index))
        self.delete_data_from_db(id)
        self.view_data()
        id = int(id) - 1
        self.graphicsView.removeItem(self.lst_item[id])

    def draw_fuctinon(self):
        function_text = self.select_function.text()
        x_min = int(self.lineEdit_2.text())
        x_max = int(self.lineEdit.text())
        x = np.linspace(x_min, x_max, int((x_max - x_min) / 0.01) + 1)
        self.symbolSize = 0.1
        try:
            func = sp.lambdify(sp.Symbol('x'), function_text)
            with np.errstate(divide='ignore', invalid='ignore'):
                y = func(x)
            # func = sp.lambdify(sp.Symbol('x'), function_text)
            # def f(x):
            #     with np.errstate(divide='ignore', invalid='ignore'):
            #         return func(x)
            # y = f(x)
        except:
            QMessageBox.warning(self, "Ошибка", "Ошибка в вычислении функции")

        self.plot_item_func = self.graphicsView.plot(x, y, pen=pg.mkPen(
            self.color, width=2, style=self.line_style), name=function_text)

        self.lst_item.append(self.plot_item_func)

    def draw_xlsx(self):
        x = self.table.values[:, 0]
        y = self.table.values[:, 1]
        self.symbolSize = 15
        self.plot_item_xlsx = self.graphicsView.plot(x, y, pen=pg.mkPen(
            self.color, width=2, style=self.line_style), symbol=self.marker, symbolBrush='black', symbolSize=self.symbolSize, name='xlsx')

        self.lst_item.append(self.plot_item_xlsx)

    def draw_chart(self):
        if self.select_function.text():
            self.draw_fuctinon()
            self.save()
        else:
            self.draw_xlsx()
        self.add_new_chart()

    def clear_all(self):
        self.graphicsView.clear()
        self.lst_item.clear()
        query = QtSql.QSqlQuery()
        query.exec("DELETE FROM charts")
        self.view_data()

    def before_close(self):
        query = QtSql.QSqlQuery()
        query.exec("DELETE FROM charts")
        os.unlink('chart_db.db')
        print("Данные удалены.")

    def save(self):
        options = QFileDialog.Options()
        fileName, _ = QFileDialog.getSaveFileName(self, "Save File", "", "SVG Files (*.svg)", options=options)
        if fileName:
            exporter = pg.exporters.SVGExporter(self.graphicsView.plotItem)
            exporter.export(fileName+'.svg')

    def closeEvent(self, event):
        self.before_close()
        event.accept()  # Если вы хотите, чтобы окно закрывалось без дополнительных запросов
        # или используйте event.ignore(), если есть условия, при которых закрытие не должно происходить


def main():
    app = QtWidgets.QApplication(sys.argv)
    window = MainApplication()
    window.show()
    app.exec_()


if __name__ == '__main__':
    main()
