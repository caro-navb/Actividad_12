# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainwindow.ui'
##
## Created by: Qt User Interface Compiler version 5.15.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(506, 530)
        self.actionAbrir = QAction(MainWindow)
        self.actionAbrir.setObjectName(u"actionAbrir")
        self.actionGuardar = QAction(MainWindow)
        self.actionGuardar.setObjectName(u"actionGuardar")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout_2 = QGridLayout(self.centralwidget)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.groupBox = QGroupBox(self.centralwidget)
        self.groupBox.setObjectName(u"groupBox")
        self.gridLayout = QGridLayout(self.groupBox)
        self.gridLayout.setObjectName(u"gridLayout")
        self.label_20 = QLabel(self.groupBox)
        self.label_20.setObjectName(u"label_20")

        self.gridLayout.addWidget(self.label_20, 0, 0, 1, 1)

        self.lineEdit_2 = QLineEdit(self.groupBox)
        self.lineEdit_2.setObjectName(u"lineEdit_2")

        self.gridLayout.addWidget(self.lineEdit_2, 0, 1, 1, 2)

        self.label_13 = QLabel(self.groupBox)
        self.label_13.setObjectName(u"label_13")

        self.gridLayout.addWidget(self.label_13, 1, 0, 1, 2)

        self.spinBox_13 = QSpinBox(self.groupBox)
        self.spinBox_13.setObjectName(u"spinBox_13")
        self.spinBox_13.setMaximum(500)

        self.gridLayout.addWidget(self.spinBox_13, 1, 3, 1, 1)

        self.label_12 = QLabel(self.groupBox)
        self.label_12.setObjectName(u"label_12")

        self.gridLayout.addWidget(self.label_12, 2, 0, 1, 2)

        self.spinBox_16 = QSpinBox(self.groupBox)
        self.spinBox_16.setObjectName(u"spinBox_16")
        self.spinBox_16.setMaximum(500)

        self.gridLayout.addWidget(self.spinBox_16, 2, 3, 1, 1)

        self.label_18 = QLabel(self.groupBox)
        self.label_18.setObjectName(u"label_18")

        self.gridLayout.addWidget(self.label_18, 3, 0, 1, 2)

        self.spinBox_15 = QSpinBox(self.groupBox)
        self.spinBox_15.setObjectName(u"spinBox_15")
        self.spinBox_15.setMaximum(500)

        self.gridLayout.addWidget(self.spinBox_15, 3, 3, 1, 1)

        self.label_16 = QLabel(self.groupBox)
        self.label_16.setObjectName(u"label_16")

        self.gridLayout.addWidget(self.label_16, 4, 0, 1, 2)

        self.spinBox_11 = QSpinBox(self.groupBox)
        self.spinBox_11.setObjectName(u"spinBox_11")
        self.spinBox_11.setMaximum(500)

        self.gridLayout.addWidget(self.spinBox_11, 4, 3, 1, 1)

        self.label_15 = QLabel(self.groupBox)
        self.label_15.setObjectName(u"label_15")

        self.gridLayout.addWidget(self.label_15, 5, 0, 1, 2)

        self.lineEdit = QLineEdit(self.groupBox)
        self.lineEdit.setObjectName(u"lineEdit")

        self.gridLayout.addWidget(self.lineEdit, 5, 3, 1, 1)

        self.label_14 = QLabel(self.groupBox)
        self.label_14.setObjectName(u"label_14")

        self.gridLayout.addWidget(self.label_14, 6, 0, 1, 2)

        self.label_11 = QLabel(self.groupBox)
        self.label_11.setObjectName(u"label_11")

        self.gridLayout.addWidget(self.label_11, 7, 1, 1, 1)

        self.spinBox_9 = QSpinBox(self.groupBox)
        self.spinBox_9.setObjectName(u"spinBox_9")
        self.spinBox_9.setMaximum(255)

        self.gridLayout.addWidget(self.spinBox_9, 7, 3, 1, 1)

        self.label_17 = QLabel(self.groupBox)
        self.label_17.setObjectName(u"label_17")

        self.gridLayout.addWidget(self.label_17, 8, 1, 1, 1)

        self.spinBox_10 = QSpinBox(self.groupBox)
        self.spinBox_10.setObjectName(u"spinBox_10")
        self.spinBox_10.setMaximum(255)

        self.gridLayout.addWidget(self.spinBox_10, 8, 3, 1, 1)

        self.label_19 = QLabel(self.groupBox)
        self.label_19.setObjectName(u"label_19")

        self.gridLayout.addWidget(self.label_19, 9, 1, 1, 1)

        self.spinBox_14 = QSpinBox(self.groupBox)
        self.spinBox_14.setObjectName(u"spinBox_14")
        self.spinBox_14.setMaximum(255)

        self.gridLayout.addWidget(self.spinBox_14, 9, 3, 1, 1)

        self.pushButton_3 = QPushButton(self.groupBox)
        self.pushButton_3.setObjectName(u"pushButton_3")

        self.gridLayout.addWidget(self.pushButton_3, 10, 1, 1, 1)

        self.pushButton = QPushButton(self.groupBox)
        self.pushButton.setObjectName(u"pushButton")

        self.gridLayout.addWidget(self.pushButton, 10, 2, 1, 1)

        self.plainTextEdit = QPlainTextEdit(self.groupBox)
        self.plainTextEdit.setObjectName(u"plainTextEdit")

        self.gridLayout.addWidget(self.plainTextEdit, 10, 3, 2, 1)

        self.pushButton_4 = QPushButton(self.groupBox)
        self.pushButton_4.setObjectName(u"pushButton_4")

        self.gridLayout.addWidget(self.pushButton_4, 11, 1, 1, 2)

        self.buscar_pushButton = QPushButton(self.groupBox)
        self.buscar_pushButton.setObjectName(u"buscar_pushButton")

        self.gridLayout.addWidget(self.buscar_pushButton, 12, 1, 1, 2)

        self.buscar_lineEdit = QLineEdit(self.groupBox)
        self.buscar_lineEdit.setObjectName(u"buscar_lineEdit")

        self.gridLayout.addWidget(self.buscar_lineEdit, 12, 3, 1, 1)

        self.mostrar_tabla_pushButton = QPushButton(self.groupBox)
        self.mostrar_tabla_pushButton.setObjectName(u"mostrar_tabla_pushButton")

        self.gridLayout.addWidget(self.mostrar_tabla_pushButton, 13, 1, 1, 2)

        self.tabla = QTableWidget(self.groupBox)
        if (self.tabla.columnCount() < 10):
            self.tabla.setColumnCount(10)
        __qtablewidgetitem = QTableWidgetItem()
        self.tabla.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tabla.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tabla.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.tabla.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.tabla.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.tabla.setHorizontalHeaderItem(5, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem()
        self.tabla.setHorizontalHeaderItem(6, __qtablewidgetitem6)
        __qtablewidgetitem7 = QTableWidgetItem()
        self.tabla.setHorizontalHeaderItem(7, __qtablewidgetitem7)
        __qtablewidgetitem8 = QTableWidgetItem()
        self.tabla.setHorizontalHeaderItem(8, __qtablewidgetitem8)
        __qtablewidgetitem9 = QTableWidgetItem()
        self.tabla.setHorizontalHeaderItem(9, __qtablewidgetitem9)
        self.tabla.setObjectName(u"tabla")

        self.gridLayout.addWidget(self.tabla, 13, 3, 1, 1)


        self.gridLayout_2.addWidget(self.groupBox, 0, 0, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Capturador de part\u00edculas", None))
        self.actionAbrir.setText(QCoreApplication.translate("MainWindow", u"Abrir", None))
#if QT_CONFIG(shortcut)
        self.actionAbrir.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+O", None))
#endif // QT_CONFIG(shortcut)
        self.actionGuardar.setText(QCoreApplication.translate("MainWindow", u"Guardar", None))
#if QT_CONFIG(shortcut)
        self.actionGuardar.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+S", None))
#endif // QT_CONFIG(shortcut)
        self.groupBox.setTitle(QCoreApplication.translate("MainWindow", u"Part\u00edculas", None))
        self.label_20.setText(QCoreApplication.translate("MainWindow", u"ID:", None))
        self.label_13.setText(QCoreApplication.translate("MainWindow", u"Origen en x:", None))
        self.label_12.setText(QCoreApplication.translate("MainWindow", u"Origen en y:", None))
        self.label_18.setText(QCoreApplication.translate("MainWindow", u"Destino en x:", None))
        self.label_16.setText(QCoreApplication.translate("MainWindow", u"Destino en y:", None))
        self.label_15.setText(QCoreApplication.translate("MainWindow", u"Velocidad:", None))
        self.label_14.setText(QCoreApplication.translate("MainWindow", u"Color (rgb):", None))
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"Red", None))
        self.label_17.setText(QCoreApplication.translate("MainWindow", u"Green", None))
        self.label_19.setText(QCoreApplication.translate("MainWindow", u"Blue", None))
        self.pushButton_3.setText(QCoreApplication.translate("MainWindow", u"Agregar al inicio", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"Agregar al final", None))
        self.pushButton_4.setText(QCoreApplication.translate("MainWindow", u"Mostrar", None))
        self.buscar_pushButton.setText(QCoreApplication.translate("MainWindow", u"Buscar", None))
        self.mostrar_tabla_pushButton.setText(QCoreApplication.translate("MainWindow", u"Mostrar tabla", None))
        ___qtablewidgetitem = self.tabla.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"ID", None));
        ___qtablewidgetitem1 = self.tabla.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"Origen_x", None));
        ___qtablewidgetitem2 = self.tabla.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"Origen_y", None));
        ___qtablewidgetitem3 = self.tabla.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("MainWindow", u"Destino_x", None));
        ___qtablewidgetitem4 = self.tabla.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("MainWindow", u"Destino_y", None));
        ___qtablewidgetitem5 = self.tabla.horizontalHeaderItem(5)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("MainWindow", u"Velocidad", None));
        ___qtablewidgetitem6 = self.tabla.horizontalHeaderItem(6)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("MainWindow", u"Red", None));
        ___qtablewidgetitem7 = self.tabla.horizontalHeaderItem(7)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("MainWindow", u"Green", None));
        ___qtablewidgetitem8 = self.tabla.horizontalHeaderItem(8)
        ___qtablewidgetitem8.setText(QCoreApplication.translate("MainWindow", u"Blue", None));
        ___qtablewidgetitem9 = self.tabla.horizontalHeaderItem(9)
        ___qtablewidgetitem9.setText(QCoreApplication.translate("MainWindow", u"Distancia", None));
    # retranslateUi

