# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'GUI\Program\mainwindow.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(650, 684)
        MainWindow.setUnifiedTitleAndToolBarOnMac(False)
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
        self.save_line.setText("")
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
        self.coin_spinBox.setMinimum(0)
        self.coin_spinBox.setMaximum(99)
        self.coin_spinBox.setSingleStep(1)
        self.coin_spinBox.setProperty("value", 0)
        self.coin_spinBox.setObjectName("coin_spinBox")
        self.gridLayout_2.addWidget(self.coin_spinBox, 3, 1, 1, 1)
        self.samp_spinBox = QtWidgets.QSpinBox(self.groupBox)
        self.samp_spinBox.setEnabled(False)
        self.samp_spinBox.setMaximumSize(QtCore.QSize(100, 16777215))
        self.samp_spinBox.setCorrectionMode(QtWidgets.QAbstractSpinBox.CorrectToNearestValue)
        self.samp_spinBox.setKeyboardTracking(False)
        self.samp_spinBox.setMinimum(0)
        self.samp_spinBox.setMaximum(99)
        self.samp_spinBox.setProperty("value", 0)
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
        self.tabWidget.addTab(self.tab, "")
        self.tab_3 = QtWidgets.QWidget()
        self.tab_3.setObjectName("tab_3")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.tab_3)
        self.verticalLayout_2.setContentsMargins(11, 11, 11, 11)
        self.verticalLayout_2.setSpacing(6)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.tabWidget.addTab(self.tab_3, "")
        self.horizontalLayout_5.addWidget(self.tabWidget)
        self.verticalLayout.addWidget(self.frame_3)
        self.plot_widget = QtWidgets.QWidget(self.centralWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.plot_widget.sizePolicy().hasHeightForWidth())
        self.plot_widget.setSizePolicy(sizePolicy)
        self.plot_widget.setMinimumSize(QtCore.QSize(0, 300))
        self.plot_widget.setObjectName("plot_widget")
        self.plot_layout = QtWidgets.QVBoxLayout(self.plot_widget)
        self.plot_layout.setContentsMargins(11, 11, 11, 11)
        self.plot_layout.setSpacing(6)
        self.plot_layout.setObjectName("plot_layout")
        self.verticalLayout.addWidget(self.plot_widget)
        MainWindow.setCentralWidget(self.centralWidget)
        self.statusBar = QtWidgets.QStatusBar(MainWindow)
        self.statusBar.setObjectName("statusBar")
        MainWindow.setStatusBar(self.statusBar)
        self.menuBar = QtWidgets.QMenuBar(MainWindow)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 650, 21))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.menuBar.sizePolicy().hasHeightForWidth())
        self.menuBar.setSizePolicy(sizePolicy)
        self.menuBar.setAutoFillBackground(False)
        self.menuBar.setDefaultUp(True)
        self.menuBar.setObjectName("menuBar")
        self.menuProperties = QtWidgets.QMenu(self.menuBar)
        self.menuProperties.setObjectName("menuProperties")
        self.menuHelp = QtWidgets.QMenu(self.menuBar)
        self.menuHelp.setObjectName("menuHelp")
        self.menuFile = QtWidgets.QMenu(self.menuBar)
        self.menuFile.setObjectName("menuFile")
        MainWindow.setMenuBar(self.menuBar)
        self.actionSave_as = QtWidgets.QAction(MainWindow)
        self.actionSave_as.setObjectName("actionSave_as")
        self.actionSave = QtWidgets.QAction(MainWindow)
        self.actionSave.setObjectName("actionSave")
        self.actionExtract = QtWidgets.QAction(MainWindow)
        self.actionExtract.setObjectName("actionExtract")
        self.actionConfigure_email = QtWidgets.QAction(MainWindow)
        self.actionConfigure_email.setObjectName("actionConfigure_email")
        self.actionDefault_properties = QtWidgets.QAction(MainWindow)
        self.actionDefault_properties.setObjectName("actionDefault_properties")
        self.actionAbout = QtWidgets.QAction(MainWindow)
        self.actionAbout.setObjectName("actionAbout")
        self.actionSave_as_2 = QtWidgets.QAction(MainWindow)
        self.actionSave_as_2.setObjectName("actionSave_as_2")
        self.actionExit = QtWidgets.QAction(MainWindow)
        self.actionExit.setObjectName("actionExit")
        self.actionChannels = QtWidgets.QAction(MainWindow)
        self.actionChannels.setObjectName("actionChannels")
        self.menuProperties.addAction(self.actionChannels)
        self.menuProperties.addAction(self.actionDefault_properties)
        self.menuHelp.addAction(self.actionAbout)
        self.menuFile.addAction(self.actionSave_as_2)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionExit)
        self.menuBar.addAction(self.menuFile.menuAction())
        self.menuBar.addAction(self.menuProperties.menuAction())
        self.menuBar.addAction(self.menuHelp.menuAction())

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Quantum"))
        self.label.setText(_translate("MainWindow", "Save as: "))
        self.save_button.setText(_translate("MainWindow", "Browse"))
        self.channels_button.setText(_translate("MainWindow", "Channels"))
        self.groupBox.setTitle(_translate("MainWindow", "Global properties"))
        self.label_2.setText(_translate("MainWindow", "Port:"))
        self.label_3.setText(_translate("MainWindow", "Sampling (ms):"))
        self.label_5.setText(_translate("MainWindow", "Coincidence\n"
"Window (ns):"))
        self.stream_button.setText(_translate("MainWindow", "Stream"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "Data"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), _translate("MainWindow", "Current"))
        self.menuProperties.setTitle(_translate("MainWindow", "Edit"))
        self.menuHelp.setTitle(_translate("MainWindow", "Help"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.actionSave_as.setText(_translate("MainWindow", "Save as"))
        self.actionSave.setText(_translate("MainWindow", "Save"))
        self.actionExtract.setText(_translate("MainWindow", "Extract"))
        self.actionConfigure_email.setText(_translate("MainWindow", "Configure email"))
        self.actionDefault_properties.setText(_translate("MainWindow", "Default"))
        self.actionAbout.setText(_translate("MainWindow", "About"))
        self.actionSave_as_2.setText(_translate("MainWindow", "Save as"))
        self.actionExit.setText(_translate("MainWindow", "Exit"))
        self.actionChannels.setText(_translate("MainWindow", "Channels"))

