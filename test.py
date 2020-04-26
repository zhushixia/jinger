import time
import win32api
import win32con
import win32gui

def operate_win(x, y):
    hWndList = []
    win32gui.EnumWindows(lambda hWnd, param: param.append(hWnd), hWndList)
    print(hWndList)
    for hwnd in hWndList:
        # 获取窗口名字
        title = win32gui.GetWindowText(hwnd)
        classname = win32gui.GetClassName(hwnd)
        if title == "Microsoft Excel":
            print(title)
            win32api.keybd_event(13, 0, 0, 0)  #
            win32gui.SetForegroundWindow(hwnd)
            # 获取鼠标当前位置的坐标
            print(win32api.GetCursorPos())
            # 将鼠标移动到坐标处
            win32api.SetCursorPos((x, y))
            # 左点击
            win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 100, 100, 0, 0)
            time.sleep(2)
            win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 100, 100, 0, 0)

if __name__ == "__main__":
    while True:
        time.sleep(2)
        operate_win(600, 400)

