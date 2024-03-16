from model import Model
from pages import homePage
from factories import driver

model = Model()
model.loadModel("ai.keras")

dr = driver.Driver()
home = homePage.Home(dr.driver)

def transformEntries(entrie, elements):
    if entrie == 1:
        return elements[1]
    elif entrie == 2:
        return elements[2]
    elif entrie == 3:
        return elements[3]
    else:
        return
    
def getElements():
    first = home.getElementByAccessilityId("item-1")
    second = home.getElementByAccessilityId("item-2")
    third = home.getElementByAccessilityId("item-3")

    elementsMap = {
        1: first,
        2: second,
        3: third
    }

    return first, second, third, elementsMap

def getLocations(first, second, third):
    locations = {
        1: first.location["y"],
        2: second.location["y"],
        3: third.location["y"]
    }

    return locations
    

while True:
    first, second, third, elements = getElements()

    locations = getLocations(first, second, third)

    transformedLocationList = dict(sorted(locations.items(), key=lambda item: item[1]))

    if list(transformedLocationList.keys()) == sorted(list(transformedLocationList.keys())):
        break

    locationKeys = list(transformedLocationList.keys())

    predictResult = model.predict([locationKeys], True)

    elementToMove = transformEntries(predictResult[0], elements)

    keyPlace = locationKeys[locationKeys.index(predictResult[1])-1]

    targetLocation = elements[keyPlace]

    home.moveTo(elementToMove, targetLocation)
