# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file '單位換算機.ui'
##
## Created by: Qt User Interface Compiler version 6.5.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QComboBox, QGridLayout, QHBoxLayout,
    QLabel, QLineEdit, QSizePolicy, QSpacerItem,
    QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(499, 269)
        Form.setStyleSheet(u".QComboBox{\n"
"	border-radius:10%;\n"
"	border:1 px solid black;\n"
"}\n"
".QLineEdit{\n"
"	border-radius:10%;\n"
"	border:1 px solid black;\n"
"}\n"
".QComboBox:hover{\n"
"	background-color:rgb(170,255,255);\n"
"}\n"
".QLineEdit:hover{\n"
"	background-color:rgb(170,255,255);\n"
"}")
        self.horizontalLayout = QHBoxLayout(Form)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.InputLineEdit_1 = QLineEdit(Form)
        self.InputLineEdit_1.setObjectName(u"InputLineEdit_1")
        self.InputLineEdit_1.setMinimumSize(QSize(0, 40))
        self.InputLineEdit_1.setClearButtonEnabled(True)

        self.gridLayout.addWidget(self.InputLineEdit_1, 5, 0, 1, 1)

        self.unitComboBox_1 = QComboBox(Form)
        self.unitComboBox_1.setObjectName(u"unitComboBox_1")
        self.unitComboBox_1.setMinimumSize(QSize(177, 40))

        self.gridLayout.addWidget(self.unitComboBox_1, 5, 1, 1, 1)

        self.dataTypeCombobox = QComboBox(Form)
        self.dataTypeCombobox.setObjectName(u"dataTypeCombobox")
        self.dataTypeCombobox.setMinimumSize(QSize(100, 20))

        self.gridLayout.addWidget(self.dataTypeCombobox, 4, 0, 1, 2)

        self.unitComboBox_2 = QComboBox(Form)
        self.unitComboBox_2.setObjectName(u"unitComboBox_2")
        self.unitComboBox_2.setMinimumSize(QSize(0, 40))

        self.gridLayout.addWidget(self.unitComboBox_2, 6, 1, 1, 1)

        self.transDataLabel = QLabel(Form)
        self.transDataLabel.setObjectName(u"transDataLabel")
        self.transDataLabel.setMinimumSize(QSize(0, 50))
        self.transDataLabel.setMaximumSize(QSize(16777215, 30))
        font = QFont()
        font.setFamilies([u"\u5fae\u8edf\u6b63\u9ed1\u9ad4"])
        font.setPointSize(30)
        font.setBold(True)
        self.transDataLabel.setFont(font)

        self.gridLayout.addWidget(self.transDataLabel, 2, 0, 1, 2)

        self.InputLineEdit_2 = QLineEdit(Form)
        self.InputLineEdit_2.setObjectName(u"InputLineEdit_2")
        self.InputLineEdit_2.setMinimumSize(QSize(0, 40))
        self.InputLineEdit_2.setClearButtonEnabled(True)

        self.gridLayout.addWidget(self.InputLineEdit_2, 6, 0, 1, 1)

        self.VerticalSpacer = QSpacerItem(7, 20, QSizePolicy.Minimum, QSizePolicy.Maximum)

        self.gridLayout.addItem(self.VerticalSpacer, 3, 0, 1, 2)

        self.orginalDataLabel = QLabel(Form)
        self.orginalDataLabel.setObjectName(u"orginalDataLabel")
        self.orginalDataLabel.setMaximumSize(QSize(16777215, 30))
        font1 = QFont()
        font1.setFamilies([u"\u5fae\u8edf\u6b63\u9ed1\u9ad4"])
        font1.setPointSize(20)
        font1.setBold(True)
        self.orginalDataLabel.setFont(font1)
        self.orginalDataLabel.setStyleSheet(u"color : rgb(71, 71, 71)")

        self.gridLayout.addWidget(self.orginalDataLabel, 0, 0, 1, 2)


        self.horizontalLayout.addLayout(self.gridLayout)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"\u55ae\u4f4d\u63db\u7b97\u6a5f", None))
#if QT_CONFIG(tooltip)
        self.InputLineEdit_1.setToolTip("")
#endif // QT_CONFIG(tooltip)
        self.InputLineEdit_1.setPlaceholderText(QCoreApplication.translate("Form", u"\u5728\u9019\u88e1\u8f38\u5165\u6578\u503c", None))
        self.transDataLabel.setText("")
        self.InputLineEdit_2.setPlaceholderText(QCoreApplication.translate("Form", u"\u9019\u88e1\u4e5f\u53ef\u4ee5\u8f38\u5165", None))
        self.orginalDataLabel.setText("")
    # retranslateUi

