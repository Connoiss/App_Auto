
from appium import webdriver as app_web

desired_caps = {
  "platformName": "Android",
  "platformVersion": "9",
  "deviceName": "emulator-5554",
  "appPackage": "me.mugzone.malody",  # me.mugzone.malody
  "appActivity": ".AppActivity",  # /.AppActivity
  "noReset": True,
  "unicodekeyboard": True,
  "resetkeyboard": True
}
driver = app_web.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)
