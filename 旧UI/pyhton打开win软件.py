import os
import pywinauto
from pywinauto.application import Application
from pywinauto.win32functions import SetFocus


def open_app(app_dir):
    os.startfile(app_dir)


def Appium_auto():
    app = Application(backend='uia').connect(path='C:\Users\22203\\AppData\\Local\\Programs\\Appium\\Appium.exe')
    main_window = app['Appium']
    button1 = main_window.child_window(
        title="Start Server v1.15.1",
        control_type="Button")
    button1.click()


Chrome_RenderWidgetHostHWND
Leidian = r'"C:\Users\22203\Desktop\雷电模拟器9.lnk"'
Appium_auto()
# open_app(Leidian)
