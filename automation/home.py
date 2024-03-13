from pages import homePage
from factories import driver

dr = driver.Driver()
home = homePage.Home(dr.driver)

first = home.getElementByAccessilityId("item-1")
second = home.getElementByAccessilityId("item-2")
third = home.getElementByAccessilityId("item-3")

home.moveTo(second, third)

dr.Quit()