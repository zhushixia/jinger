import datetime
import os

import win32api
import win32com.client as win32
import win32con
import win32gui
import win32ui
from flask_restplus import Namespace, Resource, abort

from info.modules.index.test import test
import time

apitest = Namespace("users", description="Users CURD api.")
# todo = api.model('Todo', {
#     'id': fields.Integer(readonly=True, description='The task unique identifier'),
#     'task': fields.String(required=True, description='The task details')
# })
# ns = api.namespace('todos', description='TODO operations', path="/api")

@apitest.route('/get')
class Zhushi(Resource):

    def get(self):
        file = datetime.datetime.strftime(datetime.datetime.now(), "%Y%m%d")
        path = "F:\\test\\info\\images" + os.sep + file + '.jpg'
        print(path)
        self.window_capture(path)
        self.send_mail(path)

    def send_mail(self, path):
        sub = 'outlook python mail test'
        outlook = win32.Dispatch('outlook.application')
        receivers = ['xxx']
        mail = outlook.CreateItem(0)
        mail.To = receivers[0]
        mail.Subject = sub
        mail.BodyFormat = 2
        mail.Attachments.Add(path)  # 先把要插入的图片当作一个附件添加
        # mail.Attachments.Add(r'd:\1\bj.xlsx')  # 添加正常的附件
        mail.HtmlBody = "<div><img src='{}' /></div>".format(path)
        mail.display()

    def window_capture(self, filename):
        hwnd = 0  # 窗口的编号，0号表示当前活跃窗口
        # 根据窗口句柄获取窗口的设备上下文DC（Divice Context）
        hwndDC = win32gui.GetWindowDC(hwnd)
        # 根据窗口的DC获取mfcDC
        mfcDC = win32ui.CreateDCFromHandle(hwndDC)
        # mfcDC创建可兼容的DC
        saveDC = mfcDC.CreateCompatibleDC()
        # 创建bigmap准备保存图片
        saveBitMap = win32ui.CreateBitmap()
        # 获取监控器信息
        MoniterDev = win32api.EnumDisplayMonitors(None, None)
        w = MoniterDev[0][2][2]
        h = MoniterDev[0][2][3]
        # print w,h　　　#图片大小
        # 为bitmap开辟空间
        saveBitMap.CreateCompatibleBitmap(mfcDC, w, h)
        # 高度saveDC，将截图保存到saveBitmap中
        saveDC.SelectObject(saveBitMap)
        # 截取从左上角（0，0）长宽为（w，h）的图片
        saveDC.BitBlt((0, 0), (w, h), mfcDC, (0, 0), win32con.SRCCOPY)
        saveBitMap.SaveBitmapFile(saveDC, filename)








