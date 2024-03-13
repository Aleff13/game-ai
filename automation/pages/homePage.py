from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.actions import interaction
from selenium.webdriver.common.actions.action_builder import ActionBuilder
from selenium.webdriver.common.actions.pointer_input import PointerInput
from appium.webdriver.common.appiumby import AppiumBy

class Home:
    def __init__(self, driver) -> None:
        self.driver = driver
        self.actions = ActionChains(driver)
        self.actions.w3c_actions = ActionBuilder(driver, mouse=PointerInput(interaction.POINTER_TOUCH, "touch"))

        pass

    def moveTo(self, start, final):
        self.actions.w3c_actions.pointer_action.click_and_hold(start)
        self.actions.w3c_actions.pointer_action.pause(3)
        self.actions.w3c_actions.pointer_action.move_to(final)

        self.actions.w3c_actions.pointer_action.release()
        self.actions.w3c_actions.perform()

    def getElementByAccessilityId(self, id: str):
        return self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, id)
