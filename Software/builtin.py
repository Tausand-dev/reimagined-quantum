import constants
import common
from files import File
import PyAbacus as abacus


import numpy as np
import pyqtgraph as pg
from threading import Thread
from PyQt5 import QtWidgets, QtGui, QtCore
from supportWidgets import ClickableLineEdit

class SweepDialogBase(QtWidgets.QDialog):
    def __init__(self, parent):
        super(SweepDialogBase, self).__init__(parent)
        self.resize(400, 500)

        self.parent = parent

        self.verticalLayout = QtWidgets.QVBoxLayout(self)
        self.verticalLayout.setContentsMargins(11, 11, 11, 11)
        self.verticalLayout.setSpacing(6)

        self.frame = QtWidgets.QFrame()

        self.horizontalLayout = QtWidgets.QHBoxLayout(self.frame)
        self.horizontalLayout.setContentsMargins(11, 11, 11, 11)
        self.horizontalLayout.setSpacing(6)

        label = QtWidgets.QLabel("Save as:")
        self.lineEdit = ClickableLineEdit(self)
        self.lineEdit.clicked.connect(self.chooseFile)

        self.horizontalLayout.addWidget(label)
        self.horizontalLayout.addWidget(self.lineEdit)
        self.verticalLayout.addWidget(self.frame)

        self.groupBox = QtWidgets.QGroupBox("Settings")

        self.formLayout = QtWidgets.QFormLayout(self.groupBox)

        startLabel = QtWidgets.QLabel("Start time (ns):")
        stopLabel = QtWidgets.QLabel("Stop time (ns):")
        stepLabel = QtWidgets.QLabel("Step size (ns):")
        nLabel = QtWidgets.QLabel("Number of measurements per step:")

        self.startSpin = QtWidgets.QSpinBox()
        self.stopSpin = QtWidgets.QSpinBox()
        self.stepSpin = QtWidgets.QSpinBox()
        self.nSpin = QtWidgets.QSpinBox()
        self.nSpin.setMinimum(1)

        self.startSpin.valueChanged.connect(self.handleStart)

        self.formLayout.addRow(startLabel, self.startSpin)
        self.formLayout.addRow(stopLabel, self.stopSpin)
        self.formLayout.addRow(stepLabel, self.stepSpin)
        self.formLayout.addRow(nLabel, self.nSpin)

        self.verticalLayout.addWidget(self.groupBox)

        self.startStopButton = QtWidgets.QPushButton("Start")
        self.startStopButton.setMaximumSize(QtCore.QSize(140, 60))
        self.verticalLayout.addWidget(self.startStopButton, alignment = QtCore.Qt.AlignRight)

        self.plot_win = pg.GraphicsWindow()
        self.plot = self.plot_win.addPlot()

        symbolSize = 5
        self.plot_line = self.plot.plot(pen = "r", symbol='o', symbolPen = "r", symbolBrush="r", symbolSize=symbolSize)
        self.verticalLayout.addWidget(self.plot_win)

        self.fileName = ""

        self.startStopButton.clicked.connect(self.startStop)

        self.x_data = []
        self.y_data = []

        self.completed = False

        self.timer = QtCore.QTimer()
        self.timer.setInterval(constants.CHECK_RATE)
        self.timer.timeout.connect(self.updatePlot)

        self.header = None

        self.error = None

    def handleStart(self, value):
        self.stopSpin.setMinimum(value + abacus.STEP_DELAY)

    def warning(self, error):
        error_text = str(error)
        msg = QtWidgets.QMessageBox()
        msg.setIcon(QtWidgets.QMessageBox.Warning)
        msg.setText(error_text)
        msg.setWindowTitle("Warning")
        msg.setStandardButtons(QtWidgets.QMessageBox.Ok | QtWidgets.QMessageBox.Cancel)
        return msg.exec_()

    def enableWidgets(self, enable):
        self.startSpin.setEnabled(enable)
        self.stopSpin.setEnabled(enable)
        self.stepSpin.setEnabled(enable)
        self.nSpin.setEnabled(enable)
        try:
            self.comboBox.setEnabled(enable)
        except:
            pass

    def updatePlot(self):
        self.plot_line.setData(self.x_data, self.y_data)
        if self.error != None:
            self.parent.errorWindow(self.error)
            self.error = None

        if self.completed:
            if self.fileName != "":
                file = File(self.fileName, self.header)
                data = np.vstack((self.x_data, self.y_data)).T
                file.npwrite(data, "%d" + constants.DELIMITER + "%d")

            self.x_data = []
            self.y_data = []
            self.timer.stop()
            self.completed = False
            self.startStopButton.setText("Start")
            self.enableWidgets(True)
            self.parent.check_timer.start()

    def cleanPlot(self):
        self.x_data = []
        self.y_data = []
        self.plot_line.setData(self.x_data, self.y_data)

    def chooseFile(self):
        try:
            directory = constants.directory_lineEdit
        except:
            directory = os.path.expanduser("~")

        dlg = QtWidgets.QFileDialog(directory = directory)
        dlg.setAcceptMode(QtWidgets.QFileDialog.AcceptSave)
        dlg.setFileMode(QtWidgets.QFileDialog.AnyFile)
        nameFilters = [constants.SUPPORTED_EXTENSIONS[extension] for extension in constants.SUPPORTED_EXTENSIONS]
        dlg.setNameFilters(nameFilters)
        dlg.selectNameFilter(constants.SUPPORTED_EXTENSIONS[constants.EXTENSION_DATA])
        if dlg.exec_():
            name = dlg.selectedFiles()[0]
            self.fileName = common.unicodePath(name)
            self.lineEdit.setText(self.fileName)

    def stopAcquisition(self):
        e = Exception("Data acquisition is active, in order to make the sweep it will be turned off.")
        ans = self.warning(e)
        if ans == QtWidgets.QMessageBox.Ok:
            ans = True
        else: ans = False
        if ans: self.parent.startAcquisition()
        return ans

