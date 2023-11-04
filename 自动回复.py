from appium import webdriver as app_web
from selenium.webdriver.common.by import By
from appium.webdriver.extensions.android.nativekey import AndroidKey

desired_caps = {
    'platformName': 'Android',  # 使用哪个移动操作系统平台
    'udid': 'emulator-5554',  # 连接的物理设备的唯一设备标识符
    'deviceName': 'deviceName',  # 使用的移动设备或模拟器的种类
    'platformVersion': '9',  # 移动操作系统版本
    'appPackage': 'com.tencent.mobileqq',  # apk包名com.tencent.mobileqq
    'appActivity': '.activity.SplashActivity',  # apk的launcherActivity .activity.SplashActivity
    'unicodeKeyboard': True,  # 使用unicodeKeyboard的编码方式来发送字符串，避免中文报错
    'noReset': True,
}
driver = app_web.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)
driver.implicitly_wait(20)  # 若无响应的情况下，等待20秒再报错，与time．sleep相似，这里针对每一个动作
# driver.find_element_by_id('com.tencent.mobileqg:id/btn_login').click()  # 点击登录
# driver.find_element_by_accessibility_id("请输入QQ号码或手机或邮箱").send_keys("你的QQ号码")
# driver.find＿element＿by＿id("com.tencent.mobileq:id/password").send_keys("你的密码")
# driver.find_element_by_id('com.tencent.mobileqg:id/login'). click()   # 登录
driver.find_element(By.ID, 'name').click()  # 点击搜索框find_element_by_id
driver.find_element(By.ID, 'id/et_search_keyword').send_keys("Captain")  # 搜索
driver.find_element(By.ID, 'id/title').click()    # 选中搜索的人
driver.find_element(By.ID, 'id/input').send_keys("我是自动化测试工具")  # 输入要发送的消息
driver.find_element(By.ID, 'id/name').click()   # 发送

#   https://blog.csdn.net/m0_37497061
