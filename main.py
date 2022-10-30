#  Created by cosm1c.
#  29 October of 2022y.

import math_funcs as m_f
from mainGUI import *

import sys
import numpy


detalization = 1000
startX = 0.0001
endX = 100

class mainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.dialog = QtWidgets.QDialog()
        self.ui = Ui_dialog()

        self.ui.setupUi(self.dialog)


    def drawGraphs(self):

        countPoint = (endX - startX) / detalization
        x = numpy.arange(startX, endX, countPoint)
        y = []
        y1 = []
        y2 = []

        for i in range(detalization):
            y.append(m_f.func(x[i]))
            y1.append(m_f.funcFirstDerivative(x[i]))
            y2.append(m_f.funcSecondDerivative(x[i]))

        self.ui.graphMain.showGrid(1, 1, 1)
        self.ui.graphMain.setYRange(-5, 5, padding=0)

        self.ui.graphFirst.showGrid(1, 1, 1)
        self.ui.graphFirst.setYRange(-5, 5, padding=0)

        self.ui.graphSecond.showGrid(1, 1, 1)
        self.ui.graphSecond.setYRange(-5, 5, padding=0)

        self.ui.graphMain.plot(x, y, pen=(1, 1))
        self.ui.graphFirst.plot(x, y1, pen=(1, 2))
        self.ui.graphSecond.plot(x, y2, pen=(1, 3))


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    ui = mainWindow()
    ui.dialog.show()
    ui.drawGraphs()

    sys.exit(app.exec_())



# if __name__ == "__main__":
#     import sys
#     app = QtWidgets.QApplication(sys.argv)
#     dialog = QtWidgets.QDialog()
#     ui = Ui_dialog()
#     ui.setupUi(dialog)
#     dialog.show()
#     sys.exit(app.exec_())