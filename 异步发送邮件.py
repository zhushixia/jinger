import datetime
import os
from multiprocessing import Process
from threading import Thread

import win32api
import win32com.client as win32
import win32con
import win32gui
import win32ui
from flask import current_app, render_template
from flask_mail import Message
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
        send_mail()
        return "ok"

def send_async_email():
    outlook = win32.Dispatch('Outlook.Application')
    send_account = None
    for account in outlook.Session.Accounts:
        print(account)
    reciList = ['15868407338@163.com']
    for i in range(len(reciList)):
        mail_item = outlook.CreateItem(0)  # 0: olMailItem
        mail_item.Recipients.Add(reciList[i])
        mail_item.Subject = 'Mail Test'
        mail_item.BodyFormat = 2  # 2: Html format
        mail_item.Attachments.Add('F:\\test\\3.png')
        mail_item.HTMLBody = "<div><img src='3.png' /></div>"
        mail_item.Send()


def send_mail(**kwargs):
    thr = Process(target=send_async_email)
    thr.start()
    return thr








