# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'SharingDialog.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *


class Ui_SharingDialog(object):
    def setupUi(self, SharingDialog):
        if not SharingDialog.objectName():
            SharingDialog.setObjectName(u"SharingDialog")
        SharingDialog.resize(400, 300)
        SharingDialog.setSizeGripEnabled(False)
        self.stopSharing = QPushButton(SharingDialog)
        self.stopSharing.setObjectName(u"stopSharing")
        self.stopSharing.setGeometry(QRect(150, 230, 101, 31))
        self.linkLabel = QLabel(SharingDialog)
        self.linkLabel.setObjectName(u"linkLabel")
        self.linkLabel.setGeometry(QRect(70, 80, 261, 91))
        self.linkLabel.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.linkLabel.setTextInteractionFlags(Qt.LinksAccessibleByMouse|Qt.TextSelectableByKeyboard|Qt.TextSelectableByMouse)

        self.retranslateUi(SharingDialog)

        QMetaObject.connectSlotsByName(SharingDialog)
    # setupUi

    def retranslateUi(self, SharingDialog):
        SharingDialog.setWindowTitle(QCoreApplication.translate("SharingDialog", u"Dialog", None))
        self.stopSharing.setText(QCoreApplication.translate("SharingDialog", u"Stop Sharing", None))
        self.linkLabel.setText(QCoreApplication.translate("SharingDialog", u"TextLabel", None))
    # retranslateUi

