# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/home/ivan/Documents/GitHub/PyCharts/interface4.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from pyqtgraph import PlotWidget
import resources_rc


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(886, 617)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setStyleSheet("@font-face {\n"
"    font-family: NovaFlat;\n"
"    src: url(:/fonts/Nova_Flat/NovaFlat-Regular.ttf) format(\"truetype\");\n"
"}\n"
"*{\n"
"color: #fff;\n"
"font-family: NovaFlat;\n"
"font-size: 12px;\n"
"border: nine;\n"
"background: none;\n"
"}\n"
"#centralwidget{\n"
"background-color: rgb(33, 43, 51);\n"
"}\n"
"#right_menu_widget, #percentage_bar_chart, #nested_donuts,\n"
"#line_charts, #bar_charts, #temperature_bar_chart\n"
"{\n"
"background-color: rgba(61, 80, 95, 100)\n"
"}\n"
"#header_frame, #frame_3, #frame_5{\n"
"background-color: rgb(61, 80, 95);\n"
"}\n"
"#frame_4 QPushButton{\n"
"padding: 10px;\n"
"border-radius: 5px;\n"
"background-color: rgba(33, 43, 51, 100);\n"
"}\n"
"#header_nav QPushButton{\n"
"    background-color: rgb(61, 80, 95);\n"
"    border-radius: 15px;\n"
"    border: 3px solid rgb(120, 157, 186);\n"
"}\n"
"#header_nav QPushButton:hover{\n"
"    background-color: rgb(120, 157, 186);\n"
"}\n"
"")
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.frame_2 = QtWidgets.QFrame(self.centralwidget)
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.frame_2)
        self.verticalLayout_4.setContentsMargins(6, 0, 0, 0)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.header_frame = QtWidgets.QFrame(self.frame_2)
        self.header_frame.setMinimumSize(QtCore.QSize(0, 46))
        self.header_frame.setMaximumSize(QtCore.QSize(16777215, 50))
        self.header_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.header_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.header_frame.setObjectName("header_frame")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.header_frame)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.frame_11 = QtWidgets.QFrame(self.header_frame)
        self.frame_11.setStyleSheet("")
        self.frame_11.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_11.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_11.setObjectName("frame_11")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.frame_11)
        self.horizontalLayout_5.setContentsMargins(3, 3, 3, 3)
        self.horizontalLayout_5.setSpacing(3)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.pushButton_6 = QtWidgets.QPushButton(self.frame_11)
        self.pushButton_6.setMinimumSize(QtCore.QSize(50, 30))
        self.pushButton_6.setMaximumSize(QtCore.QSize(50, 30))
        self.pushButton_6.setStyleSheet("QPushButton{\n"
"    color: rgba(49, 57, 77);\n"
"     background-color:rgba(49, 57, 77);\n"
"     border: 1px solid rgba(255,255,255,40);\n"
"     border-radius:10px;\n"
"width: 15;\n"
"height: 15;\n"
"}\n"
"QPushButton:hover{\n"
"background-color:rgba(49, 57, 77);\n"
"}\n"
"QPushButton:pressed{\n"
"background-color:rgba(255,255,255,70);\n"
"}")
        self.pushButton_6.setText("")
        self.pushButton_6.setObjectName("pushButton_6")
        self.horizontalLayout_5.addWidget(self.pushButton_6)
        self.pushButton_7 = QtWidgets.QPushButton(self.frame_11)
        self.pushButton_7.setMinimumSize(QtCore.QSize(50, 30))
        self.pushButton_7.setMaximumSize(QtCore.QSize(50, 30))
        self.pushButton_7.setStyleSheet("QPushButton{\n"
"    color: rgb(255, 255, 255);\n"
"     background-color:rgba(255,255,255,200);\n"
"     border: 1px solid rgba(255,255,255,40);\n"
"     border-radius:10px;\n"
"width: 15;\n"
"height: 15;\n"
"}\n"
"QPushButton:hover{\n"
"background-color:rgba(255,255,255,200);\n"
"}\n"
"QPushButton:pressed{\n"
"background-color:rgba(255,255,255,70);\n"
"}")
        self.pushButton_7.setText("")
        self.pushButton_7.setObjectName("pushButton_7")
        self.horizontalLayout_5.addWidget(self.pushButton_7)
        self.label_7 = QtWidgets.QLabel(self.frame_11)
        font = QtGui.QFont()
        font.setFamily("NovaFlat")
        font.setPointSize(-1)
        self.label_7.setFont(font)
        self.label_7.setAlignment(QtCore.Qt.AlignCenter)
        self.label_7.setObjectName("label_7")
        self.horizontalLayout_5.addWidget(self.label_7)
        self.horizontalLayout_3.addWidget(self.frame_11)
        self.frame_10 = QtWidgets.QFrame(self.header_frame)
        self.frame_10.setMaximumSize(QtCore.QSize(100, 16777215))
        self.frame_10.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_10.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_10.setObjectName("frame_10")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.frame_10)
        self.horizontalLayout_4.setContentsMargins(8, 0, 8, 0)
        self.horizontalLayout_4.setSpacing(2)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label_6 = QtWidgets.QLabel(self.frame_10)
        self.label_6.setObjectName("label_6")
        self.horizontalLayout_4.addWidget(self.label_6)
        self.open_close_side_bar_btn = QtWidgets.QPushButton(self.frame_10)
        self.open_close_side_bar_btn.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/icons/icons/align-center.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.open_close_side_bar_btn.setIcon(icon)
        self.open_close_side_bar_btn.setIconSize(QtCore.QSize(30, 30))
        self.open_close_side_bar_btn.setObjectName("open_close_side_bar_btn")
        self.horizontalLayout_4.addWidget(self.open_close_side_bar_btn)
        self.horizontalLayout_3.addWidget(self.frame_10)
        self.verticalLayout_4.addWidget(self.header_frame, 0, QtCore.Qt.AlignTop)
        self.frame_8 = QtWidgets.QFrame(self.frame_2)
        self.frame_8.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_8.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_8.setObjectName("frame_8")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout(self.frame_8)
        self.verticalLayout_7.setContentsMargins(3, 3, 3, 3)
        self.verticalLayout_7.setSpacing(3)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.graphicsView = PlotWidget(self.frame_8)
        self.graphicsView.setObjectName("graphicsView")
        self.verticalLayout_7.addWidget(self.graphicsView)
        self.verticalLayout_4.addWidget(self.frame_8)
        self.footer_frame = QtWidgets.QFrame(self.frame_2)
        self.footer_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.footer_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.footer_frame.setObjectName("footer_frame")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout(self.footer_frame)
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_6.setSpacing(0)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.frame_13 = QtWidgets.QFrame(self.footer_frame)
        self.frame_13.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_13.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_13.setObjectName("frame_13")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.frame_13)
        self.verticalLayout_6.setContentsMargins(3, 3, 3, 9)
        self.verticalLayout_6.setSpacing(3)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.tableView = QtWidgets.QTableView(self.frame_13)
        self.tableView.setStyleSheet("QTableView {\n"
"background-color: rgba(255, 255, 255, 30); \n"
"border: 1px solid rgba(255,255,255,40);\n"
"border-bottom-right-radius: 7px; \n"
"border-bottom-left-radius: 7px; \n"
"color: white;\n"
"}\n"
"\n"
"QHeaderView::section {\n"
"background-color: rgb(53, 53, 53);\n"
"color: white;\n"
"border: none;\n"
"height: 50px;\n"
"font-size: 16pt;\n"
"}\n"
"\n"
"QTableView::item {\n"
"    border-style: none;\n"
"    border-bottom: 1px solid rgba(255,255,255,50);\n"
"    padding-left: auto;\n"
"    padding-right: auto;\n"
"}\n"
"\n"
"QTableView::item:selected{\n"
"    border: none;\n"
"    color: rgb(255, 255, 255);\n"
"    background-color: rgba(255, 255, 255, 50);\n"
"}\n"
"")
        self.tableView.setObjectName("tableView")
        self.verticalLayout_6.addWidget(self.tableView)
        self.horizontalLayout_6.addWidget(self.frame_13)
        self.verticalLayout_4.addWidget(self.footer_frame, 0, QtCore.Qt.AlignBottom)
        self.horizontalLayout.addWidget(self.frame_2)
        self.right_menu_widget = QtWidgets.QWidget(self.centralwidget)
        self.right_menu_widget.setMinimumSize(QtCore.QSize(240, 0))
        self.right_menu_widget.setMaximumSize(QtCore.QSize(240, 1000000))
        self.right_menu_widget.setObjectName("right_menu_widget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.right_menu_widget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.frame_3 = QtWidgets.QFrame(self.right_menu_widget)
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.frame_3)
        self.horizontalLayout_2.setContentsMargins(7, 4, 0, 4)
        self.horizontalLayout_2.setSpacing(6)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_14 = QtWidgets.QLabel(self.frame_3)
        self.label_14.setMinimumSize(QtCore.QSize(40, 40))
        self.label_14.setMaximumSize(QtCore.QSize(40, 40))
        self.label_14.setText("")
        self.label_14.setPixmap(QtGui.QPixmap(":/icons/icons/pie-chart.svg"))
        self.label_14.setScaledContents(True)
        self.label_14.setObjectName("label_14")
        self.horizontalLayout_2.addWidget(self.label_14)
        self.label = QtWidgets.QLabel(self.frame_3)
        font = QtGui.QFont()
        font.setFamily("NovaFlat")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(99)
        self.label.setFont(font)
        self.label.setMouseTracking(False)
        self.label.setStyleSheet("*{font-size:12pt; font-weight: 1000;}")
        self.label.setWordWrap(False)
        self.label.setObjectName("label")
        self.horizontalLayout_2.addWidget(self.label)
        self.verticalLayout.addWidget(self.frame_3)
        self.frame_4 = QtWidgets.QFrame(self.right_menu_widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_4.sizePolicy().hasHeightForWidth())
        self.frame_4.setSizePolicy(sizePolicy)
        self.frame_4.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_4.setObjectName("frame_4")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.frame_4)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.frame = QtWidgets.QFrame(self.frame_4)
        self.frame.setMaximumSize(QtCore.QSize(1000, 1000))
        self.frame.setStyleSheet("QPushButton:pressed{\n"
"background-color:rgba(255,255,255,70);\n"
"}")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.frame)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.pushButton_2 = QtWidgets.QPushButton(self.frame)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/icons/icons/upload.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_2.setIcon(icon1)
        self.pushButton_2.setObjectName("pushButton_2")
        self.verticalLayout_3.addWidget(self.pushButton_2)
        self.verticalLayout_2.addWidget(self.frame, 0, QtCore.Qt.AlignTop)
        self.pushButton_5 = QtWidgets.QPushButton(self.frame_4)
        self.pushButton_5.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/images/images/girl.jpg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_5.setIcon(icon2)
        self.pushButton_5.setIconSize(QtCore.QSize(200, 200))
        self.pushButton_5.setObjectName("pushButton_5")
        self.verticalLayout_2.addWidget(self.pushButton_5)
        self.groupBox = QtWidgets.QGroupBox(self.frame_4)
        self.groupBox.setMinimumSize(QtCore.QSize(0, 0))
        self.groupBox.setMaximumSize(QtCore.QSize(1000, 1000))
        self.groupBox.setStyleSheet("QPushButton{\n"
"    color: rgb(255, 255, 255);\n"
"     background-color:rgba(255,255,255,30);\n"
"     border: 1px solid rgba(255,255,255,40);\n"
"     border-radius:10px;\n"
"width: 15;\n"
"height: 15;\n"
"}\n"
"QPushButton:hover{\n"
"background-color:rgba(255,255,255,30);\n"
"}\n"
"QPushButton:pressed{\n"
"background-color:rgba(255,255,255,70);\n"
"}\n"
"QLineEdit{font-size:14pt; color:#aa0000;\n"
"    background-color: rgba(255, 255, 255, 80);\n"
"    border-radius:5px;\n"
"}\n"
"QLabel{font-size:10pt;\n"
"}")
        self.groupBox.setTitle("")
        self.groupBox.setObjectName("groupBox")
        self.gridLayout = QtWidgets.QGridLayout(self.groupBox)
        self.gridLayout.setContentsMargins(3, 3, 3, 9)
        self.gridLayout.setSpacing(3)
        self.gridLayout.setObjectName("gridLayout")
        self.select_marker_point_2 = QtWidgets.QPushButton(self.groupBox)
        self.select_marker_point_2.setMinimumSize(QtCore.QSize(40, 37))
        self.select_marker_point_2.setMaximumSize(QtCore.QSize(40, 37))
        self.select_marker_point_2.setIconSize(QtCore.QSize(30, 30))
        self.select_marker_point_2.setObjectName("select_marker_point_2")
        self.gridLayout.addWidget(self.select_marker_point_2, 4, 0, 1, 1)
        self.select_color_purple = QtWidgets.QPushButton(self.groupBox)
        self.select_color_purple.setMinimumSize(QtCore.QSize(40, 37))
        self.select_color_purple.setMaximumSize(QtCore.QSize(40, 37))
        self.select_color_purple.setText("")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(":/images/images/purple-circle-svgrepo-com.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.select_color_purple.setIcon(icon3)
        self.select_color_purple.setIconSize(QtCore.QSize(25, 25))
        self.select_color_purple.setObjectName("select_color_purple")
        self.gridLayout.addWidget(self.select_color_purple, 2, 3, 1, 1)
        self.select_color_red = QtWidgets.QPushButton(self.groupBox)
        self.select_color_red.setMinimumSize(QtCore.QSize(40, 37))
        self.select_color_red.setMaximumSize(QtCore.QSize(40, 37))
        self.select_color_red.setText("")
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(":/images/images/red-circle-svgrepo-com.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.select_color_red.setIcon(icon4)
        self.select_color_red.setIconSize(QtCore.QSize(25, 25))
        self.select_color_red.setObjectName("select_color_red")
        self.gridLayout.addWidget(self.select_color_red, 2, 2, 1, 1)
        self.select_color_green = QtWidgets.QPushButton(self.groupBox)
        self.select_color_green.setMinimumSize(QtCore.QSize(40, 37))
        self.select_color_green.setMaximumSize(QtCore.QSize(40, 37))
        self.select_color_green.setText("")
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap(":/images/images/green-circle-svgrepo-com.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.select_color_green.setIcon(icon5)
        self.select_color_green.setIconSize(QtCore.QSize(25, 25))
        self.select_color_green.setObjectName("select_color_green")
        self.gridLayout.addWidget(self.select_color_green, 2, 1, 1, 1)
        self.select_marker_star = QtWidgets.QPushButton(self.groupBox)
        self.select_marker_star.setMinimumSize(QtCore.QSize(40, 37))
        self.select_marker_star.setMaximumSize(QtCore.QSize(40, 37))
        self.select_marker_star.setText("")
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap(":/images/images/m14.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.select_marker_star.setIcon(icon6)
        self.select_marker_star.setIconSize(QtCore.QSize(40, 40))
        self.select_marker_star.setObjectName("select_marker_star")
        self.gridLayout.addWidget(self.select_marker_star, 3, 2, 1, 1)
        self.select_marker_triangle = QtWidgets.QPushButton(self.groupBox)
        self.select_marker_triangle.setMinimumSize(QtCore.QSize(40, 37))
        self.select_marker_triangle.setMaximumSize(QtCore.QSize(40, 37))
        self.select_marker_triangle.setText("")
        icon7 = QtGui.QIcon()
        icon7.addPixmap(QtGui.QPixmap(":/images/images/m03_1.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.select_marker_triangle.setIcon(icon7)
        self.select_marker_triangle.setIconSize(QtCore.QSize(30, 30))
        self.select_marker_triangle.setObjectName("select_marker_triangle")
        self.gridLayout.addWidget(self.select_marker_triangle, 3, 1, 1, 1)
        self.select_marker_diamond = QtWidgets.QPushButton(self.groupBox)
        self.select_marker_diamond.setMinimumSize(QtCore.QSize(40, 37))
        self.select_marker_diamond.setMaximumSize(QtCore.QSize(40, 37))
        self.select_marker_diamond.setText("")
        icon8 = QtGui.QIcon()
        icon8.addPixmap(QtGui.QPixmap(":/images/images/m19.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.select_marker_diamond.setIcon(icon8)
        self.select_marker_diamond.setIconSize(QtCore.QSize(30, 30))
        self.select_marker_diamond.setObjectName("select_marker_diamond")
        self.gridLayout.addWidget(self.select_marker_diamond, 3, 3, 1, 1)
        self.select_marker_point = QtWidgets.QPushButton(self.groupBox)
        self.select_marker_point.setMinimumSize(QtCore.QSize(40, 37))
        self.select_marker_point.setMaximumSize(QtCore.QSize(40, 37))
        self.select_marker_point.setText("")
        icon9 = QtGui.QIcon()
        icon9.addPixmap(QtGui.QPixmap(":/images/images/m00_1.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.select_marker_point.setIcon(icon9)
        self.select_marker_point.setIconSize(QtCore.QSize(30, 30))
        self.select_marker_point.setObjectName("select_marker_point")
        self.gridLayout.addWidget(self.select_marker_point, 3, 0, 1, 1)
        self.lineEdit_2 = QtWidgets.QLineEdit(self.groupBox)
        self.lineEdit_2.setMaximumSize(QtCore.QSize(40, 16777215))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.gridLayout.addWidget(self.lineEdit_2, 1, 1, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.groupBox)
        self.label_4.setMaximumSize(QtCore.QSize(42, 25))
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 0, 0, 1, 1)
        self.select_funtion = QtWidgets.QLineEdit(self.groupBox)
        self.select_funtion.setMaximumSize(QtCore.QSize(200, 16777215))
        self.select_funtion.setStyleSheet("")
        self.select_funtion.setObjectName("select_funtion")
        self.gridLayout.addWidget(self.select_funtion, 0, 1, 1, 3)
        self.label_2 = QtWidgets.QLabel(self.groupBox)
        self.label_2.setMaximumSize(QtCore.QSize(40, 16777215))
        font = QtGui.QFont()
        font.setFamily("NovaFlat")
        font.setPointSize(10)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)
        self.lineEdit = QtWidgets.QLineEdit(self.groupBox)
        self.lineEdit.setMaximumSize(QtCore.QSize(40, 16777215))
        self.lineEdit.setObjectName("lineEdit")
        self.gridLayout.addWidget(self.lineEdit, 1, 3, 1, 1)
        self.select_color_blue = QtWidgets.QPushButton(self.groupBox)
        self.select_color_blue.setMinimumSize(QtCore.QSize(40, 37))
        self.select_color_blue.setMaximumSize(QtCore.QSize(40, 37))
        self.select_color_blue.setText("")
        icon10 = QtGui.QIcon()
        icon10.addPixmap(QtGui.QPixmap(":/images/images/blue-circle-svgrepo-com.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.select_color_blue.setIcon(icon10)
        self.select_color_blue.setIconSize(QtCore.QSize(25, 25))
        self.select_color_blue.setObjectName("select_color_blue")
        self.gridLayout.addWidget(self.select_color_blue, 2, 0, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.groupBox)
        self.label_3.setMaximumSize(QtCore.QSize(40, 16777215))
        font = QtGui.QFont()
        font.setFamily("NovaFlat")
        font.setPointSize(10)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 1, 2, 1, 1)
        self.select_marker_point_3 = QtWidgets.QPushButton(self.groupBox)
        self.select_marker_point_3.setMaximumSize(QtCore.QSize(40, 40))
        self.select_marker_point_3.setIconSize(QtCore.QSize(30, 30))
        self.select_marker_point_3.setObjectName("select_marker_point_3")
        self.gridLayout.addWidget(self.select_marker_point_3, 4, 2, 1, 1)
        self.select_marker_point_4 = QtWidgets.QPushButton(self.groupBox)
        self.select_marker_point_4.setMinimumSize(QtCore.QSize(40, 37))
        self.select_marker_point_4.setMaximumSize(QtCore.QSize(40, 37))
        self.select_marker_point_4.setIconSize(QtCore.QSize(30, 30))
        self.select_marker_point_4.setObjectName("select_marker_point_4")
        self.gridLayout.addWidget(self.select_marker_point_4, 4, 3, 1, 1)
        self.select_marker_point_5 = QtWidgets.QPushButton(self.groupBox)
        self.select_marker_point_5.setMinimumSize(QtCore.QSize(40, 37))
        self.select_marker_point_5.setMaximumSize(QtCore.QSize(40, 37))
        self.select_marker_point_5.setIconSize(QtCore.QSize(30, 30))
        self.select_marker_point_5.setObjectName("select_marker_point_5")
        self.gridLayout.addWidget(self.select_marker_point_5, 4, 1, 1, 1)
        self.verticalLayout_2.addWidget(self.groupBox, 0, QtCore.Qt.AlignBottom)
        self.verticalLayout.addWidget(self.frame_4)
        self.frame_5 = QtWidgets.QFrame(self.right_menu_widget)
        self.frame_5.setMinimumSize(QtCore.QSize(0, 40))
        self.frame_5.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_5.setObjectName("frame_5")
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout(self.frame_5)
        self.horizontalLayout_7.setContentsMargins(6, 0, 0, 0)
        self.horizontalLayout_7.setSpacing(6)
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.verticalLayout.addWidget(self.frame_5)
        self.frame_6 = QtWidgets.QFrame(self.right_menu_widget)
        self.frame_6.setStyleSheet("QPushButton{\n"
"    color: rgb(255, 255, 255);\n"
"     background-color:rgba(255,255,255,30);\n"
"     border: 1px solid rgba(255,255,255,40);\n"
"     border-radius:10px;\n"
"height: 30;\n"
"}\n"
"QPushButton:hover{\n"
"background-color:rgba(255,255,255,30);\n"
"}\n"
"QPushButton:pressed{\n"
"background-color:rgba(255,255,255,70);\n"
"}\n"
"")
        self.frame_6.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_6.setObjectName("frame_6")
        self.gridLayout_6 = QtWidgets.QGridLayout(self.frame_6)
        self.gridLayout_6.setObjectName("gridLayout_6")
        self.pushButton_3 = QtWidgets.QPushButton(self.frame_6)
        self.pushButton_3.setStyleSheet("")
        self.pushButton_3.setObjectName("pushButton_3")
        self.gridLayout_6.addWidget(self.pushButton_3, 2, 0, 1, 1)
        self.pushButton_4 = QtWidgets.QPushButton(self.frame_6)
        self.pushButton_4.setStyleSheet("")
        icon11 = QtGui.QIcon()
        icon11.addPixmap(QtGui.QPixmap(":/icons/icons/alert-triangle.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_4.setIcon(icon11)
        self.pushButton_4.setObjectName("pushButton_4")
        self.gridLayout_6.addWidget(self.pushButton_4, 2, 1, 1, 1)
        self.pushButton = QtWidgets.QPushButton(self.frame_6)
        self.pushButton.setObjectName("pushButton")
        self.gridLayout_6.addWidget(self.pushButton, 1, 0, 1, 2)
        self.verticalLayout.addWidget(self.frame_6)
        self.horizontalLayout.addWidget(self.right_menu_widget)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_7.setText(_translate("MainWindow", "DASHBOARD"))
        self.label_6.setText(_translate("MainWindow", "MENU"))
        self.label.setText(_translate("MainWindow", "PY CHARTS"))
        self.pushButton_2.setText(_translate("MainWindow", "Загрузить данные"))
        self.select_marker_point_2.setText(_translate("MainWindow", "---"))
        self.label_4.setText(_translate("MainWindow", "f(x)="))
        self.label_2.setText(_translate("MainWindow", "Xmin:"))
        self.label_3.setText(_translate("MainWindow", "Xmax:"))
        self.select_marker_point_3.setText(_translate("MainWindow", ". . ."))
        self.select_marker_point_4.setText(_translate("MainWindow", "-.-.-"))
        self.select_marker_point_5.setText(_translate("MainWindow", "- - -"))
        self.pushButton_3.setText(_translate("MainWindow", "Стререть"))
        self.pushButton_4.setText(_translate("MainWindow", "Стереть все"))
        self.pushButton.setText(_translate("MainWindow", "Построить"))
