# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'uiOrthoViewer.ui'
##
## Created by: Qt User Interface Compiler version 6.6.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (
    QCoreApplication,
    QDate,
    QDateTime,
    QLocale,
    QMetaObject,
    QObject,
    QPoint,
    QRect,
    QSize,
    QTime,
    QUrl,
    Qt,
)
from PySide6.QtGui import (
    QAction,
    QBrush,
    QColor,
    QConicalGradient,
    QCursor,
    QFont,
    QFontDatabase,
    QGradient,
    QIcon,
    QImage,
    QKeySequence,
    QLinearGradient,
    QPainter,
    QPalette,
    QPixmap,
    QRadialGradient,
    QTransform,
)
from PySide6.QtWidgets import (
    QApplication,
    QFrame,
    QGridLayout,
    QHBoxLayout,
    QMainWindow,
    QMenu,
    QMenuBar,
    QPushButton,
    QSizePolicy,
    QSplitter,
    QStatusBar,
    QToolBox,
    QWidget,
)

from vtkmodules.qt.QVTKRenderWindowInteractor import QVTKRenderWindowInteractor


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName("MainWindow")
        MainWindow.resize(838, 731)
        self.actionOpen = QAction(MainWindow)
        self.actionOpen.setObjectName("actionOpen")
        self.actionExit = QAction(MainWindow)
        self.actionExit.setObjectName("actionExit")
        self.actionMaximize = QAction(MainWindow)
        self.actionMaximize.setObjectName("actionMaximize")
        self.actionFullScreen = QAction(MainWindow)
        self.actionFullScreen.setObjectName("actionFullScreen")
        self.actionFullScreen.setCheckable(True)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.splitter = QSplitter(self.centralwidget)
        self.splitter.setObjectName("splitter")
        self.splitter.setOrientation(Qt.Horizontal)
        self.toolBox = QToolBox(self.splitter)
        self.toolBox.setObjectName("toolBox")
        self.toolBox.setMaximumSize(QSize(200, 16777215))
        self.toolBox.setBaseSize(QSize(150, 0))
        self.page = QWidget()
        self.page.setObjectName("page")
        self.page.setGeometry(QRect(0, 0, 98, 28))
        self.toolBox.addItem(self.page, "General")
        self.pageSegmentationList = QWidget()
        self.pageSegmentationList.setObjectName("pageSegmentationList")
        self.pageSegmentationList.setGeometry(QRect(0, 0, 200, 561))
        self.toolBox.addItem(self.pageSegmentationList, "Segmentation")
        self.pagePointLists = QWidget()
        self.pagePointLists.setObjectName("pagePointLists")
        self.pagePointLists.setGeometry(QRect(0, 0, 200, 561))
        self.gridLayout_3 = QGridLayout(self.pagePointLists)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.toolBox.addItem(self.pagePointLists, "Landmarks")
        self.pageMeshes = QWidget()
        self.pageMeshes.setObjectName("pageMeshes")
        self.toolBox.addItem(self.pageMeshes, "Meshes")
        self.splitter.addWidget(self.toolBox)
        self.frame = QFrame(self.splitter)
        self.frame.setObjectName("frame")
        self.frame.setFrameShape(QFrame.Box)
        self.frame.setFrameShadow(QFrame.Raised)
        self.gridLayout_2 = QGridLayout(self.frame)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.buttonMaximize_ul = QPushButton(self.frame)
        self.buttonMaximize_ul.setObjectName("buttonMaximize_ul")
        self.buttonMaximize_ul.setFlat(False)

        self.horizontalLayout.addWidget(self.buttonMaximize_ul)

        self.gridLayout_2.addLayout(self.horizontalLayout, 0, 0, 1, 1)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.buttonMaximize_ur = QPushButton(self.frame)
        self.buttonMaximize_ur.setObjectName("buttonMaximize_ur")

        self.horizontalLayout_2.addWidget(self.buttonMaximize_ur)

        self.gridLayout_2.addLayout(self.horizontalLayout_2, 0, 1, 1, 1)

        self.qvtkWidget_ul = QVTKRenderWindowInteractor(self.frame)
        self.qvtkWidget_ul.setObjectName("qvtkWidget_ul")

        self.gridLayout_2.addWidget(self.qvtkWidget_ul, 1, 0, 1, 1)

        self.qvtkWidget_ur = QVTKRenderWindowInteractor(self.frame)
        self.qvtkWidget_ur.setObjectName("qvtkWidget_ur")

        self.gridLayout_2.addWidget(self.qvtkWidget_ur, 1, 1, 1, 1)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.buttonMaximize_ll = QPushButton(self.frame)
        self.buttonMaximize_ll.setObjectName("buttonMaximize_ll")

        self.horizontalLayout_3.addWidget(self.buttonMaximize_ll)

        self.gridLayout_2.addLayout(self.horizontalLayout_3, 2, 0, 1, 1)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.buttonMaximize_lr = QPushButton(self.frame)
        self.buttonMaximize_lr.setObjectName("buttonMaximize_lr")

        self.horizontalLayout_4.addWidget(self.buttonMaximize_lr)

        self.gridLayout_2.addLayout(self.horizontalLayout_4, 2, 1, 1, 1)

        self.qvtkWidget_ll = QVTKRenderWindowInteractor(self.frame)
        self.qvtkWidget_ll.setObjectName("qvtkWidget_ll")

        self.gridLayout_2.addWidget(self.qvtkWidget_ll, 3, 0, 1, 1)

        self.qvtkWidget_lr = QVTKRenderWindowInteractor(self.frame)
        self.qvtkWidget_lr.setObjectName("qvtkWidget_lr")

        self.gridLayout_2.addWidget(self.qvtkWidget_lr, 3, 1, 1, 1)

        self.splitter.addWidget(self.frame)

        self.gridLayout.addWidget(self.splitter, 0, 0, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName("menubar")
        self.menubar.setGeometry(QRect(0, 0, 838, 21))
        self.menuFile = QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        self.menuHelp = QMenu(self.menubar)
        self.menuHelp.setObjectName("menuHelp")
        self.menuView = QMenu(self.menubar)
        self.menuView.setObjectName("menuView")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuView.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())
        self.menuFile.addAction(self.actionOpen)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionExit)
        self.menuView.addAction(self.actionFullScreen)

        self.retranslateUi(MainWindow)

        self.toolBox.setCurrentIndex(1)

        QMetaObject.connectSlotsByName(MainWindow)

    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(
            QCoreApplication.translate("MainWindow", "OrthoViewer", None)
        )
        self.actionOpen.setText(
            QCoreApplication.translate("MainWindow", "Open...", None)
        )
        self.actionExit.setText(QCoreApplication.translate("MainWindow", "Exit", None))
        self.actionMaximize.setText(
            QCoreApplication.translate("MainWindow", "Maximize Upper Left", None)
        )
        self.actionFullScreen.setText(
            QCoreApplication.translate("MainWindow", "Full Screen", None)
        )
        self.toolBox.setItemText(
            self.toolBox.indexOf(self.page),
            QCoreApplication.translate("MainWindow", "General", None),
        )
        self.toolBox.setItemText(
            self.toolBox.indexOf(self.pageSegmentationList),
            QCoreApplication.translate("MainWindow", "Segmentation", None),
        )
        self.toolBox.setItemText(
            self.toolBox.indexOf(self.pagePointLists),
            QCoreApplication.translate("MainWindow", "Landmarks", None),
        )
        self.toolBox.setItemText(
            self.toolBox.indexOf(self.pageMeshes),
            QCoreApplication.translate("MainWindow", "Meshes", None),
        )
        self.buttonMaximize_ul.setText(
            QCoreApplication.translate("MainWindow", "+", None)
        )
        self.buttonMaximize_ur.setText(
            QCoreApplication.translate("MainWindow", "+", None)
        )
        self.buttonMaximize_ll.setText(
            QCoreApplication.translate("MainWindow", "+", None)
        )
        self.buttonMaximize_lr.setText(
            QCoreApplication.translate("MainWindow", "+", None)
        )
        self.menuFile.setTitle(QCoreApplication.translate("MainWindow", "File", None))
        self.menuHelp.setTitle(QCoreApplication.translate("MainWindow", "Help", None))
        self.menuView.setTitle(QCoreApplication.translate("MainWindow", "View", None))

    # retranslateUi
