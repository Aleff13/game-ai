from pages import homePage
from factories import driver

dr = driver.Driver()
home = homePage.Home(dr.driver)

first = home.getElementByAccessilityId("item-1")
second = home.getElementByAccessilityId("item-2")
third = home.getElementByAccessilityId("item-3")

print(first.location["y"])
print(second.location["y"])
print(third.location["y"])

home.moveTo(first, second)

dr.Quit()