class SleepDialog(SweepDialogBase):
    def __init__(self, parent):
        super(SleepDialog, self).__init__(parent)

        self.setWindowTitle("Sleep time sweep")

        self.startSpin.setMinimum(-abacus.MAX_SLEEP)
        self.startSpin.setMaximum(abacus.MAX_DELAY - abacus.STEP_DELAY)
        self.startSpin.setSingleStep(abacus.STEP_DELAY)
        self.startSpin.setValue(abacus.MIN_DELAY)

        self.stopSpin.setMinimum(abacus.MIN_DELAY)
        self.stopSpin.setMaximum(abacus.MAX_DELAY)
        self.stopSpin.setSingleStep(abacus.STEP_DELAY)
        self.stopSpin.setValue(abacus.MAX_DELAY)

        self.stepSpin.setMinimum(abacus.STEP_DELAY)
        self.stepSpin.setMaximum(((abacus.MAX_DELAY - abacus.MIN_DELAY) // abacus.STEP_DELAY) * abacus.STEP_DELAY)
        self.stepSpin.setSingleStep(abacus.STEP_DELAY)

        self.plot.setLabel('left', "Counts")
        self.plot.setLabel('bottom', "Sleep time", units='ns')

    def startStop(self):
        pass

class DelayDialog(SweepDialogBase):
    def __init__(self, parent):
        super(DelayDialog, self).__init__(parent)

        self.parent = parent

        self.setWindowTitle("Delay time sweep")

        label = QtWidgets.QLabel("Channel:")
        self.comboBox = QtWidgets.QComboBox()
        self.comboBox.addItems(["A", "B"])

        self.formLayout.insertRow(0, label, self.comboBox)

        self.startSpin.setMinimum(abacus.MIN_DELAY)
        self.startSpin.setMaximum(abacus.MAX_DELAY - abacus.STEP_DELAY)
        self.startSpin.setSingleStep(abacus.STEP_DELAY)
        self.startSpin.setValue(abacus.MIN_DELAY)

        self.stopSpin.setMinimum(abacus.MIN_DELAY)
        self.stopSpin.setMaximum(abacus.MAX_DELAY)
        self.stopSpin.setSingleStep(abacus.STEP_DELAY)
        self.stopSpin.setValue(abacus.MAX_DELAY)

        self.stepSpin.setMinimum(abacus.STEP_DELAY)
        self.stepSpin.setMaximum(((abacus.MAX_DELAY - abacus.MIN_DELAY) // abacus.STEP_DELAY) * abacus.STEP_DELAY)
        self.stepSpin.setSingleStep(abacus.STEP_DELAY)

        self.plot.setLabel('left', "Coincidences")
        self.plot.setLabel('bottom', "Delay time", units='ns')

    def startStop(self):
        if self.startStopButton.text() == "Stop":
            self.timer.stop()
            self.completed = True
            self.updatePlot()
            self.completed = True

        else:
            step = self.stepSpin.value()
            n = self.nSpin.value()
            range_ = np.arange(self.startSpin.value(), self.stopSpin.value() + step, step)
            range_ = range_[range_ <= abacus.MAX_DELAY]
            channel = self.comboBox.currentText()

            if self.parent.experiment != None:
                if self.parent.streaming:
                    if self.stopAcquisition():
                        self.run(channel, n, range_)
                else:
                    self.run(channel, n, range_)
            else:
                self.parent.connect()
                if self.parent.experiment != None:
                    if self.parent.streaming:
                        if self.stopAcquisition():
                            self.run(channel, n, range_)
                    else:
                        self.run(channel, n, range_)

    def run(self, channel, n, range_):
        self.cleanPlot()
        self.completed = False
        self.startStopButton.setText("Stop")
        self.enableWidgets(False)

        self.header = "Delay time (ns)"  + constants.DELIMITER +  "Coincidences (%s)"%channel

        self.parent.check_timer.stop()
        thread = Thread(target = self.heavyDuty, args = (channel, n, range_))
        thread.daemon = True
        self.timer.start()
        thread.start()

    def heavyDuty(self, channel, n, range_):
        try:
            for (i, delay) in enumerate(range_):
                if not self.completed:
                    result = self.parent.experiment.delaySweep(channel, delay, n)
                    self.x_data.append(delay)
                    self.y_data.append(result)
                else:
                    break

            self.completed = True
        except Exception as e:
            self.completed = True
            self.error = e