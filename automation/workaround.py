from appium import webdriver
from appium.options.common import AppiumOptions

from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.actions import interaction
from selenium.webdriver.common.actions.action_builder import ActionBuilder
from selenium.webdriver.common.actions.pointer_input import PointerInput
from appium.webdriver.common.appiumby import AppiumBy

capabilities = {
    'platformName': 'iOS',
    'deviceName': 'iPhone 15 Pro Max',
    'platformVersion': '17.2',
    "automationName": "XCUITest",
    'udid': 'E88AD5F7-2E83-4304-B6DD-C6AD1956106F',
    # 'app': apk_path
}

def moveTo(actions, start, final):
    actions.w3c_actions.pointer_action.click_and_hold(start)
    actions.w3c_actions.pointer_action.pause(3)
    actions.w3c_actions.pointer_action.move_to(final)

    actions.w3c_actions.pointer_action.release()
    actions.w3c_actions.perform()

driver = webdriver.Remote('http://localhost:4723/wd/hub', capabilities,
    options=AppiumOptions().load_capabilities(capabilities))

# Find the element you want to perform a long press on
item1 = driver.find_element(AppiumBy.ACCESSIBILITY_ID, 'item-1')  # Adjust locator method if necessary
item2 = driver.find_element(AppiumBy.ACCESSIBILITY_ID, 'item-2')  # Adjust locator method if necessary
item3 = driver.find_element(AppiumBy.ACCESSIBILITY_ID, 'item-3')  # Adjust locator method if necessary

actions = ActionChains(driver)
actions.w3c_actions = ActionBuilder(driver, mouse=PointerInput(interaction.POINTER_TOUCH, "touch"))
# actions.w3c_actions.pointer_action.click_and_hold(item1)
# actions.w3c_actions.pointer_action.pause(3)
# actions.w3c_actions.pointer_action.move_to(item2)
moveTo(actions, item1, item2)
# moveTo(actions, item2, item3)

# actions.w3c_actions.pointer_action.release()
# actions.w3c_actions.perform()

driver.quit()