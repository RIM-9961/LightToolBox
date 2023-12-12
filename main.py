import sys
import os
import platform
from modules import *
from widgets import *
os.environ["QT_FONT_DPI"] = "96" # FIX Problem for High DPI and Scale above 100%

# SET AS GLOBAL widgets
#-------------------------------------------------------------
widgets = None

class MainWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        screen = QGuiApplication.primaryScreen().geometry()  # 获取屏幕类并调用geometry()方法获取屏幕大小
        width = screen.width()  # 获取屏幕的宽
        height = screen.height()  # 获取屏幕的高
        # SET AS GLOBAL widgets
        #-------------------------------------------------------------
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        global widgets
        widgets = self.ui 
        # USE CUSTOM TITLE BAR | USE AS "False" FOR MAC OR LINUX
        #-------------------------------------------------------------
        Settings.ENABLE_CUSTOM_TITLE_BAR = True
        title = "光刃工具箱"
        description = "光刃工具箱"
        #屏幕大小自适应
        polynum=20#子控件跟mainwindow的大小比例
        self.resize(width*0.7,height*0.7)
        widgets.leftMenuBg.setMinimumSize(QSize(height/polynum,0))
        widgets.topLogoInfo.setMinimumSize(QSize(0,height/polynum))
        # APPLY TEXTS
        self.setWindowTitle(title)
        widgets.titleRightInfo.setText(description)
        widgets.toggleButton.clicked.connect(lambda: UIFunctions.toggleMenu(self, True))
        # SET UI DEFINITIONS
        #-------------------------------------------------------------
        UIFunctions.uiDefinitions(self)
        # QTableWidget PARAMETERS
        #-------------------------------------------------------------
        widgets.tableWidget.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        # BUTTONS CLICK
        #-------------------------------------------------------------
        # LEFT MENUS
        widgets.btn_home.clicked.connect(self.buttonClick)
        widgets.btn_widgets.clicked.connect(self.buttonClick)
        widgets.btn_new.clicked.connect(self.buttonClick)
        widgets.btn_save.clicked.connect(self.buttonClick)
        # EXTRA LEFT BOX
        def openCloseLeftBox():
            UIFunctions.toggleLeftBox(self, True)
        widgets.toggleLeftBox.clicked.connect(openCloseLeftBox)
        widgets.extraCloseColumnBtn.clicked.connect(openCloseLeftBox)
        # EXTRA RIGHT BOX
        def openCloseRightBox():
            UIFunctions.toggleRightBox(self, True)
        widgets.settingsTopBtn.clicked.connect(openCloseRightBox)
        # SHOW APP
        #-------------------------------------------------------------
        self.show()
        # SET CUSTOM THEME
        #-------------------------------------------------------------
        useCustomTheme = True
        themeFile = "themes\py_dracula_light.qss"
        # SET THEME AND HACKS
        if useCustomTheme:
            # LOAD AND APPLY STYLE
            UIFunctions.theme(self, themeFile, True)
            # SET HACKS
            AppFunctions.setThemeHack(self)
        # SET HOME PAGE AND SELECT MENU
        #-------------------------------------------------------------
        widgets.stackedWidget.setCurrentWidget(widgets.home)
        widgets.btn_home.setStyleSheet(UIFunctions.selectMenu(widgets.btn_home.styleSheet()))
    # BUTTONS CLICK
    # Post here your functions for clicked buttons
    #-------------------------------------------------------------
    def buttonClick(self):
        # GET BUTTON CLICKED
        btn = self.sender()
        btnName = btn.objectName()
        # SHOW HOME PAGE
        if btnName == "btn_home":
            widgets.stackedWidget.setCurrentWidget(widgets.home)
            UIFunctions.resetStyle(self, btnName)
            btn.setStyleSheet(UIFunctions.selectMenu(btn.styleSheet()))
        # SHOW widgets PAGE
        if btnName == "btn_widgets":
            widgets.stackedWidget.setCurrentWidget(widgets.widgets)
            UIFunctions.resetStyle(self, btnName)
            btn.setStyleSheet(UIFunctions.selectMenu(btn.styleSheet()))
        # SHOW NEW PAGE
        if btnName == "btn_new":
            widgets.stackedWidget.setCurrentWidget(widgets.new_page) # SET PAGE
            UIFunctions.resetStyle(self, btnName) # RESET ANOTHERS BUTTONS SELECTED
            btn.setStyleSheet(UIFunctions.selectMenu(btn.styleSheet())) # SELECT MENU
        if btnName == "btn_save":
            print("Save BTN clicked!")
        # PRINT BTN NAME
        print(f'Button "{btnName}" pressed!')
    # RESIZE EVENTS
    #-------------------------------------------------------------
    def resizeEvent(self, event):
        # Update Size Grips
        UIFunctions.resize_grips(self)
    # MOUSE CLICK EVENTS
    #-------------------------------------------------------------
    def mousePressEvent(self, event):
        # SET DRAG POS WINDOW
        self.dragPos = event.globalPos()
        # PRINT MOUSE EVENTS
        if event.buttons() == Qt.LeftButton:
            print('Mouse click: LEFT CLICK')
        if event.buttons() == Qt.RightButton:
            print('Mouse click: RIGHT CLICK')
if __name__ == "__main__":
    QApplication.setHighDpiScaleFactorRoundingPolicy(Qt.HighDpiScaleFactorRoundingPolicy.PassThrough)
    app = QApplication(sys.argv)
    app.setWindowIcon(QIcon("icon.ico"))
    window = MainWindow()
    sys.exit(app.exec())
