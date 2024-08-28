# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'eKW_pobieracz.ui'
#
# Created by: PyQt5 UI code generator 5.15.11
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setEnabled(True)
        MainWindow.resize(328, 521)
        MainWindow.setMinimumSize(QtCore.QSize(328, 521))
        MainWindow.setMaximumSize(QtCore.QSize(16777215, 16777215))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("C:/Users/BG-P/.designer/backup/ico/eKW.jpg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setStyleSheet("")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_8 = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.lblBanner = QtWidgets.QLabel(self.centralwidget)
        self.lblBanner.setObjectName("lblBanner")
        self.verticalLayout_8.addWidget(self.lblBanner)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.lineSave = QtWidgets.QLineEdit(self.centralwidget)
        self.lineSave.setObjectName("lineSave")
        self.horizontalLayout_2.addWidget(self.lineSave)
        self.btnSave = QtWidgets.QPushButton(self.centralwidget)
        self.btnSave.setText("")
        self.btnSave.setObjectName("btnSave")
        self.horizontalLayout_2.addWidget(self.btnSave)
        self.verticalLayout_8.addLayout(self.horizontalLayout_2)
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setStyleSheet("")
        self.tabWidget.setObjectName("tabWidget")
        self.tab_Lister = QtWidgets.QWidget()
        self.tab_Lister.setObjectName("tab_Lister")
        self.verticalLayout_10 = QtWidgets.QVBoxLayout(self.tab_Lister)
        self.verticalLayout_10.setObjectName("verticalLayout_10")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.horizontalLayout.setSpacing(6)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.lineList = QtWidgets.QLineEdit(self.tab_Lister)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineList.sizePolicy().hasHeightForWidth())
        self.lineList.setSizePolicy(sizePolicy)
        self.lineList.setObjectName("lineList")
        self.horizontalLayout.addWidget(self.lineList)
        self.btnList = QtWidgets.QPushButton(self.tab_Lister)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btnList.sizePolicy().hasHeightForWidth())
        self.btnList.setSizePolicy(sizePolicy)
        self.btnList.setText("")
        self.btnList.setObjectName("btnList")
        self.horizontalLayout.addWidget(self.btnList)
        self.verticalLayout_10.addLayout(self.horizontalLayout)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        self.verticalLayout_10.addItem(spacerItem)
        self.btnRun = QtWidgets.QPushButton(self.tab_Lister)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btnRun.sizePolicy().hasHeightForWidth())
        self.btnRun.setSizePolicy(sizePolicy)
        self.btnRun.setAutoFillBackground(False)
        self.btnRun.setIconSize(QtCore.QSize(24, 24))
        self.btnRun.setFlat(False)
        self.btnRun.setObjectName("btnRun")
        self.verticalLayout_10.addWidget(self.btnRun)
        self.btnTurbo = QtWidgets.QPushButton(self.tab_Lister)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btnTurbo.sizePolicy().hasHeightForWidth())
        self.btnTurbo.setSizePolicy(sizePolicy)
        self.btnTurbo.setIconSize(QtCore.QSize(24, 24))
        self.btnTurbo.setFlat(False)
        self.btnTurbo.setObjectName("btnTurbo")
        self.verticalLayout_10.addWidget(self.btnTurbo)
        self.tabWidget.addTab(self.tab_Lister, "")
        self.tab_Generator = QtWidgets.QWidget()
        self.tab_Generator.setObjectName("tab_Generator")
        self.verticalLayout_11 = QtWidgets.QVBoxLayout(self.tab_Generator)
        self.verticalLayout_11.setObjectName("verticalLayout_11")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.lineSign = QtWidgets.QLineEdit(self.tab_Generator)
        self.lineSign.setMaxLength(4)
        self.lineSign.setObjectName("lineSign")
        self.verticalLayout_4.addWidget(self.lineSign)
        self.lineFloor = QtWidgets.QLineEdit(self.tab_Generator)
        self.lineFloor.setText("")
        self.lineFloor.setMaxLength(8)
        self.lineFloor.setObjectName("lineFloor")
        self.verticalLayout_4.addWidget(self.lineFloor)
        self.lineRoof = QtWidgets.QLineEdit(self.tab_Generator)
        self.lineRoof.setText("")
        self.lineRoof.setMaxLength(8)
        self.lineRoof.setFrame(True)
        self.lineRoof.setObjectName("lineRoof")
        self.verticalLayout_4.addWidget(self.lineRoof)
        self.verticalLayout_11.addLayout(self.verticalLayout_4)
        self.chParams = QtWidgets.QCheckBox(self.tab_Generator)
        self.chParams.setObjectName("chParams")
        self.verticalLayout_11.addWidget(self.chParams)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setContentsMargins(-1, 0, -1, -1)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.lineLast = QtWidgets.QLineEdit(self.tab_Generator)
        self.lineLast.setEnabled(False)
        self.lineLast.setMaxLength(1)
        self.lineLast.setObjectName("lineLast")
        self.horizontalLayout_5.addWidget(self.lineLast)
        self.lineControl = QtWidgets.QLineEdit(self.tab_Generator)
        self.lineControl.setEnabled(False)
        self.lineControl.setMaxLength(1)
        self.lineControl.setObjectName("lineControl")
        self.horizontalLayout_5.addWidget(self.lineControl)
        self.verticalLayout_11.addLayout(self.horizontalLayout_5)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_11.addItem(spacerItem1)
        self.btnGen = QtWidgets.QPushButton(self.tab_Generator)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btnGen.sizePolicy().hasHeightForWidth())
        self.btnGen.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.btnGen.setFont(font)
        self.btnGen.setObjectName("btnGen")
        self.verticalLayout_11.addWidget(self.btnGen)
        self.btnGenSave = QtWidgets.QPushButton(self.tab_Generator)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btnGenSave.sizePolicy().hasHeightForWidth())
        self.btnGenSave.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.btnGenSave.setFont(font)
        self.btnGenSave.setObjectName("btnGenSave")
        self.verticalLayout_11.addWidget(self.btnGenSave)
        self.btnGenSaveTurbo = QtWidgets.QPushButton(self.tab_Generator)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btnGenSaveTurbo.sizePolicy().hasHeightForWidth())
        self.btnGenSaveTurbo.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.btnGenSaveTurbo.setFont(font)
        self.btnGenSaveTurbo.setObjectName("btnGenSaveTurbo")
        self.verticalLayout_11.addWidget(self.btnGenSaveTurbo)
        self.tabWidget.addTab(self.tab_Generator, "")
        self.tab_Proxy = QtWidgets.QWidget()
        self.tab_Proxy.setObjectName("tab_Proxy")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.tab_Proxy)
        self.verticalLayout.setObjectName("verticalLayout")
        self.chProxy = QtWidgets.QCheckBox(self.tab_Proxy)
        self.chProxy.setObjectName("chProxy")
        self.verticalLayout.addWidget(self.chProxy)
        self.label_5 = QtWidgets.QLabel(self.tab_Proxy)
        self.label_5.setObjectName("label_5")
        self.verticalLayout.addWidget(self.label_5)
        self.lineProxy = QtWidgets.QLineEdit(self.tab_Proxy)
        self.lineProxy.setEnabled(False)
        self.lineProxy.setObjectName("lineProxy")
        self.verticalLayout.addWidget(self.lineProxy)
        spacerItem2 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem2)
        self.tabWidget.addTab(self.tab_Proxy, "")
        self.tab_Settings = QtWidgets.QWidget()
        self.tab_Settings.setObjectName("tab_Settings")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.tab_Settings)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.scrollArea = QtWidgets.QScrollArea(self.tab_Settings)
        self.scrollArea.setMinimumSize(QtCore.QSize(0, 215))
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 267, 620))
        self.scrollAreaWidgetContents.setMinimumSize(QtCore.QSize(0, 620))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.verticalLayout_12 = QtWidgets.QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_12.setObjectName("verticalLayout_12")
        self.label = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.verticalLayout_12.addWidget(self.label)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.horizontalSlider = QtWidgets.QSlider(self.scrollAreaWidgetContents)
        self.horizontalSlider.setMinimum(2)
        self.horizontalSlider.setMaximum(50)
        self.horizontalSlider.setSingleStep(1)
        self.horizontalSlider.setPageStep(5)
        self.horizontalSlider.setSliderPosition(5)
        self.horizontalSlider.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider.setInvertedAppearance(False)
        self.horizontalSlider.setInvertedControls(False)
        self.horizontalSlider.setTickPosition(QtWidgets.QSlider.TicksAbove)
        self.horizontalSlider.setTickInterval(5)
        self.horizontalSlider.setObjectName("horizontalSlider")
        self.horizontalLayout_3.addWidget(self.horizontalSlider)
        self.spN = QtWidgets.QSpinBox(self.scrollAreaWidgetContents)
        self.spN.setMinimum(2)
        self.spN.setMaximum(50)
        self.spN.setProperty("value", 5)
        self.spN.setObjectName("spN")
        self.horizontalLayout_3.addWidget(self.spN)
        self.verticalLayout_12.addLayout(self.horizontalLayout_3)
        self.label_3 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.verticalLayout_12.addWidget(self.label_3)
        self.verticalLayout_9 = QtWidgets.QVBoxLayout()
        self.verticalLayout_9.setObjectName("verticalLayout_9")
        self.chPDF = QtWidgets.QCheckBox(self.scrollAreaWidgetContents)
        self.chPDF.setMinimumSize(QtCore.QSize(0, 22))
        self.chPDF.setObjectName("chPDF")
        self.verticalLayout_9.addWidget(self.chPDF)
        self.chHTML = QtWidgets.QCheckBox(self.scrollAreaWidgetContents)
        self.chHTML.setMinimumSize(QtCore.QSize(0, 22))
        self.chHTML.setObjectName("chHTML")
        self.verticalLayout_9.addWidget(self.chHTML)
        self.chTXT = QtWidgets.QCheckBox(self.scrollAreaWidgetContents)
        self.chTXT.setMinimumSize(QtCore.QSize(0, 22))
        self.chTXT.setObjectName("chTXT")
        self.verticalLayout_9.addWidget(self.chTXT)
        self.chJSON = QtWidgets.QCheckBox(self.scrollAreaWidgetContents)
        self.chJSON.setMinimumSize(QtCore.QSize(0, 22))
        self.chJSON.setObjectName("chJSON")
        self.verticalLayout_9.addWidget(self.chJSON)
        self.chCSV = QtWidgets.QCheckBox(self.scrollAreaWidgetContents)
        self.chCSV.setMinimumSize(QtCore.QSize(0, 22))
        self.chCSV.setObjectName("chCSV")
        self.verticalLayout_9.addWidget(self.chCSV)
        self.chJSON1o = QtWidgets.QCheckBox(self.scrollAreaWidgetContents)
        self.chJSON1o.setMinimumSize(QtCore.QSize(0, 22))
        self.chJSON1o.setObjectName("chJSON1o")
        self.verticalLayout_9.addWidget(self.chJSON1o)
        self.chXlsx = QtWidgets.QCheckBox(self.scrollAreaWidgetContents)
        self.chXlsx.setEnabled(False)
        self.chXlsx.setMinimumSize(QtCore.QSize(0, 22))
        self.chXlsx.setObjectName("chXlsx")
        self.verticalLayout_9.addWidget(self.chXlsx)
        self.verticalLayout_12.addLayout(self.verticalLayout_9)
        self.label_4 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.verticalLayout_12.addWidget(self.label_4)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.chMerge = QtWidgets.QCheckBox(self.scrollAreaWidgetContents)
        self.chMerge.setMinimumSize(QtCore.QSize(0, 38))
        self.chMerge.setCheckable(True)
        self.chMerge.setChecked(True)
        self.chMerge.setObjectName("chMerge")
        self.verticalLayout_3.addWidget(self.chMerge)
        self.chError = QtWidgets.QCheckBox(self.scrollAreaWidgetContents)
        self.chError.setMinimumSize(QtCore.QSize(0, 38))
        self.chError.setChecked(True)
        self.chError.setObjectName("chError")
        self.verticalLayout_3.addWidget(self.chError)
        self.chImg = QtWidgets.QCheckBox(self.scrollAreaWidgetContents)
        self.chImg.setMinimumSize(QtCore.QSize(0, 38))
        self.chImg.setChecked(True)
        self.chImg.setObjectName("chImg")
        self.verticalLayout_3.addWidget(self.chImg)
        self.chSkip = QtWidgets.QCheckBox(self.scrollAreaWidgetContents)
        self.chSkip.setMinimumSize(QtCore.QSize(0, 38))
        self.chSkip.setObjectName("chSkip")
        self.verticalLayout_3.addWidget(self.chSkip)
        self.chBg = QtWidgets.QCheckBox(self.scrollAreaWidgetContents)
        self.chBg.setMinimumSize(QtCore.QSize(0, 22))
        self.chBg.setObjectName("chBg")
        self.verticalLayout_3.addWidget(self.chBg)
        self.verticalLayout_12.addLayout(self.verticalLayout_3)
        self.label_2 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.verticalLayout_12.addWidget(self.label_2)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.ch1o = QtWidgets.QCheckBox(self.scrollAreaWidgetContents)
        self.ch1o.setMinimumSize(QtCore.QSize(0, 22))
        self.ch1o.setChecked(True)
        self.ch1o.setObjectName("ch1o")
        self.verticalLayout_2.addWidget(self.ch1o)
        self.ch1s = QtWidgets.QCheckBox(self.scrollAreaWidgetContents)
        self.ch1s.setMinimumSize(QtCore.QSize(0, 22))
        self.ch1s.setChecked(False)
        self.ch1s.setObjectName("ch1s")
        self.verticalLayout_2.addWidget(self.ch1s)
        self.ch2 = QtWidgets.QCheckBox(self.scrollAreaWidgetContents)
        self.ch2.setMinimumSize(QtCore.QSize(0, 22))
        self.ch2.setChecked(True)
        self.ch2.setObjectName("ch2")
        self.verticalLayout_2.addWidget(self.ch2)
        self.ch3 = QtWidgets.QCheckBox(self.scrollAreaWidgetContents)
        self.ch3.setMinimumSize(QtCore.QSize(0, 22))
        self.ch3.setChecked(True)
        self.ch3.setObjectName("ch3")
        self.verticalLayout_2.addWidget(self.ch3)
        self.ch4 = QtWidgets.QCheckBox(self.scrollAreaWidgetContents)
        self.ch4.setMinimumSize(QtCore.QSize(0, 22))
        self.ch4.setObjectName("ch4")
        self.verticalLayout_2.addWidget(self.ch4)
        self.verticalLayout_12.addLayout(self.verticalLayout_2)
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setContentsMargins(-1, 0, -1, -1)
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.lblBrowser = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.lblBrowser.setFont(font)
        self.lblBrowser.setObjectName("lblBrowser")
        self.horizontalLayout_7.addWidget(self.lblBrowser)
        self.cbBrowser = QtWidgets.QComboBox(self.scrollAreaWidgetContents)
        self.cbBrowser.setEditable(False)
        self.cbBrowser.setObjectName("cbBrowser")
        self.cbBrowser.addItem("")
        self.cbBrowser.addItem("")
        self.cbBrowser.addItem("")
        self.cbBrowser.setItemText(2, "firefox (test)")
        self.horizontalLayout_7.addWidget(self.cbBrowser)
        self.verticalLayout_12.addLayout(self.horizontalLayout_7)
        self.lblDzList = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.lblDzList.setFont(font)
        self.lblDzList.setObjectName("lblDzList")
        self.verticalLayout_12.addWidget(self.lblDzList)
        self.chDzList = QtWidgets.QCheckBox(self.scrollAreaWidgetContents)
        self.chDzList.setObjectName("chDzList")
        self.verticalLayout_12.addWidget(self.chDzList)
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_8.setContentsMargins(-1, 0, -1, -1)
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.lineDzList = QtWidgets.QLineEdit(self.scrollAreaWidgetContents)
        self.lineDzList.setEnabled(False)
        self.lineDzList.setReadOnly(True)
        self.lineDzList.setObjectName("lineDzList")
        self.horizontalLayout_8.addWidget(self.lineDzList)
        self.btnOpenDzList = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        self.btnOpenDzList.setEnabled(False)
        self.btnOpenDzList.setObjectName("btnOpenDzList")
        self.horizontalLayout_8.addWidget(self.btnOpenDzList)
        self.verticalLayout_12.addLayout(self.horizontalLayout_8)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.btnLog = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        self.btnLog.setObjectName("btnLog")
        self.horizontalLayout_4.addWidget(self.btnLog)
        self.btnErr = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        self.btnErr.setObjectName("btnErr")
        self.horizontalLayout_4.addWidget(self.btnErr)
        self.verticalLayout_12.addLayout(self.horizontalLayout_4)
        self.chTheme = QtWidgets.QCheckBox(self.scrollAreaWidgetContents)
        self.chTheme.setObjectName("chTheme")
        self.verticalLayout_12.addWidget(self.chTheme)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.verticalLayout_6.addWidget(self.scrollArea)
        self.tabWidget.addTab(self.tab_Settings, "")
        self.tab_Info = QtWidgets.QWidget()
        self.tab_Info.setObjectName("tab_Info")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.tab_Info)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.btn_Github = QtWidgets.QPushButton(self.tab_Info)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_Github.sizePolicy().hasHeightForWidth())
        self.btn_Github.setSizePolicy(sizePolicy)
        self.btn_Github.setObjectName("btn_Github")
        self.verticalLayout_5.addWidget(self.btn_Github)
        self.btn_Instrukcja = QtWidgets.QPushButton(self.tab_Info)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_Instrukcja.sizePolicy().hasHeightForWidth())
        self.btn_Instrukcja.setSizePolicy(sizePolicy)
        self.btn_Instrukcja.setObjectName("btn_Instrukcja")
        self.verticalLayout_5.addWidget(self.btn_Instrukcja)
        spacerItem3 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_5.addItem(spacerItem3)
        self.btn_Coffe = QtWidgets.QPushButton(self.tab_Info)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_Coffe.sizePolicy().hasHeightForWidth())
        self.btn_Coffe.setSizePolicy(sizePolicy)
        self.btn_Coffe.setObjectName("btn_Coffe")
        self.verticalLayout_5.addWidget(self.btn_Coffe)
        self.tabWidget.addTab(self.tab_Info, "")
        self.verticalLayout_8.addWidget(self.tabWidget)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.progressBar = QtWidgets.QProgressBar(self.centralwidget)
        self.progressBar.setProperty("value", 0)
        self.progressBar.setObjectName("progressBar")
        self.horizontalLayout_6.addWidget(self.progressBar)
        self.btnPause = QtWidgets.QPushButton(self.centralwidget)
        self.btnPause.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/icons/res/pause.jpg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnPause.setIcon(icon1)
        self.btnPause.setIconSize(QtCore.QSize(24, 24))
        self.btnPause.setFlat(True)
        self.btnPause.setObjectName("btnPause")
        self.horizontalLayout_6.addWidget(self.btnPause)
        self.btnStop = QtWidgets.QPushButton(self.centralwidget)
        self.btnStop.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/icons/res/stop.jpg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnStop.setIcon(icon2)
        self.btnStop.setIconSize(QtCore.QSize(24, 24))
        self.btnStop.setFlat(True)
        self.btnStop.setObjectName("btnStop")
        self.horizontalLayout_6.addWidget(self.btnStop)
        self.verticalLayout_8.addLayout(self.horizontalLayout_6)
        self.lblStatus = QtWidgets.QLabel(self.centralwidget)
        self.lblStatus.setText("")
        self.lblStatus.setObjectName("lblStatus")
        self.verticalLayout_8.addWidget(self.lblStatus)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 328, 21))
        self.menubar.setObjectName("menubar")
        self.menu_O_programie = QtWidgets.QMenu(self.menubar)
        self.menu_O_programie.setObjectName("menu_O_programie")
        self.menu_Muzyka = QtWidgets.QMenu(self.menubar)
        self.menu_Muzyka.setObjectName("menu_Muzyka")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.action_Wsparcie = QtWidgets.QAction(MainWindow)
        self.action_Wsparcie.setObjectName("action_Wsparcie")
        self.action_github = QtWidgets.QAction(MainWindow)
        self.action_github.setObjectName("action_github")
        self.action_Instrukcja = QtWidgets.QAction(MainWindow)
        self.action_Instrukcja.setObjectName("action_Instrukcja")
        self.action_muzyka = QtWidgets.QAction(MainWindow)
        self.action_muzyka.setObjectName("action_muzyka")
        self.menu_O_programie.addAction(self.action_Wsparcie)
        self.menu_O_programie.addAction(self.action_github)
        self.menu_O_programie.addAction(self.action_Instrukcja)
        self.menu_Muzyka.addAction(self.action_muzyka)
        self.menubar.addAction(self.menu_O_programie.menuAction())
        self.menubar.addAction(self.menu_Muzyka.menuAction())

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        self.horizontalSlider.valueChanged['int'].connect(self.spN.setValue) # type: ignore
        self.spN.valueChanged['int'].connect(self.horizontalSlider.setValue) # type: ignore
        self.chProxy.toggled['bool'].connect(self.lineProxy.setEnabled) # type: ignore
        self.chJSON1o.toggled['bool'].connect(self.chXlsx.setEnabled) # type: ignore
        self.chDzList.clicked['bool'].connect(self.lineDzList.setEnabled) # type: ignore
        self.chDzList.clicked['bool'].connect(self.btnOpenDzList.setEnabled) # type: ignore
        self.chParams.clicked['bool'].connect(self.lineLast.setEnabled) # type: ignore
        self.chParams.clicked['bool'].connect(self.lineControl.setEnabled) # type: ignore
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "eKW pobieraczek 1.2"))
        self.lblBanner.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><img src=\":/baner/res/baner_310x60.jpg\"/></p></body></html>"))
        self.lineSave.setToolTip(_translate("MainWindow", "<html><head/><body><p>folder zapisu ksiąg</p></body></html>"))
        self.lineSave.setPlaceholderText(_translate("MainWindow", "folder zapisu ksiąg"))
        self.btnSave.setToolTip(_translate("MainWindow", "<html><head/><body><p>Wybór folderu do zapisu pobieranych ksiąg wieczystych</p></body></html>"))
        self.lineList.setToolTip(_translate("MainWindow", "<html><head/><body><p>ścieżka do listy z KW</p></body></html>"))
        self.lineList.setPlaceholderText(_translate("MainWindow", "ścieżka do listy z KW"))
        self.btnList.setToolTip(_translate("MainWindow", "<html><head/><body><p>Ścieżka do pliku tekstowego z listą oznaczeń ksiąg wieczystych.</p></body></html>"))
        self.btnRun.setToolTip(_translate("MainWindow", "<html><head/><body><p>Rozpocznij pobieranie ksiąg z listy z pliku txt.</p></body></html>"))
        self.btnRun.setText(_translate("MainWindow", "Pobierz pojedynczo"))
        self.btnTurbo.setText(_translate("MainWindow", "Pobierz Turbo !!! OSTROŻNIE !!!"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_Lister), _translate("MainWindow", "Lista"))
        self.lineSign.setToolTip(_translate("MainWindow", "<html><head/><body><p>Kod sądu np. BB1B</p></body></html>"))
        self.lineSign.setPlaceholderText(_translate("MainWindow", "Kod sądu np. BB1B"))
        self.lineFloor.setToolTip(_translate("MainWindow", "<html><head/><body><p>numer początkowy np. 1</p></body></html>"))
        self.lineFloor.setPlaceholderText(_translate("MainWindow", "numer początkowy np. 1"))
        self.lineRoof.setToolTip(_translate("MainWindow", "<html><head/><body><p>numer końcowy np. 99999999</p></body></html>"))
        self.lineRoof.setPlaceholderText(_translate("MainWindow", "numer końcowy np. 99999999"))
        self.chParams.setText(_translate("MainWindow", "Parametry"))
        self.lineLast.setPlaceholderText(_translate("MainWindow", "Ostatnia cyfra numeru"))
        self.lineControl.setPlaceholderText(_translate("MainWindow", "Cyfra kontrolna"))
        self.btnGen.setToolTip(_translate("MainWindow", "<html><head/><body><p>Generuj listę z potencjalnymi numerami ksiąg wieczystych z danego zakresu i zapisz do pliku txt.</p></body></html>"))
        self.btnGen.setText(_translate("MainWindow", "Generuj listę"))
        self.btnGenSave.setToolTip(_translate("MainWindow", "<html><head/><body><p>Rozpocznij pobieranie ksiąg z wskazanego zakresu.</p></body></html>"))
        self.btnGenSave.setText(_translate("MainWindow", "Pobierz z zakresu"))
        self.btnGenSaveTurbo.setText(_translate("MainWindow", "Turbo Pobierz z zakresu"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_Generator), _translate("MainWindow", "Generator"))
        self.chProxy.setText(_translate("MainWindow", "proxy"))
        self.label_5.setText(_translate("MainWindow", "<html><head/><body><p>PROXY IP:</p></body></html>"))
        self.lineProxy.setPlaceholderText(_translate("MainWindow", "149.215.113.110:70"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_Proxy), _translate("MainWindow", "Proxy"))
        self.label.setText(_translate("MainWindow", "Liczba operacji w tym samym czasie"))
        self.label_3.setText(_translate("MainWindow", "Formaty pobieranych plików"))
        self.chPDF.setText(_translate("MainWindow", "PDF (nie dla firefox)"))
        self.chHTML.setText(_translate("MainWindow", "HTML"))
        self.chTXT.setText(_translate("MainWindow", "TXT"))
        self.chJSON.setText(_translate("MainWindow", "JSON (wyszukiwanie)"))
        self.chCSV.setText(_translate("MainWindow", "CSV (jeden plik dla całego pobierania)"))
        self.chJSON1o.setText(_translate("MainWindow", "JSON (DZIAŁ I-O)"))
        self.chXlsx.setText(_translate("MainWindow", "XLSX (DZIAŁ I-O)"))
        self.label_4.setText(_translate("MainWindow", "Ogólne działanie programu"))
        self.chMerge.setText(_translate("MainWindow", "Złącz działy w jeden pdf"))
        self.chError.setText(_translate("MainWindow", "Gdy brak aktualnej pobieraj zupełną"))
        self.chImg.setToolTip(_translate("MainWindow", "<html><head/><body><p>Włącz lub wyłącz ładowanie grafik na stronie (może zmniejszyć zużycie ramu)</p></body></html>"))
        self.chImg.setText(_translate("MainWindow", "ładowanie grafik strony"))
        self.chSkip.setText(_translate("MainWindow", "Pomijaj już pobrane"))
        self.chBg.setText(_translate("MainWindow", "Zachować tło strony"))
        self.label_2.setText(_translate("MainWindow", "Działy KW do pobrania"))
        self.ch1o.setText(_translate("MainWindow", "Dział I-O"))
        self.ch1s.setText(_translate("MainWindow", "Dział I-SP"))
        self.ch2.setText(_translate("MainWindow", "Dział II"))
        self.ch3.setText(_translate("MainWindow", "Dział III"))
        self.ch4.setText(_translate("MainWindow", "Dział IV"))
        self.lblBrowser.setText(_translate("MainWindow", "Domyślna przeglądarka"))
        self.cbBrowser.setItemText(0, _translate("MainWindow", "chrome"))
        self.cbBrowser.setItemText(1, _translate("MainWindow", "edge"))
        self.lblDzList.setText(_translate("MainWindow", "Pobieranie KW jeżeli..."))
        self.chDzList.setText(_translate("MainWindow", "Pobieraj KW jeżeli nr dz na liście"))
        self.btnOpenDzList.setText(_translate("MainWindow", "lista nr dz"))
        self.btnLog.setToolTip(_translate("MainWindow", "<html><head/><body><p>Otwórz plik z zapisanymi logami z ostatniej operacji.</p></body></html>"))
        self.btnLog.setText(_translate("MainWindow", "Logi"))
        self.btnErr.setToolTip(_translate("MainWindow", "<html><head/><body><p>Otwórz plik z odnotowanymi błędami działania programu lub wsadu do programu.</p></body></html>"))
        self.btnErr.setText(_translate("MainWindow", "Błędy"))
        self.chTheme.setText(_translate("MainWindow", "Jasny motyw wymagany restart programu"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_Settings), _translate("MainWindow", "Ustawienia"))
        self.btn_Github.setText(_translate("MainWindow", "GITHUB"))
        self.btn_Instrukcja.setText(_translate("MainWindow", "Otwórz plik pomocy (PDF)"))
        self.btn_Coffe.setText(_translate("MainWindow", "Postaw mi kawę"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_Info), _translate("MainWindow", "*"))
        self.btnPause.setToolTip(_translate("MainWindow", "Wstrzymaj lub wznów bierzącą operacje"))
        self.btnStop.setToolTip(_translate("MainWindow", "Zatrzymanie bierzącej operacji. Opreacja dokończy ostanią pętle i się zatrzyma."))
        self.menu_O_programie.setTitle(_translate("MainWindow", "&O programie"))
        self.menu_Muzyka.setTitle(_translate("MainWindow", "&Muzyka"))
        self.action_Wsparcie.setText(_translate("MainWindow", "&Postaw mi kawę"))
        self.action_github.setText(_translate("MainWindow", "&Github"))
        self.action_Instrukcja.setText(_translate("MainWindow", "&Instrukcja"))
        self.action_muzyka.setText(_translate("MainWindow", "&włącz/wyłącz"))
import res_rc
