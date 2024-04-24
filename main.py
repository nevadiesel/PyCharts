# Возможности программы на данный момент:
#     1. Построение графиков:
#         Изменение цвета, стиля линии графика
#             1) По точкам
#                 Загрузка данных из таблицы, изменение формы точек
#             2) Заданной функции на промежутке
#             3) Функции вида y = число
#     2. Вывод в таблицу основных параметров графика(x_min, x_max, color, line style)
#     2. Сохранение графиков
#         svg - формат
#     3. Свернуть/развернуть меню

# Планируемые обновления:
#     Оптимизация кода, ускорение работы программы, повышение стабильности работы
#     Интрефейс:
#         1. Подгонка размеров фреймов
#         2. Доработка цветовой палитры
#         3. Увеличение размера, изменение шрифта
#         4. Добавление большей закругленности элементов интерфейса
#         5. Добавление кастомного TitleBar,
#             кнопок свернуть, развернуть, закрыть программу
#         6. Фикс некоректного перебора элементов инерфейса при использовании Tab
#     Функции:
#         1. Возможность строить несколько графиков из одного файла таблицы
#             Выбирать в каких столбцах x, y. (по умолчанию x - первый,y - второй)
#         2. Устранение артефакта при постройки графика вида 1/x, x->0 (tan(x), 1/sin(x))
#         3. Фикс некоректной работы программы
#             после использования функции clear_all(кнопки: Стереть все)

# Возможные обновления:
#     1. Построение графиков в полярной системе координат
#     2. Добавление возможности автоматического построения производной графика функции
#     3. Вывод в таблицу дополнительной информации по графику функции:
#         пересечение с осями координат, точек разрыва...
#     4. Возможность задавать свой цвет графика в формате rgb

import os
import sys
import re
from Ui_interface import Ui_MainWindow
from table import Table
import numpy as np
import sympy as sp
import pyqtgraph as pg
import pyqtgraph.exporters
from PyQt5 import QtWidgets, QtCore, QtWidgets, QtSql
from PyQt5.QtWidgets import QFileDialog, QMessageBox
from PyQt5.QtGui import QIcon
from PyQt5.QtSql import QSqlTableModel

from plot import Function, HorizontalLine, XlsxPlot


class MainApplication(QtWidgets.QMainWindow, Ui_MainWindow, Table, Function, HorizontalLine, XlsxPlot):
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
        self.graphicsView.showGrid(x=True, y=True, alpha=0.2)
        self.graphicsView.addLegend()
        self.create_db()
        self.view_data()
        self.setup_signals()

    def setup_signals(self):
        self.pushButton_6.clicked.connect(
            lambda: self.set_background_color('#31394D'))
        self.pushButton_7.clicked.connect(
            lambda: self.set_background_color('w'))
        self.pushButton.clicked.connect(self.draw)
        self.pushButton_3.clicked.connect(self.delete_chart)
        self.pushButton_4.clicked.connect(self.clear_all)
        self.pushButton_2.clicked.connect(self.open_xlsx)
        self.saveButton.clicked.connect(self.save)
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

    def set_background_color(self, color: str):
        self.graphicsView.setBackground(color)

    def set_color(self, color: str):
        self.color = color

    def set_marker(self, marker: str):
        self.marker = marker

    def set_line_style(self, style):
        self.line_style = style

    def view_data(self):
        self.model = QSqlTableModel()
        self.model.setTable('charts')
        self.model.select()
        self.tableView.setModel(self.model)
        self.tableView.setColumnWidth(0, 100)
        self.tableView.setColumnWidth(1, 200)
        self.tableView.setColumnWidth(2, 120)
        self.tableView.setColumnWidth(3, 120)
        self.tableView.setColumnWidth(4, 140)
        self.tableView.setColumnWidth(5, 90)
        # self.tableView.setTextAlignment(QtCore.Qt.AlignCenter)
        # item = QTableVievItem(Func) # create the item
        # item.setTextAlignment(Qt.AlignHCenter)

    def draw_fuctinon(self, function: str, x_min: int, x_max: int):
        x = np.linspace(x_min, x_max, int((x_max - x_min) / 0.01) + 1)
        self.symbolSize = 0.1
        try:
            func = sp.lambdify(sp.Symbol('x'), function)
            with np.errstate(divide='ignore', invalid='ignore'):
                y = func(x)
        except:
            QMessageBox.warning(self, "Ошибка", "Ошибка в вычислении функции")
            return

        plot_item_func = self.graphicsView.plot(x, y, pen=pg.mkPen(
            self.color, width=2, style=self.line_style), name=function)

        self.lst_item.append(plot_item_func)
        self.add_new_chart(function, x_min, x_max, self.color, self.line_style)

    def draw_xlsx(self):
        x = self.table.values[:, 0]
        y = self.table.values[:, 1]
        x_min = int(min(x))
        x_max = int(max(x))
        self.symbolSize = 10
        plot_item_xlsx = self.graphicsView.plot(x, y, pen=pg.mkPen(
            self.color, width=2, style=self.line_style), symbol=self.marker,
            symbolBrush='black', symbolSize=self.symbolSize, name='xlsx')

        self.lst_item.append(plot_item_xlsx)
        self.add_new_chart('Xlsx', x_min, x_max, self.color, self.line_style)

    def draw(self):
        if self.select_function.text():
            if re.compile(r'\d*').fullmatch(self.select_function.text()):
                line = HorizontalLine(
                    self.select_function.text(), 0, 0, self.color, self.line_style)
                self.graphicsView.addItem(line.draw(), ignoreBounds=True)
            else:
                self.draw_fuctinon(function=self.select_function.text(), 
                                   x_min=int(self.lineEdit_2.text()), 
                                   x_max=int(self.lineEdit.text()))
        else:
            self.draw_xlsx()

    def clear_all(self):
        self.graphicsView.clear()
        self.lst_item.clear()
        query = QtSql.QSqlQuery()
        query.exec("DELETE FROM charts")
        self.view_data()

    def save(self):
        options = QFileDialog.Options()
        fileName, _ = QFileDialog.getSaveFileName(
            self, "Save File", "", "SVG Files (*.svg)", options=options)
        if fileName:
            exporter = pyqtgraph.exporters.SVGExporter(
                self.graphicsView.plotItem)
            exporter.export(fileName+'.svg')

    def before_close(self):
        query = QtSql.QSqlQuery()
        query.exec("DELETE FROM charts")
        os.unlink('chart_db.db')
        print("Данные удалены.")

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
