from pathlib import Path
from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy
from appium.options.common import AppiumOptions

from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver import ActionChains
from selenium.webdriver.common.actions import interaction
from selenium.webdriver.common.actions.action_builder import ActionBuilder
from selenium.webdriver.common.actions.pointer_input import PointerInput

# apk_path = str(Path.cwd() / "app/MVCTodo.app")

capabilities = {
    'deviceName': 'iPhone 15 Pro Max',
    'platformName': 'iOS',
    'automationName': 'xcuitest',
    'platformVersion': '17.2',
    'udid': 'E88AD5F7-2E83-4304-B6DD-C6AD1956106F',
    # 'app': apk_path
}

driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', 
    options=AppiumOptions().load_capabilities(capabilities))

# driver.shake()

item1 = driver.find_element(AppiumBy.ACCESSIBILITY_ID, 'item-1')
item2 = driver.find_element(AppiumBy.ACCESSIBILITY_ID, 'item-2')

print(item1)
print(item2.location)

item1.click()
# actions = ActionChains(driver)
# # override as 'touch' pointer action
# actions.w3c_actions = ActionBuilder(driver, mouse=PointerInput(interaction.POINTER_TOUCH, "touch"))
# actions.w3c_actions.pointer_action.double_click(item1)
# actions.w3c_actions.pointer_action.release()
# actions.perform()
