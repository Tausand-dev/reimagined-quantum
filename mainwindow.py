# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'GUI/mainwindow.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(600, 436)
        self.centralWidget = QtWidgets.QWidget(MainWindow)
        self.centralWidget.setObjectName("centralWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralWidget)
        self.verticalLayout.setContentsMargins(11, 11, 11, 11)
        self.verticalLayout.setSpacing(6)
        self.verticalLayout.setObjectName("verticalLayout")
        self.frame = QtWidgets.QFrame(self.centralWidget)
        self.frame.setMinimumSize(QtCore.QSize(0, 50))
        self.frame.setMaximumSize(QtCore.QSize(16777215, 50))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.frame)
        self.horizontalLayout_2.setContentsMargins(11, 11, 11, 11)
        self.horizontalLayout_2.setSpacing(6)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label = QtWidgets.QLabel(self.frame)
        self.label.setObjectName("label")
        self.horizontalLayout_2.addWidget(self.label)
        self.save_line = QtWidgets.QLineEdit(self.frame)
        self.save_line.setObjectName("save_line")
        self.horizontalLayout_2.addWidget(self.save_line)
        self.save_button = QtWidgets.QPushButton(self.frame)
        self.save_button.setObjectName("save_button")
        self.horizontalLayout_2.addWidget(self.save_button)
        self.verticalLayout.addWidget(self.frame)
        self.frame_3 = QtWidgets.QFrame(self.centralWidget)
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.frame_3)
        self.horizontalLayout_5.setContentsMargins(11, 11, 11, 11)
        self.horizontalLayout_5.setSpacing(6)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.frame_4 = QtWidgets.QFrame(self.frame_3)
        self.frame_4.setMinimumSize(QtCore.QSize(250, 0))
        self.frame_4.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_4.setObjectName("frame_4")
        self.gridLayout = QtWidgets.QGridLayout(self.frame_4)
        self.gridLayout.setContentsMargins(11, 11, 11, 11)
        self.gridLayout.setSpacing(6)
        self.gridLayout.setObjectName("gridLayout")
        self.channels_button = QtWidgets.QPushButton(self.frame_4)
        self.channels_button.setEnabled(False)
        self.channels_button.setObjectName("channels_button")
        self.gridLayout.addWidget(self.channels_button, 2, 0, 1, 1)
        self.groupBox = QtWidgets.QGroupBox(self.frame_4)
        self.groupBox.setFlat(False)
        self.groupBox.setObjectName("groupBox")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.groupBox)
        self.gridLayout_2.setContentsMargins(11, 11, 11, 11)
        self.gridLayout_2.setSpacing(6)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.label_2 = QtWidgets.QLabel(self.groupBox)
        self.label_2.setObjectName("label_2")
        self.gridLayout_2.addWidget(self.label_2, 0, 0, 1, 1)
        self.port_box = QtWidgets.QComboBox(self.groupBox)
        self.port_box.setMinimumSize(QtCore.QSize(100, 0))
        self.port_box.setObjectName("port_box")
        self.gridLayout_2.addWidget(self.port_box, 0, 1, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.groupBox)
        self.label_3.setObjectName("label_3")
        self.gridLayout_2.addWidget(self.label_3, 2, 0, 1, 1)
        self.label_5 = QtWidgets.QLabel(self.groupBox)
        self.label_5.setObjectName("label_5")
        self.gridLayout_2.addWidget(self.label_5, 3, 0, 1, 1)
        self.coin_spinBox = QtWidgets.QSpinBox(self.groupBox)
        self.coin_spinBox.setEnabled(False)
        self.coin_spinBox.setMaximumSize(QtCore.QSize(100, 16777215))
        self.coin_spinBox.setCorrectionMode(QtWidgets.QAbstractSpinBox.CorrectToNearestValue)
        self.coin_spinBox.setKeyboardTracking(False)
        self.coin_spinBox.setMinimum(5)
        self.coin_spinBox.setMaximum(1000000)
        self.coin_spinBox.setSingleStep(5)
        self.coin_spinBox.setProperty("value", 5)
        self.coin_spinBox.setObjectName("coin_spinBox")
        self.gridLayout_2.addWidget(self.coin_spinBox, 3, 1, 1, 1)
        self.samp_spinBox = QtWidgets.QSpinBox(self.groupBox)
        self.samp_spinBox.setEnabled(False)
        self.samp_spinBox.setMaximumSize(QtCore.QSize(100, 16777215))
        self.samp_spinBox.setCorrectionMode(QtWidgets.QAbstractSpinBox.CorrectToNearestValue)
        self.samp_spinBox.setKeyboardTracking(False)
        self.samp_spinBox.setMinimum(1)
        self.samp_spinBox.setMaximum(1000000)
        self.samp_spinBox.setObjectName("samp_spinBox")
        self.gridLayout_2.addWidget(self.samp_spinBox, 2, 1, 1, 1)
        self.gridLayout.addWidget(self.groupBox, 0, 0, 1, 1)
        self.stream_button = QtWidgets.QPushButton(self.frame_4)
        self.stream_button.setEnabled(False)
        self.stream_button.setObjectName("stream_button")
        self.gridLayout.addWidget(self.stream_button, 3, 0, 1, 1)
        self.horizontalLayout_5.addWidget(self.frame_4)
        self.tabWidget = QtWidgets.QTabWidget(self.frame_3)
        self.tabWidget.setMinimumSize(QtCore.QSize(300, 150))
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.tab)
        self.horizontalLayout_3.setContentsMargins(11, 11, 11, 11)
        self.horizontalLayout_3.setSpacing(6)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.table = QtWidgets.QTableWidget(self.tab)
        self.table.setEnabled(False)
        self.table.setDragEnabled(True)
        self.table.setRowCount(50)
        self.table.setColumnCount(10)
        self.table.setObjectName("table")
        self.table.horizontalHeader().setSortIndicatorShown(False)
        self.table.verticalHeader().setDefaultSectionSize(16)
        self.table.verticalHeader().setMinimumSectionSize(16)
        self.table.verticalHeader().setSortIndicatorShown(False)
        self.horizontalLayout_3.addWidget(self.table)
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.tab_2)
        self.verticalLayout_3.setContentsMargins(11, 11, 11, 11)
        self.verticalLayout_3.setSpacing(6)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.terminal_text = QtWidgets.QPlainTextEdit(self.tab_2)
        self.terminal_text.setEnabled(True)
        self.terminal_text.setAutoFillBackground(False)
        self.terminal_text.setTabChangesFocus(False)
        self.terminal_text.setUndoRedoEnabled(False)
        self.terminal_text.setReadOnly(True)
        self.terminal_text.setTextInteractionFlags(QtCore.Qt.NoTextInteraction)
        self.terminal_text.setCenterOnScroll(False)
        self.terminal_text.setObjectName("terminal_text")
        self.verticalLayout_3.addWidget(self.terminal_text)
        self.widget_4 = QtWidgets.QWidget(self.tab_2)
        self.widget_4.setMinimumSize(QtCore.QSize(0, 0))
        self.widget_4.setObjectName("widget_4")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.widget_4)
        self.horizontalLayout_4.setContentsMargins(11, 11, 11, 11)
        self.horizontalLayout_4.setSpacing(6)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label_4 = QtWidgets.QLabel(self.widget_4)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_4.addWidget(self.label_4)
        self.terminal_line = QtWidgets.QLineEdit(self.widget_4)
        self.terminal_line.setEnabled(False)
        self.terminal_line.setClearButtonEnabled(False)
        self.terminal_line.setObjectName("terminal_line")
        self.horizontalLayout_4.addWidget(self.terminal_line)
        self.verticalLayout_3.addWidget(self.widget_4)
        self.tabWidget.addTab(self.tab_2, "")
        self.horizontalLayout_5.addWidget(self.tabWidget)
        self.verticalLayout.addWidget(self.frame_3)
        self.plot = QtWidgets.QWidget(self.centralWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.plot.sizePolicy().hasHeightForWidth())
        self.plot.setSizePolicy(sizePolicy)
        self.plot.setMinimumSize(QtCore.QSize(0, 150))
        self.plot.setObjectName("plot")
        self.verticalLayout.addWidget(self.plot)
        MainWindow.setCentralWidget(self.centralWidget)
        self.mainToolBar = QtWidgets.QToolBar(MainWindow)
        self.mainToolBar.setObjectName("mainToolBar")
        MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.mainToolBar)
        self.statusBar = QtWidgets.QStatusBar(MainWindow)
        self.statusBar.setObjectName("statusBar")
        MainWindow.setStatusBar(self.statusBar)
        self.menuBar = QtWidgets.QMenuBar(MainWindow)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 600, 17))
        self.menuBar.setObjectName("menuBar")
        MainWindow.setMenuBar(self.menuBar)
        self.actionSave_as = QtWidgets.QAction(MainWindow)
        self.actionSave_as.setObjectName("actionSave_as")
        self.actionSave = QtWidgets.QAction(MainWindow)
        self.actionSave.setObjectName("actionSave")
        self.actionExtract = QtWidgets.QAction(MainWindow)
        self.actionExtract.setObjectName("actionExtract")

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Quantum"))
        self.label.setText(_translate("MainWindow", "Save at: "))
        self.save_line.setText(_translate("MainWindow", "output.csv"))
        self.save_button.setText(_translate("MainWindow", "Open"))
        self.channels_button.setText(_translate("MainWindow", "Channels"))
        self.groupBox.setTitle(_translate("MainWindow", "Global properties"))
        self.label_2.setText(_translate("MainWindow", "Port:"))
        self.label_3.setText(_translate("MainWindow", "Sampling (ms):"))
        self.label_5.setText(_translate("MainWindow", "Coincidence\n"
"Window (ns):"))
        self.stream_button.setText(_translate("MainWindow", "Stream"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "Data"))
        self.label_4.setText(_translate("MainWindow", "Input:"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "Terminal"))
        self.actionSave_as.setText(_translate("MainWindow", "Save as"))
        self.actionSave.setText(_translate("MainWindow", "Save"))
        self.actionExtract.setText(_translate("MainWindow", "Extract"))

