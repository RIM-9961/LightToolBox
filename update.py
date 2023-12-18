import sys
import requests
import webbrowser
from modules import *
from widgets import *
now_version="v1.0.6\n"
def update():
    url="https://gitee.com/api/v5/repos/renjie-cn/light-tool-box/branches/main"
    dm=requests.get(url).json()
    return dm["commit"]["commit"]["message"]
class update_screen(QWidget):
    sendNoUpdateToMain=Signal(object)
    def __init__(self):
        super().__init__()
        self.ui = Ui_update()
        self.ui.setupUi(self)
        self.ui.offUpScreen.clicked.connect(self.openMainScreen)
        self.ui.download.clicked.connect(self.downLoadFromURL)
    def downLoadFromURL(self):
        webbrowser.open("https://gitee.com/renjie-cn/light-tool-box", new=0, autoraise=True) 
        self.close()
    def openMainScreen(self):
        self.close()

