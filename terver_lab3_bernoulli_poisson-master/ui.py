# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\varfolomey\Desktop\terver_lab3_bernoulli_poisson\ui.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(719, 377)
        MainWindow.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.formulaType = QtWidgets.QComboBox(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.formulaType.setFont(font)
        self.formulaType.setObjectName("formulaType")
        self.formulaType.addItem("")
        self.formulaType.addItem("")
        self.verticalLayout_2.addWidget(self.formulaType)
        self.formula_img = QtWidgets.QLabel(self.centralwidget)
        self.formula_img.setMinimumSize(QtCore.QSize(390, 140))
        self.formula_img.setAlignment(QtCore.Qt.AlignCenter)
        self.formula_img.setObjectName("formula_img")
        self.verticalLayout_2.addWidget(self.formula_img)
        self.restriction_label = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.restriction_label.setFont(font)
        self.restriction_label.setAlignment(QtCore.Qt.AlignCenter)
        self.restriction_label.setObjectName("restriction_label")
        self.verticalLayout_2.addWidget(self.restriction_label)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem)
        self.horizontalLayout.addLayout(self.verticalLayout_2)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.solveType = QtWidgets.QComboBox(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.solveType.setFont(font)
        self.solveType.setObjectName("solveType")
        self.solveType.addItem("")
        self.solveType.addItem("")
        self.solveType.addItem("")
        self.solveType.addItem("")
        self.verticalLayout.addWidget(self.solveType)
        spacerItem1 = QtWidgets.QSpacerItem(296, 13, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem1)
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.n_spinBox = QtWidgets.QSpinBox(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.n_spinBox.setFont(font)
        self.n_spinBox.setMaximum(100000)
        self.n_spinBox.setObjectName("n_spinBox")
        self.gridLayout.addWidget(self.n_spinBox, 0, 1, 1, 1)
        self.n_label = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.n_label.setFont(font)
        self.n_label.setTextFormat(QtCore.Qt.AutoText)
        self.n_label.setScaledContents(False)
        self.n_label.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.n_label.setObjectName("n_label")
        self.gridLayout.addWidget(self.n_label, 0, 0, 1, 1)
        self.m1_label = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.m1_label.setFont(font)
        self.m1_label.setObjectName("m1_label")
        self.gridLayout.addWidget(self.m1_label, 1, 0, 1, 1)
        self.m2_label = QtWidgets.QLabel(self.centralwidget)
        self.m2_label.setEnabled(True)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.m2_label.setFont(font)
        self.m2_label.setObjectName("m2_label")
        self.gridLayout.addWidget(self.m2_label, 2, 0, 1, 1)
        self.p_label = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.p_label.setFont(font)
        self.p_label.setObjectName("p_label")
        self.gridLayout.addWidget(self.p_label, 3, 0, 1, 1)
        self.m1_spinBox = QtWidgets.QSpinBox(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.m1_spinBox.setFont(font)
        self.m1_spinBox.setObjectName("m1_spinBox")
        self.gridLayout.addWidget(self.m1_spinBox, 1, 1, 1, 1)
        self.m2_spinBox = QtWidgets.QSpinBox(self.centralwidget)
        self.m2_spinBox.setEnabled(True)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.m2_spinBox.setFont(font)
        self.m2_spinBox.setObjectName("m2_spinBox")
        self.gridLayout.addWidget(self.m2_spinBox, 2, 1, 1, 1)
        self.p_spinBox = QtWidgets.QDoubleSpinBox(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.p_spinBox.setFont(font)
        self.p_spinBox.setDecimals(4)
        self.p_spinBox.setMaximum(1.0)
        self.p_spinBox.setSingleStep(0.001)
        self.p_spinBox.setObjectName("p_spinBox")
        self.gridLayout.addWidget(self.p_spinBox, 3, 1, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout)
        spacerItem2 = QtWidgets.QSpacerItem(296, 13, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem2)
        self.result_label = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.result_label.setFont(font)
        self.result_label.setObjectName("result_label")
        self.verticalLayout.addWidget(self.result_label)
        self.result_lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.result_lineEdit.setFont(font)
        self.result_lineEdit.setReadOnly(True)
        self.result_lineEdit.setObjectName("result_lineEdit")
        self.verticalLayout.addWidget(self.result_lineEdit)
        self.result_button = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.result_button.setFont(font)
        self.result_button.setObjectName("result_button")
        self.verticalLayout.addWidget(self.result_button)
        self.horizontalLayout.addLayout(self.verticalLayout)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 719, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.formulaType.setItemText(0, _translate("MainWindow", "?????????????? ????????????????"))
        self.formulaType.setItemText(1, _translate("MainWindow", "?????????????? ????????????????"))
        self.formula_img.setText(_translate("MainWindow", "TextLabel"))
        self.restriction_label.setText(_translate("MainWindow", "TextLabel"))
        self.solveType.setItemText(0, _translate("MainWindow", "Pn(k=m)"))
        self.solveType.setItemText(1, _translate("MainWindow", "Pn(k<m)"))
        self.solveType.setItemText(2, _translate("MainWindow", "Pn(k???m)"))
        self.solveType.setItemText(3, _translate("MainWindow", "Pn(m1???k???m2)"))
        self.n_label.setText(_translate("MainWindow", "n"))
        self.m1_label.setText(_translate("MainWindow", "m1"))
        self.m2_label.setText(_translate("MainWindow", "m2"))
        self.p_label.setText(_translate("MainWindow", "p"))
        self.result_label.setText(_translate("MainWindow", "??????????????????????"))
        self.result_button.setText(_translate("MainWindow", "????????????"))
