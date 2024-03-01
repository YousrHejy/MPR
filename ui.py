# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'uiViewer.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(838, 731)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.splitter = QtWidgets.QSplitter(self.centralwidget)
        self.splitter.setOrientation(QtCore.Qt.Horizontal)
        self.splitter.setObjectName("splitter")
        self.toolBox = QtWidgets.QToolBox(self.splitter)
        self.toolBox.setMaximumSize(QtCore.QSize(200, 16777215))
        self.toolBox.setBaseSize(QtCore.QSize(150, 0))
        self.toolBox.setObjectName("toolBox")
        self.page = QtWidgets.QWidget()
        self.page.setGeometry(QtCore.QRect(0, 0, 200, 534))
        self.page.setObjectName("page")
        self.verticalLayoutWidget_3 = QtWidgets.QWidget(self.page)
        self.verticalLayoutWidget_3.setGeometry(QtCore.QRect(0, 0, 191, 121))
        self.verticalLayoutWidget_3.setObjectName("verticalLayoutWidget_3")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_3)
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.l3 = QtWidgets.QLabel(self.verticalLayoutWidget_3)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.l3.setFont(font)
        self.l3.setAlignment(QtCore.Qt.AlignCenter)
        self.l3.setObjectName("l3")
        self.verticalLayout_5.addWidget(self.l3)
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.slider = QtWidgets.QSlider(self.verticalLayoutWidget_3)
        self.slider.setOrientation(QtCore.Qt.Horizontal)
        self.slider.setObjectName("slider")
        self.horizontalLayout_7.addWidget(self.slider)
        self.verticalLayout_5.addLayout(self.horizontalLayout_7)
        self.verticalLayoutWidget_4 = QtWidgets.QWidget(self.page)
        self.verticalLayoutWidget_4.setGeometry(QtCore.QRect(0, 130, 191, 121))
        self.verticalLayoutWidget_4.setObjectName("verticalLayoutWidget_4")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_4)
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.l3_2 = QtWidgets.QLabel(self.verticalLayoutWidget_4)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.l3_2.setFont(font)
        self.l3_2.setAlignment(QtCore.Qt.AlignCenter)
        self.l3_2.setObjectName("l3_2")
        self.verticalLayout_6.addWidget(self.l3_2)
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.slider_2 = QtWidgets.QSlider(self.verticalLayoutWidget_4)
        self.slider_2.setOrientation(QtCore.Qt.Horizontal)
        self.slider_2.setObjectName("slider_2")
        self.horizontalLayout_8.addWidget(self.slider_2)
        self.verticalLayout_6.addLayout(self.horizontalLayout_8)
        self.verticalLayoutWidget_9 = QtWidgets.QWidget(self.page)
        self.verticalLayoutWidget_9.setGeometry(QtCore.QRect(0, 270, 191, 121))
        self.verticalLayoutWidget_9.setObjectName("verticalLayoutWidget_9")
        self.verticalLayout_13 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_9)
        self.verticalLayout_13.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_13.setObjectName("verticalLayout_13")
        self.l3_3 = QtWidgets.QLabel(self.verticalLayoutWidget_9)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.l3_3.setFont(font)
        self.l3_3.setAlignment(QtCore.Qt.AlignCenter)
        self.l3_3.setObjectName("l3_3")
        self.verticalLayout_13.addWidget(self.l3_3)
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.btn_play = QtWidgets.QPushButton(self.verticalLayoutWidget_9)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.btn_play.setFont(font)
        self.btn_play.setObjectName("btn_play")
        self.horizontalLayout_9.addWidget(self.btn_play)
        self.btn_pause = QtWidgets.QPushButton(self.verticalLayoutWidget_9)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.btn_pause.setFont(font)
        self.btn_pause.setObjectName("btn_pause")
        self.horizontalLayout_9.addWidget(self.btn_pause)
        self.btn_stop = QtWidgets.QPushButton(self.verticalLayoutWidget_9)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.btn_stop.setFont(font)
        self.btn_stop.setObjectName("btn_stop")
        self.horizontalLayout_9.addWidget(self.btn_stop)
        self.verticalLayout_13.addLayout(self.horizontalLayout_9)
        self.toolBox.addItem(self.page, "")
        self.pageSegmentationList = QtWidgets.QWidget()
        self.pageSegmentationList.setGeometry(QtCore.QRect(0, 0, 200, 534))
        self.pageSegmentationList.setObjectName("pageSegmentationList")
        self.toolBox.addItem(self.pageSegmentationList, "")
        self.pagePointLists = QtWidgets.QWidget()
        self.pagePointLists.setGeometry(QtCore.QRect(0, 0, 200, 534))
        self.pagePointLists.setObjectName("pagePointLists")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.pagePointLists)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.toolBox.addItem(self.pagePointLists, "")
        self.pageMeshes = QtWidgets.QWidget()
        self.pageMeshes.setGeometry(QtCore.QRect(0, 0, 200, 534))
        self.pageMeshes.setObjectName("pageMeshes")
        self.toolBox.addItem(self.pageMeshes, "")
        self.frame = QtWidgets.QFrame(self.splitter)
        self.frame.setFrameShape(QtWidgets.QFrame.Box)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.frame)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.widget_v2 = QtWidgets.QWidget(self.frame)
        self.widget_v2.setObjectName("widget_v2")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.widget_v2)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.widget_v3 = QtWidgets.QWidget(self.widget_v2)
        self.widget_v3.setObjectName("widget_v3")
        self.verticalLayout_9 = QtWidgets.QVBoxLayout(self.widget_v3)
        self.verticalLayout_9.setObjectName("verticalLayout_9")
        self.verticalLayout_10 = QtWidgets.QVBoxLayout()
        self.verticalLayout_10.setObjectName("verticalLayout_10")
        self.buttonMaximize_ul_5 = QtWidgets.QPushButton(self.widget_v3)
        self.buttonMaximize_ul_5.setFlat(False)
        self.buttonMaximize_ul_5.setObjectName("buttonMaximize_ul_5")
        self.verticalLayout_10.addWidget(self.buttonMaximize_ul_5)
        self.verticalLayout_9.addLayout(self.verticalLayout_10)
        self.btn_zoom_v3 = QtWidgets.QToolButton(self.widget_v3)
        self.btn_zoom_v3.setObjectName("btn_zoom_v3")
        self.verticalLayout_9.addWidget(self.btn_zoom_v3)
        self.horizontalLayout_3.addWidget(self.widget_v3)
        self.widget_v2_2 = QtWidgets.QWidget(self.widget_v2)
        self.widget_v2_2.setObjectName("widget_v2_2")
        self.verticalLayout_12 = QtWidgets.QVBoxLayout(self.widget_v2_2)
        self.verticalLayout_12.setObjectName("verticalLayout_12")
        self.verticalLayout_11 = QtWidgets.QVBoxLayout()
        self.verticalLayout_11.setObjectName("verticalLayout_11")
        self.buttonMaximize_ul_4 = QtWidgets.QPushButton(self.widget_v2_2)
        self.buttonMaximize_ul_4.setFlat(False)
        self.buttonMaximize_ul_4.setObjectName("buttonMaximize_ul_4")
        self.verticalLayout_11.addWidget(self.buttonMaximize_ul_4)
        self.verticalLayout_12.addLayout(self.verticalLayout_11)
        self.btn_zoom_v2 = QtWidgets.QToolButton(self.widget_v2_2)
        self.btn_zoom_v2.setObjectName("btn_zoom_v2")
        self.verticalLayout_12.addWidget(self.btn_zoom_v2)
        self.horizontalLayout_3.addWidget(self.widget_v2_2)
        self.horizontalLayout_2.addWidget(self.widget_v2)
        self.gridLayout_2.addLayout(self.horizontalLayout_2, 1, 0, 1, 1)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.widget_v1 = QtWidgets.QWidget(self.frame)
        self.widget_v1.setObjectName("widget_v1")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.widget_v1)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout()
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.buttonMaximize_ul_2 = QtWidgets.QPushButton(self.widget_v1)
        self.buttonMaximize_ul_2.setFlat(False)
        self.buttonMaximize_ul_2.setObjectName("buttonMaximize_ul_2")
        self.verticalLayout_7.addWidget(self.buttonMaximize_ul_2)
        self.verticalLayout_2.addLayout(self.verticalLayout_7)
        self.btn_zoom_v1 = QtWidgets.QToolButton(self.widget_v1)
        self.btn_zoom_v1.setObjectName("btn_zoom_v1")
        self.verticalLayout_2.addWidget(self.btn_zoom_v1)
        self.horizontalLayout.addWidget(self.widget_v1)
        self.widget_img = QtWidgets.QWidget(self.frame)
        self.widget_img.setObjectName("widget_img")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.widget_img)
        self.verticalLayout.setObjectName("verticalLayout")
        self.verticalLayout_8 = QtWidgets.QVBoxLayout()
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.buttonMaximize_ul_3 = QtWidgets.QPushButton(self.widget_img)
        self.buttonMaximize_ul_3.setFlat(False)
        self.buttonMaximize_ul_3.setObjectName("buttonMaximize_ul_3")
        self.verticalLayout_8.addWidget(self.buttonMaximize_ul_3)
        self.verticalLayout.addLayout(self.verticalLayout_8)
        self.btn_zoom_img = QtWidgets.QToolButton(self.widget_img)
        self.btn_zoom_img.setObjectName("btn_zoom_img")
        self.verticalLayout.addWidget(self.btn_zoom_img)
        self.horizontalLayout.addWidget(self.widget_img)
        self.gridLayout_2.addLayout(self.horizontalLayout, 0, 0, 1, 1)
        self.gridLayout.addWidget(self.splitter, 1, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 838, 36))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        self.menuHelp = QtWidgets.QMenu(self.menubar)
        self.menuHelp.setObjectName("menuHelp")
        self.menuView = QtWidgets.QMenu(self.menubar)
        self.menuView.setObjectName("menuView")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionOpen = QtWidgets.QAction(MainWindow)
        self.actionOpen.setObjectName("actionOpen")
        self.actionExit = QtWidgets.QAction(MainWindow)
        self.actionExit.setObjectName("actionExit")
        self.actionMaximize = QtWidgets.QAction(MainWindow)
        self.actionMaximize.setObjectName("actionMaximize")
        self.actionFullScreen = QtWidgets.QAction(MainWindow)
        self.actionFullScreen.setCheckable(True)
        self.actionFullScreen.setObjectName("actionFullScreen")
        self.menuFile.addAction(self.actionOpen)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionExit)
        self.menuView.addAction(self.actionFullScreen)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuView.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())

        self.retranslateUi(MainWindow)
        self.toolBox.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "OrthoViewer"))
        self.l3.setText(_translate("MainWindow", "Brightness"))
        self.l3_2.setText(_translate("MainWindow", "Contrast"))
        self.l3_3.setText(_translate("MainWindow", "CineOptions"))
        self.btn_play.setText(_translate("MainWindow", "Play"))
        self.btn_pause.setText(_translate("MainWindow", "Pause"))
        self.btn_stop.setText(_translate("MainWindow", "Stop"))
        self.toolBox.setItemText(self.toolBox.indexOf(self.page), _translate("MainWindow", "General"))
        self.toolBox.setItemText(self.toolBox.indexOf(self.pageSegmentationList), _translate("MainWindow", "Segmentation"))
        self.toolBox.setItemText(self.toolBox.indexOf(self.pagePointLists), _translate("MainWindow", "Landmarks"))
        self.toolBox.setItemText(self.toolBox.indexOf(self.pageMeshes), _translate("MainWindow", "Meshes"))
        self.buttonMaximize_ul_5.setText(_translate("MainWindow", "+"))
        self.btn_zoom_v3.setText(_translate("MainWindow", "zoom to fit"))
        self.buttonMaximize_ul_4.setText(_translate("MainWindow", "+"))
        self.btn_zoom_v2.setText(_translate("MainWindow", "zoom to fit"))
        self.buttonMaximize_ul_2.setText(_translate("MainWindow", "+"))
        self.btn_zoom_v1.setText(_translate("MainWindow", "zoom to fit"))
        self.buttonMaximize_ul_3.setText(_translate("MainWindow", "+"))
        self.btn_zoom_img.setText(_translate("MainWindow", "zoom to fit"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.menuHelp.setTitle(_translate("MainWindow", "Help"))
        self.menuView.setTitle(_translate("MainWindow", "View"))
        self.actionOpen.setText(_translate("MainWindow", "Open..."))
        self.actionExit.setText(_translate("MainWindow", "Exit"))
        self.actionMaximize.setText(_translate("MainWindow", "Maximize Upper Left"))
        self.actionFullScreen.setText(_translate("MainWindow", "Full Screen"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
