import os
import sys
import pandas as pd
from Ui_interface import Ui_MainWindow
import numpy as np
import sympy as sp
import pyqtgraph as pg
from PyQt5 import QtWidgets, QtCore, QtWidgets, QtSql
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
        self.table = None
        self.color = 'red'
        self.marker = 'o'
        self.lst_item_func = []
        self.lst_item_xlsx = []
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
        self.tableView.setColumnWidth(0, 60)
        self.tableView.setColumnWidth(1, 150)
        self.tableView.setColumnWidth(2, 70)
        self.tableView.setColumnWidth(3, 70)
        self.tableView.setColumnWidth(4, 160)
        self.tableView.setColumnWidth(5, 96)

    def add_new_transaction(self):
        function_text = self.select_funtion.text() if self.select_funtion.text() else 'xlsx'
        x_min = int(self.lineEdit_2.text())
        x_max = int(self.lineEdit.text())
        color = self.color
        line_style = self.line_style

        self.add_new_transaction_query(
            function_text, x_min, x_max, color, line_style)
        self.view_data()

    def add_new_transaction_query(self, function_text, x_min, x_max, color, line_style):
        sql_query = "INSERT INTO charts (Func, Min, Max, Color, Style) VALUES (?, ?, ?, ?, ?)"
        self.execute_query_with_params(
            sql_query, [function_text, x_min, x_max, color, line_style])

    def execute_query_with_params(self, sql_query, query_values=None):
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
        self.execute_query_with_params(sql_query, [id])

    def delete_chart(self):
        index = self.tableView.selectedIndexes()[0]
        id = str(self.tableView.model().data(index))
        self.delete_data_from_db(id)
        self.view_data()
        id = int(id) - 1
        self.graphicsView.removeItem(self.lst_item_func[id])

    def draw_chart(self):
        function_text = self.select_funtion.text()
        if function_text:
            x = np.linspace(int(self.lineEdit.text()),
                            int(self.lineEdit_2.text()), 500)
            self.symbolSize = 0.1
            try:
                func = sp.lambdify(sp.Symbol('x'), function_text)
                y = func(x)
            except:
                QMessageBox.warning(
                    self, "Ошибка", "Ошибка в вычислении функции")

            self.plot_item_func = self.graphicsView.plot(x, y, pen=pg.mkPen(
                self.color, width=2, style=self.line_style), name=function_text)

            self.lst_item_func.append(self.plot_item_func)
        else:
            x = self.table.values[:, 0]
            y = self.table.values[:, 1]
            self.symbolSize = 15
            self.plot_item_xlsx = self.graphicsView.plot(x, y, pen=pg.mkPen(
                self.color, width=2, style=self.line_style), symbol=self.marker, symbolBrush='black', symbolSize=self.symbolSize, name='xlsx')

            self.lst_item_func.append(self.plot_item_xlsx)

        try:
            print(self.lst_item_func)
            print(self.lst_item_xlsx)
            print('________________')
        except:
            pass
        self.add_new_transaction()

    def clear_all(self):
        self.graphicsView.clear()
        self.lst_item_func.clear()
        self.lst_item_xlsx.clear()

    def before_close(self):
        query = QtSql.QSqlQuery()
        query.exec("DELETE FROM charts")
        os.unlink('chart_db.db')
        print("Данные удалены.")

    def closeEvent(self, event):
        # Вызов функции перед закрытием
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
