# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'update.ui'
##
## Created by: Qt User Interface Compiler version 6.6.0
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
from PySide6.QtWidgets import (QApplication, QFrame, QHBoxLayout, QLabel,
    QPushButton, QScrollArea, QSizePolicy, QVBoxLayout,
    QWidget)

class Ui_update(object):
    def setupUi(self, update):
        if not update.objectName():
            update.setObjectName(u"update")
        update.resize(400, 300)
        update.setCursor(QCursor(Qt.IBeamCursor))
        self.verticalLayout_2 = QVBoxLayout(update)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.frame = QFrame(update)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.frame)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.scrollArea = QScrollArea(self.frame)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setVerticalScrollBarPolicy(Qt.ScrollBarAsNeeded)
        self.scrollArea.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 360, 228))
        self.horizontalLayout_2 = QHBoxLayout(self.scrollAreaWidgetContents)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label = QLabel(self.scrollAreaWidgetContents)
        self.label.setObjectName(u"label")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setMinimumSize(QSize(0, 0))
        self.label.setMaximumSize(QSize(16777215, 16777215))
        font = QFont()
        font.setFamilies([u"\u9ed1\u4f53"])
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setKerning(True)
        self.label.setFont(font)
        self.label.setCursor(QCursor(Qt.IBeamCursor))
        self.label.setTabletTracking(False)
        self.label.setTextFormat(Qt.AutoText)
        self.label.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)
        self.label.setWordWrap(True)
        self.label.setMargin(0)
        self.label.setIndent(-1)
        self.label.setOpenExternalLinks(False)
        self.label.setTextInteractionFlags(Qt.LinksAccessibleByMouse|Qt.TextSelectableByKeyboard|Qt.TextSelectableByMouse)

        self.horizontalLayout_2.addWidget(self.label)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.verticalLayout.addWidget(self.scrollArea)


        self.verticalLayout_2.addWidget(self.frame)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.download = QPushButton(update)
        self.download.setObjectName(u"download")

        self.horizontalLayout.addWidget(self.download)

        self.offUpScreen = QPushButton(update)
        self.offUpScreen.setObjectName(u"offUpScreen")

        self.horizontalLayout.addWidget(self.offUpScreen)


        self.verticalLayout_2.addLayout(self.horizontalLayout)


        self.retranslateUi(update)

        QMetaObject.connectSlotsByName(update)
    # setupUi

    def retranslateUi(self, update):
        update.setWindowTitle(QCoreApplication.translate("update", u"Form", None))
        self.label.setText(QCoreApplication.translate("update", u"\u7c97\u73b0\u95ee\u9898\u4e86", None))
        self.download.setText(QCoreApplication.translate("update", u"\u524d\u5f80\u4e0b\u8f7d", None))
        self.offUpScreen.setText(QCoreApplication.translate("update", u"\u4e0b\u6b21\u4e00\u5b9a", None))
    # retranslateUi

