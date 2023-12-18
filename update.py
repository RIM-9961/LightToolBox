import sys
import git
import requests
import webbrowser
from modules import *
from widgets import *
now_version="v1.0.6"
url="https://gitee.com/api/v5/repos/renjie-cn/light-tool-box/releases/latest?access_token=8860ce06ddd4306142dcc5692152f5a5"
def update():
    dm=requests.get(url).json()
    return dm["tag_name"]
class update_screen(QWidget):
    sendNoUpdateToMain=Signal(object)
    def __init__(self):
        super().__init__()
        bb=requests.get(url).json()
        self.ui = Ui_update()
        self.ui.setupUi(self)
        self.ui.offUpScreen.clicked.connect(self.openMainScreen)
        self.ui.download.clicked.connect(self.downLoadFromURL)
        self.ui.label.setText("发现新版本\n当前版本为:"+now_version+"\n最新版版本为"+bb["tag_name"]+"\n更新内容为:\n"+bb["body"])
    def downLoadFromURL(self):
        webbrowser.open("https://gitee.com/renjie-cn/light-tool-box", new=0, autoraise=True) 
        self.close()
    def openMainScreen(self):
        self.close()

