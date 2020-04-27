# coding:utf8
from time import sleep
from selenium import webdriver
import json


class Hiblog(object):
    def __init__(self, url1):
        self.url = url1

    def screen_shot(self):
        driver = webdriver.PhantomJS(executable_path=r'F:\phantomjs-2.1.1-windows\bin\phantomjs.exe')
        driver.get(self.url)
        # driver.find_element_by_name("username").send_keys("admin")
        # driver.find_element_by_name("password").send_keys("admin")
        # driver.find_element_by_xpath("//button[@type='submit']").click()
        # driver.viewportSize = {'width': 1024, 'height': 800}
        driver.maximize_window()
        driver.save_screenshot('test.png')
        print(driver.title)


if __name__ == "__main__":
    url = "https://www.baidu.com/s?wd=phantomjs%E4%B8%8B%E8%BD%BD&rsv_spt=1&rsv_iqid=0xdc8812740016b799&issp=1&f=3&rsv_bp=1&rsv_idx=2&ie=utf-8&rqlang=cn&tn=baiduhome_pg&rsv_enter=0&rsv_dl=ts_1&oq=phantomjs%25E4%25B8%258B%25E8%25BD%25BD&rsv_t=fab3hkgFMm9dBBJCsKv7Z06YDhNAc37uCthAOmstWp7y%2BneebzFSolW3gbuCRpMiNDv4&rsv_pq=fb76f83a00032fe4&prefixsug=phantomjs%25E4%25B8%258B%25E8%25BD%25BD&rsp=1"
    screen = Hiblog(url)
    screen.screen_shot()