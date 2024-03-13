from model import Model
from pages import homePage
from factories import driver

model = Model()
model.loadModel("ai.keras")

dr = driver.Driver()
home = homePage.Home(dr.driver)

def transformEntries(entrie):
    elements = {
        1: first,
        2: second,
        3: third
    }
    if entrie == 1:
        return elements[1]
    elif entrie == 2:
        return elements[2]
    elif entrie == 3:
        return elements[3]
    else:
        return

while True:
    first = home.getElementByAccessilityId("item-1")
    second = home.getElementByAccessilityId("item-2")
    third = home.getElementByAccessilityId("item-3")

    locations = {
        1: first.location["y"],
        2: second.location["y"],
        3: third.location["y"]
    }

    transformedLocationList = dict(sorted(locations.items(), key=lambda item: item[1]))

    if list(transformedLocationList.keys()) == sorted(list(transformedLocationList.keys())):
        break

    locationsMap = {
        1: first,
        2: second,
        3: third
    }

    locationKeys = list(transformedLocationList.keys())

    result = model.predict([locationKeys], True)

    needToMove = transformEntries(result[0])

    keyPlace = locationKeys[locationKeys.index(result[1])-1]

    home.moveTo(needToMove, locationsMap[keyPlace])
