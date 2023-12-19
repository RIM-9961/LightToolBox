# -*- coding: utf-8 -*-

from PySide6 import QtCore, QtGui, QtWidgets

class Ui_cameraScreen(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("相机控制")
        MainWindow.resize(932, 651)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.graphicsView = QtWidgets.QGraphicsView(self.centralwidget)
        self.graphicsView.setGeometry(QtCore.QRect(10, 40, 683, 512))
        self.graphicsView.setDragMode(QtWidgets.QGraphicsView.ScrollHandDrag)
        self.graphicsView.setObjectName("graphicsView")
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(700, 0, 221, 171))
        self.groupBox.setObjectName("groupBox")
        self.comboBox_CameraList = QtWidgets.QComboBox(self.groupBox)
        self.comboBox_CameraList.setGeometry(QtCore.QRect(10, 70, 201, 31))
        self.comboBox_CameraList.setObjectName("comboBox_CameraList")
        self.pushButton_UpdateCameraList = QtWidgets.QPushButton(self.groupBox)
        self.pushButton_UpdateCameraList.setGeometry(QtCore.QRect(10, 30, 201, 31))
        self.pushButton_UpdateCameraList.setObjectName("pushButton_UpdateCameraList")
        self.pushButton_OpenCamera = QtWidgets.QPushButton(self.groupBox)
        self.pushButton_OpenCamera.setGeometry(QtCore.QRect(10, 110, 101, 28))
        self.pushButton_OpenCamera.setObjectName("pushButton_OpenCamera")
        self.pushButton_CloseCamera = QtWidgets.QPushButton(self.groupBox)
        self.pushButton_CloseCamera.setGeometry(QtCore.QRect(110, 110, 101, 28))
        self.pushButton_CloseCamera.setObjectName("pushButton_CloseCamera")
        self.pushButton_StartAcq = QtWidgets.QPushButton(self.groupBox)
        self.pushButton_StartAcq.setGeometry(QtCore.QRect(10, 140, 101, 28))
        self.pushButton_StartAcq.setObjectName("pushButton_StartAcq")
        self.pushButton_StopAcq = QtWidgets.QPushButton(self.groupBox)
        self.pushButton_StopAcq.setGeometry(QtCore.QRect(110, 140, 101, 28))
        self.pushButton_StopAcq.setObjectName("pushButton_StopAcq")
        self.pushButton_ZoomIn = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_ZoomIn.setGeometry(QtCore.QRect(510, 10, 92, 28))
        self.pushButton_ZoomIn.setObjectName("pushButton_ZoomIn")
        self.pushButton_ZoomOut = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_ZoomOut.setGeometry(QtCore.QRect(600, 10, 92, 28))
        self.pushButton_ZoomOut.setObjectName("pushButton_ZoomOut")
        self.groupBox_2 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_2.setGeometry(QtCore.QRect(700, 170, 221, 111))
        self.groupBox_2.setObjectName("groupBox_2")
        self.comboBox_ExposureMode = QtWidgets.QComboBox(self.groupBox_2)
        self.comboBox_ExposureMode.setGeometry(QtCore.QRect(120, 20, 91, 22))
        self.comboBox_ExposureMode.setObjectName("comboBox_ExposureMode")
        self.label = QtWidgets.QLabel(self.groupBox_2)
        self.label.setGeometry(QtCore.QRect(10, 20, 111, 21))
        self.label.setObjectName("label")
        self.comboBox_ExposureAuto = QtWidgets.QComboBox(self.groupBox_2)
        self.comboBox_ExposureAuto.setGeometry(QtCore.QRect(120, 50, 91, 22))
        self.comboBox_ExposureAuto.setObjectName("comboBox_ExposureAuto")
        self.label_2 = QtWidgets.QLabel(self.groupBox_2)
        self.label_2.setGeometry(QtCore.QRect(10, 50, 111, 21))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.groupBox_2)
        self.label_3.setGeometry(QtCore.QRect(10, 80, 111, 21))
        self.label_3.setObjectName("label_3")
        self.doubleSpinBox_ExposureTime = QtWidgets.QDoubleSpinBox(self.groupBox_2)
        self.doubleSpinBox_ExposureTime.setGeometry(QtCore.QRect(120, 80, 91, 22))
        self.doubleSpinBox_ExposureTime.setMaximum(99999999.99)
        self.doubleSpinBox_ExposureTime.setObjectName("doubleSpinBox_ExposureTime")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(10, 560, 72, 15))
        self.label_4.setObjectName("label_4")
        self.label_AcqNum = QtWidgets.QLabel(self.centralwidget)
        self.label_AcqNum.setGeometry(QtCore.QRect(80, 560, 72, 15))
        self.label_AcqNum.setObjectName("label_AcqNum")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(180, 560, 41, 16))
        self.label_5.setObjectName("label_5")
        self.label_FPS = QtWidgets.QLabel(self.centralwidget)
        self.label_FPS.setGeometry(QtCore.QRect(220, 560, 41, 16))
        self.label_FPS.setObjectName("label_FPS")
        self.groupBox_3 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_3.setGeometry(QtCore.QRect(700, 280, 221, 131))
        self.groupBox_3.setObjectName("groupBox_3")
        self.label_6 = QtWidgets.QLabel(self.groupBox_3)
        self.label_6.setGeometry(QtCore.QRect(10, 20, 111, 21))
        self.label_6.setObjectName("label_6")
        self.comboBox_TriggerMode = QtWidgets.QComboBox(self.groupBox_3)
        self.comboBox_TriggerMode.setGeometry(QtCore.QRect(120, 20, 91, 22))
        self.comboBox_TriggerMode.setObjectName("comboBox_TriggerMode")
        self.comboBox_TriggerSource = QtWidgets.QComboBox(self.groupBox_3)
        self.comboBox_TriggerSource.setGeometry(QtCore.QRect(120, 50, 91, 22))
        self.comboBox_TriggerSource.setObjectName("comboBox_TriggerSource")
        self.label_7 = QtWidgets.QLabel(self.groupBox_3)
        self.label_7.setGeometry(QtCore.QRect(10, 50, 111, 21))
        self.label_7.setObjectName("label_7")
        self.pushButton_SendSoftwareCommand = QtWidgets.QPushButton(self.groupBox_3)
        self.pushButton_SendSoftwareCommand.setGeometry(QtCore.QRect(10, 80, 201, 41))
        self.pushButton_SendSoftwareCommand.setObjectName("pushButton_SendSoftwareCommand")
        self.groupBox_4 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_4.setGeometry(QtCore.QRect(700, 410, 221, 81))
        self.groupBox_4.setObjectName("groupBox_4")
        self.label_8 = QtWidgets.QLabel(self.groupBox_4)
        self.label_8.setGeometry(QtCore.QRect(10, 20, 111, 21))
        self.label_8.setObjectName("label_8")
        self.comboBox_GainAuto = QtWidgets.QComboBox(self.groupBox_4)
        self.comboBox_GainAuto.setGeometry(QtCore.QRect(120, 20, 91, 22))
        self.comboBox_GainAuto.setObjectName("comboBox_GainAuto")
        self.doubleSpinBox_GainValue = QtWidgets.QDoubleSpinBox(self.groupBox_4)
        self.doubleSpinBox_GainValue.setGeometry(QtCore.QRect(120, 50, 91, 22))
        self.doubleSpinBox_GainValue.setMaximum(99999999.99)
        self.doubleSpinBox_GainValue.setObjectName("doubleSpinBox_GainValue")
        self.label_9 = QtWidgets.QLabel(self.groupBox_4)
        self.label_9.setGeometry(QtCore.QRect(10, 50, 111, 21))
        self.label_9.setObjectName("label_9")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(700, 490, 221, 61))
        self.pushButton.setObjectName("pushButton")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 932, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.pushButton.clicked.connect(MainWindow.close)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.groupBox.setTitle(_translate("MainWindow", "相机控制"))
        self.pushButton_UpdateCameraList.setText(_translate("MainWindow", "更新相机列表"))
        self.pushButton_OpenCamera.setText(_translate("MainWindow", "打开相机"))
        self.pushButton_CloseCamera.setText(_translate("MainWindow", "关闭相机"))
        self.pushButton_StartAcq.setText(_translate("MainWindow", "开始采集"))
        self.pushButton_StopAcq.setText(_translate("MainWindow", "停止采集"))
        self.pushButton_ZoomIn.setText(_translate("MainWindow", "放大"))
        self.pushButton_ZoomOut.setText(_translate("MainWindow", "缩小"))
        self.groupBox_2.setTitle(_translate("MainWindow", "曝光"))
        self.label.setText(_translate("MainWindow", "曝光模式:"))
        self.label_2.setText(_translate("MainWindow", "自动曝光:"))
        self.label_3.setText(_translate("MainWindow", "曝光时间:"))
        self.label_4.setText(_translate("MainWindow", "采集次数:"))
        self.label_AcqNum.setText(_translate("MainWindow", "0"))
        self.label_5.setText(_translate("MainWindow", "帧率:"))
        self.label_FPS.setText(_translate("MainWindow", "0"))
        self.groupBox_3.setTitle(_translate("MainWindow", "触发"))
        self.label_6.setText(_translate("MainWindow", "触发模式:"))
        self.label_7.setText(_translate("MainWindow", "触发源:"))
        self.pushButton_SendSoftwareCommand.setText(_translate("MainWindow", "发送软触发命令"))
        self.groupBox_4.setTitle(_translate("MainWindow", "增益"))
        self.label_8.setText(_translate("MainWindow", "自动增益:"))
        self.label_9.setText(_translate("MainWindow", "增益值:"))
        self.pushButton.setText(_translate("MainWindow", "关闭"))