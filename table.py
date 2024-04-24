from PyQt5 import QtSql, QtWidgets
from PyQt5.QtWidgets import QFileDialog
import pyqtgraph
import pandas as pd


class Table:
    def open_xlsx(self):
        options = QFileDialog.Options()
        fileName, _ = QFileDialog.getOpenFileName(
            self, "Open File", "", "Excel file (*.xlsx)", options=options)
        if fileName:
            self.table = pd.read_excel(fileName)

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

    def add_new_chart(self, function, x_min, x_max, color, line_style):
        sql_query = "INSERT INTO charts (Func, Min, Max, Color, Style) VALUES (?, ?, ?, ?, ?)"
        self.delete_query_id(
            sql_query, [function, x_min, x_max, color, line_style])
        self.view_data()

    def delete_chart(self):
        index = self.tableView.selectedIndexes()[0]
        id = str(self.tableView.model().data(index))
        self.delete_data_from_db(id)
        self.view_data()
        id = int(id) - 1
        self.graphicsView.removeItem(self.lst_item[id])

    def delete_data_from_db(self, id):
        sql_query = "DELETE FROM charts WHERE ID=?"
        self.delete_query_id(sql_query, [id])

    def delete_query_id(self, sql_query, query_values=None):
        query = QtSql.QSqlQuery()
        query.prepare(sql_query)

        if query_values is not None:
            for query_value in query_values:
                query.addBindValue(query_value)

        query.exec()

        return query