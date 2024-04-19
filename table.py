from PyQt5.QtWidgets import QFileDialog
import pyqtgraph


class Table:
    def save(self):
        options = QFileDialog.Options()
        fileName, _ = QFileDialog.getSaveFileName(
            self, "Save File", "", "SVG Files (*.svg)", options=options)
        if fileName:
            exporter = pyqtgraph.exporters.SVGExporter(self.graphicsView.plotItem)
            exporter.export(fileName+'.svg')