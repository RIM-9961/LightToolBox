import requests
import base64
url="https://gitee.com/api/v5/repos/renjie-cn/light-tool-box/branches/main"
dm=requests.get(url).json()
print(dm["commit"]["commit"]["message"])