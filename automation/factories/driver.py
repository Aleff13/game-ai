from appium import webdriver
from appium.options.common import AppiumOptions
from capabilities import capabilities

class Driver:
    def __init__(self) -> None:
        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', capabilities,
            options=AppiumOptions().load_capabilities(capabilities))
        pass

    def Quit(self):
        self.driver.quit()