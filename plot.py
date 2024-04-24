import pyqtgraph as pg
import numpy as np
import sympy as sp
from PyQt5.QtWidgets import QMessageBox


class Plot:
    def __init__(self, function, x_min: int, x_max: int, color, line_style) -> None:
        self.function = function
        self.x_min = x_min
        self.x_max = x_max
        self.color = color
        self.line_style = line_style


class Function(Plot):
    def __init__(self, function, x_min, x_max, color, line_style) -> None:
        super().__init__(function, x_min, x_max, color, line_style)

    def draw(self):
        pass



class HorizontalLine(Plot):
    def __init__(self, function, x_min, x_max, color, line_style) -> None:
        super().__init__(function, x_min, x_max, color, line_style)

    def draw(self):
        horizontal_line = pg.InfiniteLine(pos=int(
            self.function), angle=0, movable=True, pen=pg.mkPen(
            self.color, width=2, style=self.line_style), name=int(self.function))

        return horizontal_line



class XlsxPlot(Plot):
    def __init__(self, function, x_min, x_max, color, line_style) -> None:
        super().__init__(function, x_min, x_max, color, line_style)

    def draw(self):
        pass
