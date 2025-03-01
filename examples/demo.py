import os
import sys

# 添加父目录到 Python 路径
# current_dir = os.path.dirname(os.path.abspath(__file__))
# parent_dir = os.path.dirname(current_dir)
# if parent_dir not in sys.path:
#     sys.path.append(parent_dir)

from wxauto.wxauto import WeChat
import time
# 获取微信窗口对象
wx = WeChat()
# 输出 > 初始化成功，获取到已登录窗口：xxxx
msg = '你好~~'
who = '群备注'
# at = ['备注']
res = wx.SendMsg(msg, who)  # 向`文件传输助手`发送消息：你好~
print(res)
