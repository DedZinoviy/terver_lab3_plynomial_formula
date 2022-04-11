from formules import *
from  PyQt5 import QtWidgets
from PyQt5 import QtCore
from PyQt5.QtGui import QPixmap
from ui import Ui_MainWindow
import sys

class mywindow(QtWidgets.QMainWindow):
    '''Конструктор гловного окна'''
    def __init__(self):
        super(mywindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.formula_img.setPixmap(QPixmap("img/0.png"))

        self.ui.result_button.clicked.connect(self.solveProblem)
        self.ui.k_spinBox.valueChanged.connect(self.changeRowCount)


    def changeRowCount(self):
        previousRowCount = self.ui.table.rowCount()
        rowCount = self.ui.k_spinBox.value()
        self.ui.table.setRowCount(rowCount)
        for i in range (previousRowCount, rowCount):
            self.ui.table.setItem(i, 0, QtWidgets.QTableWidgetItem("0.5"))
            self.ui.table.setItem(i, 1, QtWidgets.QTableWidgetItem("0"))

    
    def solveProblem(self):
        n = self.ui.n_spinBox.value()
        p_list = []
        m_list = []
        try:
            for i in range(self.ui.table.rowCount()):
                p = float(self.ui.table.item(i, 0).text())
                m = int(self.ui.table.item(i, 1).text())

                if p < 0 or p > 1:
                    QtWidgets.QMessageBox.warning(self, "Ошибка ввода", "Некорректный диапазон значения p в строке " + str(i))
                    return

                p_list.append(p)
                m_list.append(m)
        except:
            QtWidgets.QMessageBox.warning(self, "Ошибка ввода", "Некорректный ввод в строке " + str(i))
            return

        s = sum(m_list)
        if s != n:
            QtWidgets.QMessageBox.warning(self, "Ошибка ввода", "Сумма m не равна n")
            return

        result = pollinom(n, p_list, m_list)
        self.ui.result_SpinBox.setValue(result)

        



if __name__ == '__main__': 
    app = QtWidgets.QApplication([])
    application = mywindow()
    application.show()
    
    sys.exit(app.exec())