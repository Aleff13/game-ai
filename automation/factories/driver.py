from appium import webdriver
from appium.options.common import AppiumOptions
from capabilities import capabilities

class Driver:
    def __init__(self, serverHost = 'http://localhost:4723/wd/hub') -> None:
        self.driver = webdriver.Remote(serverHost, capabilities,
            options=AppiumOptions().load_capabilities(capabilities))
        pass

    def Quit(self):
        self.driver.quit()