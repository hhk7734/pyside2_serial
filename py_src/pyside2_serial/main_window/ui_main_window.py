# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main_window.ui'
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
        MainWindow.resize(626, 640)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.tabWidget = QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName(u"tabWidget")
        self.portTab = QWidget()
        self.portTab.setObjectName(u"portTab")
        self.verticalLayout_2 = QVBoxLayout(self.portTab)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.gridLayout_2 = QGridLayout()
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.portRefreshPushButton = QPushButton(self.portTab)
        self.portRefreshPushButton.setObjectName(u"portRefreshPushButton")

        self.gridLayout_2.addWidget(self.portRefreshPushButton, 0, 1, 1, 1)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.widget = QWidget(self.portTab)
        self.widget.setObjectName(u"widget")
        self.verticalLayout_7 = QVBoxLayout(self.widget)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.portNoParityRadioButton = QRadioButton(self.widget)
        self.portNoParityRadioButton.setObjectName(u"portNoParityRadioButton")
        self.portNoParityRadioButton.setChecked(True)

        self.verticalLayout_7.addWidget(self.portNoParityRadioButton)

        self.portOddParityRadioButton = QRadioButton(self.widget)
        self.portOddParityRadioButton.setObjectName(u"portOddParityRadioButton")

        self.verticalLayout_7.addWidget(self.portOddParityRadioButton)

        self.portEvenParityRadioButton = QRadioButton(self.widget)
        self.portEvenParityRadioButton.setObjectName(u"portEvenParityRadioButton")

        self.verticalLayout_7.addWidget(self.portEvenParityRadioButton)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_7.addItem(self.verticalSpacer_2)


        self.horizontalLayout.addWidget(self.widget)

        self.widget_2 = QWidget(self.portTab)
        self.widget_2.setObjectName(u"widget_2")
        self.verticalLayout_4 = QVBoxLayout(self.widget_2)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.port8BitsRadioButton = QRadioButton(self.widget_2)
        self.port8BitsRadioButton.setObjectName(u"port8BitsRadioButton")
        self.port8BitsRadioButton.setChecked(True)

        self.verticalLayout_4.addWidget(self.port8BitsRadioButton)

        self.port7BitsRadioButton = QRadioButton(self.widget_2)
        self.port7BitsRadioButton.setObjectName(u"port7BitsRadioButton")

        self.verticalLayout_4.addWidget(self.port7BitsRadioButton)

        self.port6BitsRadioButton = QRadioButton(self.widget_2)
        self.port6BitsRadioButton.setObjectName(u"port6BitsRadioButton")

        self.verticalLayout_4.addWidget(self.port6BitsRadioButton)

        self.port5BitsRadioButton = QRadioButton(self.widget_2)
        self.port5BitsRadioButton.setObjectName(u"port5BitsRadioButton")

        self.verticalLayout_4.addWidget(self.port5BitsRadioButton)

        self.verticalSpacer_5 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_4.addItem(self.verticalSpacer_5)


        self.horizontalLayout.addWidget(self.widget_2)

        self.widget_3 = QWidget(self.portTab)
        self.widget_3.setObjectName(u"widget_3")
        self.verticalLayout_5 = QVBoxLayout(self.widget_3)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.port1StopBitRadioButton = QRadioButton(self.widget_3)
        self.port1StopBitRadioButton.setObjectName(u"port1StopBitRadioButton")
        self.port1StopBitRadioButton.setChecked(True)

        self.verticalLayout_5.addWidget(self.port1StopBitRadioButton)

        self.port2StopBitRadioButton_9 = QRadioButton(self.widget_3)
        self.port2StopBitRadioButton_9.setObjectName(u"port2StopBitRadioButton_9")

        self.verticalLayout_5.addWidget(self.port2StopBitRadioButton_9)

        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_5.addItem(self.verticalSpacer_3)


        self.horizontalLayout.addWidget(self.widget_3)

        self.widget_4 = QWidget(self.portTab)
        self.widget_4.setObjectName(u"widget_4")
        self.verticalLayout_6 = QVBoxLayout(self.widget_4)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.portNoFlowControlRadioButton = QRadioButton(self.widget_4)
        self.portNoFlowControlRadioButton.setObjectName(u"portNoFlowControlRadioButton")
        self.portNoFlowControlRadioButton.setChecked(True)

        self.verticalLayout_6.addWidget(self.portNoFlowControlRadioButton)

        self.portHardwareControlRadioButton = QRadioButton(self.widget_4)
        self.portHardwareControlRadioButton.setObjectName(u"portHardwareControlRadioButton")
        self.portHardwareControlRadioButton.setChecked(False)

        self.verticalLayout_6.addWidget(self.portHardwareControlRadioButton)

        self.portSoftwareControlRadioButton = QRadioButton(self.widget_4)
        self.portSoftwareControlRadioButton.setObjectName(u"portSoftwareControlRadioButton")

        self.verticalLayout_6.addWidget(self.portSoftwareControlRadioButton)

        self.verticalSpacer_4 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_6.addItem(self.verticalSpacer_4)


        self.horizontalLayout.addWidget(self.widget_4)


        self.gridLayout_2.addLayout(self.horizontalLayout, 7, 0, 1, 1)

        self.portOpenClosePushButton = QPushButton(self.portTab)
        self.portOpenClosePushButton.setObjectName(u"portOpenClosePushButton")

        self.gridLayout_2.addWidget(self.portOpenClosePushButton, 1, 1, 1, 1)

        self.gridLayout_3 = QGridLayout()
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.label = QLabel(self.portTab)
        self.label.setObjectName(u"label")

        self.gridLayout_3.addWidget(self.label, 0, 0, 1, 1)

        self.portComboBox = QComboBox(self.portTab)
        self.portComboBox.setObjectName(u"portComboBox")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.portComboBox.sizePolicy().hasHeightForWidth())
        self.portComboBox.setSizePolicy(sizePolicy)
        self.portComboBox.setEditable(True)

        self.gridLayout_3.addWidget(self.portComboBox, 0, 1, 1, 1)

        self.label_2 = QLabel(self.portTab)
        self.label_2.setObjectName(u"label_2")

        self.gridLayout_3.addWidget(self.label_2, 1, 0, 1, 1)

        self.portBaudrateComboBox = QComboBox(self.portTab)
        self.portBaudrateComboBox.setObjectName(u"portBaudrateComboBox")
        sizePolicy.setHeightForWidth(self.portBaudrateComboBox.sizePolicy().hasHeightForWidth())
        self.portBaudrateComboBox.setSizePolicy(sizePolicy)
        self.portBaudrateComboBox.setEditable(False)

        self.gridLayout_3.addWidget(self.portBaudrateComboBox, 1, 1, 1, 1)


        self.gridLayout_2.addLayout(self.gridLayout_3, 0, 0, 2, 1)


        self.verticalLayout_2.addLayout(self.gridLayout_2)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer)

        self.tabWidget.addTab(self.portTab, "")
        self.textViewTab = QWidget()
        self.textViewTab.setObjectName(u"textViewTab")
        self.verticalLayout_8 = QVBoxLayout(self.textViewTab)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.gridLayout_4 = QGridLayout()
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.widget_5 = QWidget(self.textViewTab)
        self.widget_5.setObjectName(u"widget_5")
        self.verticalLayout_3 = QVBoxLayout(self.widget_5)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.textViewEnableCheckBox = QCheckBox(self.widget_5)
        self.textViewEnableCheckBox.setObjectName(u"textViewEnableCheckBox")

        self.verticalLayout_3.addWidget(self.textViewEnableCheckBox)

        self.label_3 = QLabel(self.widget_5)
        self.label_3.setObjectName(u"label_3")

        self.verticalLayout_3.addWidget(self.label_3)

        self.textViewMaxNumLinesSpinBox = QSpinBox(self.widget_5)
        self.textViewMaxNumLinesSpinBox.setObjectName(u"textViewMaxNumLinesSpinBox")
        self.textViewMaxNumLinesSpinBox.setMaximum(3000)
        self.textViewMaxNumLinesSpinBox.setValue(1000)

        self.verticalLayout_3.addWidget(self.textViewMaxNumLinesSpinBox)

        self.verticalSpacer_6 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_3.addItem(self.verticalSpacer_6)

        self.textViewClearPushButton = QPushButton(self.widget_5)
        self.textViewClearPushButton.setObjectName(u"textViewClearPushButton")

        self.verticalLayout_3.addWidget(self.textViewClearPushButton)


        self.gridLayout_4.addWidget(self.widget_5, 0, 0, 1, 1)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.textViewSendLineEdit = QLineEdit(self.textViewTab)
        self.textViewSendLineEdit.setObjectName(u"textViewSendLineEdit")

        self.horizontalLayout_2.addWidget(self.textViewSendLineEdit)

        self.textViewSendLineEndingComboBox = QComboBox(self.textViewTab)
        self.textViewSendLineEndingComboBox.addItem("")
        self.textViewSendLineEndingComboBox.addItem("")
        self.textViewSendLineEndingComboBox.addItem("")
        self.textViewSendLineEndingComboBox.addItem("")
        self.textViewSendLineEndingComboBox.setObjectName(u"textViewSendLineEndingComboBox")

        self.horizontalLayout_2.addWidget(self.textViewSendLineEndingComboBox)

        self.textViewSendPushButton = QPushButton(self.textViewTab)
        self.textViewSendPushButton.setObjectName(u"textViewSendPushButton")

        self.horizontalLayout_2.addWidget(self.textViewSendPushButton)


        self.gridLayout_4.addLayout(self.horizontalLayout_2, 1, 0, 1, 2)

        self.textViewPlainTextEdit = QPlainTextEdit(self.textViewTab)
        self.textViewPlainTextEdit.setObjectName(u"textViewPlainTextEdit")
        self.textViewPlainTextEdit.setUndoRedoEnabled(False)
        self.textViewPlainTextEdit.setReadOnly(True)

        self.gridLayout_4.addWidget(self.textViewPlainTextEdit, 0, 1, 1, 1)


        self.verticalLayout_8.addLayout(self.gridLayout_4)

        self.tabWidget.addTab(self.textViewTab, "")
        self.commandsTab = QWidget()
        self.commandsTab.setObjectName(u"commandsTab")
        self.tabWidget.addTab(self.commandsTab, "")

        self.gridLayout.addWidget(self.tabWidget, 0, 0, 1, 1)


        self.verticalLayout.addLayout(self.gridLayout)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 626, 22))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        self.tabWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.portRefreshPushButton.setText(QCoreApplication.translate("MainWindow", u"Refresh", None))
        self.portNoParityRadioButton.setText(QCoreApplication.translate("MainWindow", u"No Parity", None))
        self.portOddParityRadioButton.setText(QCoreApplication.translate("MainWindow", u"Odd Parity", None))
        self.portEvenParityRadioButton.setText(QCoreApplication.translate("MainWindow", u"Even Parity", None))
        self.port8BitsRadioButton.setText(QCoreApplication.translate("MainWindow", u"8 Bits", None))
        self.port7BitsRadioButton.setText(QCoreApplication.translate("MainWindow", u"7 Bits", None))
        self.port6BitsRadioButton.setText(QCoreApplication.translate("MainWindow", u"6 Bits", None))
        self.port5BitsRadioButton.setText(QCoreApplication.translate("MainWindow", u"5 Bits", None))
        self.port1StopBitRadioButton.setText(QCoreApplication.translate("MainWindow", u"1 Stop bit", None))
        self.port2StopBitRadioButton_9.setText(QCoreApplication.translate("MainWindow", u"2 Stop bit", None))
        self.portNoFlowControlRadioButton.setText(QCoreApplication.translate("MainWindow", u"No Flow Control", None))
        self.portHardwareControlRadioButton.setText(QCoreApplication.translate("MainWindow", u"Hardware Control", None))
        self.portSoftwareControlRadioButton.setText(QCoreApplication.translate("MainWindow", u"Software Control", None))
        self.portOpenClosePushButton.setText(QCoreApplication.translate("MainWindow", u"Open", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Port: ", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Baudrate: ", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.portTab), QCoreApplication.translate("MainWindow", u"Port", None))
        self.textViewEnableCheckBox.setText(QCoreApplication.translate("MainWindow", u"Enable", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Num. Lines:", None))
        self.textViewClearPushButton.setText(QCoreApplication.translate("MainWindow", u"Clear", None))
        self.textViewSendLineEndingComboBox.setItemText(0, QCoreApplication.translate("MainWindow", u"No line ending", None))
        self.textViewSendLineEndingComboBox.setItemText(1, QCoreApplication.translate("MainWindow", u"Newline(\\n)", None))
        self.textViewSendLineEndingComboBox.setItemText(2, QCoreApplication.translate("MainWindow", u"Carriage return(\\r)", None))
        self.textViewSendLineEndingComboBox.setItemText(3, QCoreApplication.translate("MainWindow", u"Both(\\r\\n)", None))

        self.textViewSendPushButton.setText(QCoreApplication.translate("MainWindow", u"Send", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.textViewTab), QCoreApplication.translate("MainWindow", u"Text View", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.commandsTab), QCoreApplication.translate("MainWindow", u"Commands", None))
    # retranslateUi

