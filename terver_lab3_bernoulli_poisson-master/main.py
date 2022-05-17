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
        self.changeSolveType()
        self.changeFormula()
        self.ui.formula_img.setPixmap(QPixmap("img/0.png"))

        self.ui.result_button.clicked.connect(self.solveProblem)
        self.ui.solveType.currentIndexChanged.connect(self.changeSolveType)
        self.ui.formulaType.currentIndexChanged.connect(self.changeFormula)

    
    def solveProblem(self):
        solveType = self.ui.solveType.currentIndex()
        n = self.ui.n_spinBox.value()
        p = self.ui.p_spinBox.value()

        if solveType == 0:
            m1 = self.ui.m1_spinBox.value()
            m2 = m1
        elif solveType == 1:
            m1 = 0
            m2 = self.ui.m1_spinBox.value() - 1
        elif solveType == 2:
            m1 = self.ui.m1_spinBox.value()
            m2 = n
        else:
            m1 = self.ui.m1_spinBox.value()
            m2 = self.ui.m2_spinBox.value()

        if m1 > n or m2 > n:
            QtWidgets.QMessageBox.warning(self, "Ошибка ввода", "m не должно быть больше n")
            return

        if m2 < m1:
            QtWidgets.QMessageBox.warning(self, "Ошибка ввода", "m1 не может превышать значения m2")
            return
            
        result = 0
        if (self.ui.formulaType.currentIndex() == 0):
            for m in range(m1, m2 + 1):
                result += bernully(p, n, m)
        else:
            for m in range(m1, m2 + 1):
                result += puasson(p, n, m)
                print(result)
        
        result = "{:01.12f}".format(result)

        self.ui.result_lineEdit.setText(str(result))

    
    def changeSolveType(self):
        isVisible = False
        labelText = "m"
        
        if self.ui.solveType.currentIndex() == 3:
            isVisible = True
            labelText = "m1"
        
        self.ui.m2_label.setVisible(isVisible)
        self.ui.m2_spinBox.setVisible(isVisible)
        self.ui.m1_label.setText(labelText)

    
    def changeFormula(self):
        n_minimum = [1, 500]
        restriction = "%d ≤ n"

        formula = self.ui.formulaType.currentIndex()
        self.ui.formula_img.setPixmap(QPixmap("img/" + str(formula) + ".png"))
        self.ui.n_spinBox.setMinimum(n_minimum[formula])
        restriction = restriction % (n_minimum[formula])
        self.ui.restriction_label.setText(restriction)


if __name__ == '__main__': 
    app = QtWidgets.QApplication([])
    application = mywindow()
    application.show()
    
    sys.exit(app.exec())