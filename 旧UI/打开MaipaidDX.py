from appium import webdriver as app_web

desired_caps = {
    "platformName": "Android",
    "platformVersion": "9",
    "deviceName": "emulator-5554",
    "appPackage": "com.Reflektone.MaipadDX",   # com.Reflektone.MaipadDX
    # com.unity3d.player.UnityPlayerActivity
    "appActivity": "com.unity3d.player.UnityPlayerActivity",
    "noReset": True,
    "unicodekeyboard": True,
    "resetkeyboard": True
}
driver = app_web.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)
driver.implicitly_wait(10000)
driver.quit()
