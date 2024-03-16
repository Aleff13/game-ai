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
    

def isAlreadySorted(transformedLocationList):
    return sorted(getLocationKeys(transformedLocationList))

def getLocationKeys(transformedLocationList):
    return list(transformedLocationList.keys())

def predictNewLocations(model, locationKeys):
    return model.predict([locationKeys], True)

def getKeyOfNewPlace(locationKeys, predictLocations):
    return locationKeys[locationKeys.index(predictLocations[1])-1]

def getNewLocation(model, transformEntries, getLocationKeys, predictNewLocations, getKeyOfNewPlace, elements, transformedLocationList):
    locationKeys = getLocationKeys(transformedLocationList)

    predictLocations = predictNewLocations(model, locationKeys)

    elementThatNeedToMove = transformEntries(predictLocations[0], elements)
    targetPlace = elements[getKeyOfNewPlace(locationKeys, predictLocations)]

    return elementThatNeedToMove, targetPlace

while True:
    first, second, third, elements = getElements()

    locations = getLocations(first, second, third)

    transformedLocationList = dict(sorted(locations.items(), key=lambda item: item[1]))

    if isAlreadySorted(transformedLocationList):
        break

    elementThatNeedToMove, targetPlace = getNewLocation(model, transformEntries, getLocationKeys, predictNewLocations, getKeyOfNewPlace, elements, transformedLocationList)

    home.moveTo(elementThatNeedToMove, targetPlace)
